
╔════════════════════════════════════════════════════════════════════════════════════════╗
║            CONSULTA METODOLÓGICA: DESPLIEGUE EN AWS                                   ║
║                    ERT Groundwater Predictor Pro                                      ║
╚════════════════════════════════════════════════════════════════════════════════════════╝

OBJETIVO:
Desplegar la aplicación web (Lovable) + backend (modelo ML) en AWS para acceso remoto
por gobiernos locales y equipos de campo.

═════════════════════════════════════════════════════════════════════════════════════════

1. ARQUITECTURA PROPUESTA EN AWS

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                    INTERNET                                         │
└────────────────────────────────┬────────────────────────────────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   CloudFront (CDN)      │
                    │   (Caché global)        │
                    └────────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────────┐
        │                        │                            │
    ┌───▼────────────┐    ┌─────▼─────────┐    ┌────────────▼────┐
    │  S3 (Frontend) │    │  EC2/ECS      │    │  API Gateway    │
    │  (React app)   │    │  (Backend ML) │    │  (REST APIs)    │
    └────────────────┘    └─────┬─────────┘    └────────┬────────┘
                                │                        │
                                │        ┌───────────────┘
                                │        │
                         ┌──────▼────────▼──────┐
                         │  RDS (PostgreSQL)    │
                         │  (Base de datos)     │
                         └──────────────────────┘

═════════════════════════════════════════════════════════════════════════════════════════

2. SERVICIOS AWS RECOMENDADOS

Componente          Servicio            Costo Estimado    Descripción
─────────────────────────────────────────────────────────────────────────────────────

Frontend            S3 + CloudFront     $5-10/mes         Almacenar React estático + CDN
                                                          Acceso global rápido

Backend             EC2 t2.medium       $25-35/mes        Servidor Python/FastAPI
                    o ECS Fargate       $20-30/mes        Contenedor Docker sin gestión

Base de datos       RDS PostgreSQL      $15-25/mes        PostgreSQL administrado
                    (micro)                               Backup automático

API                 API Gateway         $3-5/mes          Servless REST endpoints
                                                          Escalado automático

Almacenamiento      S3 (datos)          $1-5/mes          CSV, PNG, resultados

SSL/HTTPS           ACM (gratuito)      $0                Certificados SSL gratuitos
                    o Let's Encrypt

TOTAL ESTIMADO:                         $50-80/mes        (~$600-1000/año)

═════════════════════════════════════════════════════════════════════════════════════════

3. PASO A PASO DE DESPLIEGUE

FASE 1: Preparar el código
─────────────────────────────────────────────────────────────────────────────────────

1.1 Estructura del proyecto:
    backend/
    ├── app.py (FastAPI)
    ├── model.pkl (modelo ML entrenado)
    ├── requirements.txt
    ├── Dockerfile
    └── .env (secrets)

    frontend/
    ├── (React app compilado)
    ├── build/
    └── package.json

1.2 Crear Dockerfile:
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    EXPOSE 8000
    CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]

1.3 Crear .gitignore:
    .env
    *.pkl
    __pycache__/
    node_modules/

═════════════════════════════════════════════════════════════════════════════════════════

FASE 2: Desplegar Backend
─────────────────────────────────────────────────────────────────────────────────────

OPCIÓN A: EC2 + GitHub Actions (Recomendado para inicio)

    2.1 Crear instancia EC2 (t2.micro/t2.small)
        - OS: Ubuntu 22.04 LTS
        - Security group: permitir puertos 22, 80, 443
        - Par de claves: descargar .pem

    2.2 SSH a la instancia:
        ssh -i tu-clave.pem ubuntu@tu-ip-ec2.amazonaws.com

    2.3 Instalar dependencias:
        sudo apt update
        sudo apt install python3-pip git nginx
        pip install uvicorn fastapi python-dotenv

    2.4 Clonar repositorio:
        git clone https://github.com/tu-usuario/repo.git
        cd repo/backend
        pip install -r requirements.txt

    2.5 Ejecutar con supervisor (daemon):
        pip install supervisor
        # Crear config en /etc/supervisor/conf.d/ert.conf

    2.6 Configurar Nginx como proxy:
        sudo nano /etc/nginx/sites-available/default
        # Proxy a http://localhost:8000

    2.7 Obtener SSL gratuito:
        sudo apt install certbot python3-certbot-nginx
        sudo certbot certonly --nginx -d tu-dominio.com

OPCIÓN B: ECS + ECR (Más profesional)

    2.1 Crear repositorio ECR en AWS
    2.2 Build Docker imagen:
        docker build -t ert-backend .
    2.3 Push a ECR:
        aws ecr get-login-password | docker login ...
        docker tag ert-backend:latest xxxxx.dkr.ecr.us-east-1.amazonaws.com/ert:latest
        docker push xxxxx.dkr.ecr.us-east-1.amazonaws.com/ert:latest
    2.4 Crear task definition en ECS
    2.5 Crear service + load balancer

═════════════════════════════════════════════════════════════════════════════════════════

FASE 3: Desplegar Frontend
─────────────────────────────────────────────────────────────────────────────────────

3.1 Compilar React:
    npm run build

3.2 Crear bucket S3:
    aws s3 mb s3://ert-app-frontend

3.3 Subir archivos:
    aws s3 sync build/ s3://ert-app-frontend/ --delete

3.4 Configurar S3 para sitio estático:
    - Propiedades → Hosting de sitios estáticos
    - Index document: index.html
    - Error document: index.html

3.5 Crear distribución CloudFront:
    - Origin: tu bucket S3
    - TTL: 3600 segundos
    - SSL: ACM certificate (gratuito)

═════════════════════════════════════════════════════════════════════════════════════════

FASE 4: Configurar Base de Datos
─────────────────────────────────────────────────────────────────────────────────────

4.1 Crear RDS PostgreSQL:
    - Instance class: db.t3.micro
    - Storage: 20 GB
    - Multi-AZ: No (para desarrollo)
    - Backup retention: 7 días

4.2 Conectar desde EC2:
    psql -h tu-rds-endpoint.amazonaws.com -U admin -d ert_db

4.3 Crear tablas:
    CREATE TABLE measurements (
        id SERIAL PRIMARY KEY,
        location VARCHAR(100),
        resistance FLOAT,
        conductivity FLOAT,
        probability FLOAT,
        status VARCHAR(20),
        created_at TIMESTAMP DEFAULT NOW()
    );

═════════════════════════════════════════════════════════════════════════════════════════

FASE 5: Configurar API
─────────────────────────────────────────────────────────────────────────────────────

5.1 Crear API Gateway:
    - Crear API REST
    - Crear recursos: /measurements, /predict, /history
    - Métodos: GET, POST

5.2 Integrar con Lambda o Backend EC2:
    - POST /predict → Ejecuta modelo ML
    - GET /history → Consulta RDS
    - POST /measurements → Guarda en RDS

5.3 Habilitar CORS:
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Methods: GET, POST, OPTIONS

═════════════════════════════════════════════════════════════════════════════════════════

4. MONITOREO Y MANTENIMIENTO

CloudWatch Logs:
    - Monitorear errores del backend
    - Alertas si API cae
    - Métricas de uso

Auto-scaling:
    - EC2: Auto-scaling group (min: 1, max: 5)
    - Si CPU > 70% → agregar instancia
    - Si CPU < 30% → remover instancia

Backups:
    - RDS automated snapshots (diarios)
    - S3 versioning habilitado
    - Snapshot cada semana a S3 en otra región

Costos:
    - Monitorear con AWS Cost Explorer
    - Budget alerts en $100/mes

═════════════════════════════════════════════════════════════════════════════════════════

5. VENTAJAS Y DESVENTAJAS

VENTAJAS DE AWS:
    ✅ Escalabilidad: De 1 a 1M usuarios sin cambios
    ✅ Seguridad: Encriptación, SSL, firewalls
    ✅ Disponibilidad: 99.99% SLA
    ✅ Backup: Automático y redundante
    ✅ Monitoreo: CloudWatch incluido
    ✅ Global: CDN en 200+ ciudades

DESVENTAJAS:
    ❌ Curva de aprendizaje: AWS es complejo
    ❌ Gestión: Requiere DevOps/Admin
    ❌ Costos: Pueden crecer si no se monitorean
    ❌ Vendor lock-in: Difícil migrar después

ALTERNATIVAS MÁS SIMPLES:
    • Heroku: $7-50/mes (pero menos control)
    • Render: $7/mes (muy similar a Heroku)
    • DigitalOcean: $5-15/mes (más barato que AWS)
    • Railway: $5-50/mes (simplicidad + poder)

═════════════════════════════════════════════════════════════════════════════════════════

6. RECOMENDACIÓN PARA TU PROYECTO

Dado que es un proyecto académico y potencialmente una startup:

CORTO PLAZO (Próximos 3 meses):
    → Usar Heroku o Render
    → Bajo costo ($10-30/mes)
    → Menos configuración
    → Perfecto para MVP

MEDIANO PLAZO (6-12 meses):
    → Si tienes usuarios reales
    → Migrar a AWS + DigitalOcean
    → Mejor escalabilidad

LARGO PLAZO (1+ años):
    → AWS full-stack
    → Multi-región
    → Arquitectura enterprise

═════════════════════════════════════════════════════════════════════════════════════════

7. COMANDOS RÁPIDOS

# Ver costos estimados
aws ce get-cost-and-usage \
  --time-period Start=2026-03-01,End=2026-03-31 \
  --granularity MONTHLY \
  --metrics "UnblendedCost"

# Crear instancia EC2
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name tu-clave

# Subir a S3
aws s3 cp tu-archivo.png s3://ert-app-data/

═════════════════════════════════════════════════════════════════════════════════════════

CONCLUSIÓN:

Para tu proyecto de agua subterránea:

1. Comienza con Heroku/Render (económico, simple)
2. Backend Python FastAPI + PostgreSQL
3. Frontend React en S3 + CloudFront
4. Cuando tengas usuarios → migrá a AWS
5. Presupuesto inicial: $30-50/mes
6. Presupuesto escalado: $100-200/mes (para 1000+ usuarios)

═════════════════════════════════════════════════════════════════════════════════════════
