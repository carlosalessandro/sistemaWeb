# 🚀 Guia de Deploy

Como fazer deploy do LangChain AI System em produção.

## 📋 Pré-requisitos

- Servidor Linux (Ubuntu 20.04+ recomendado)
- Python 3.8+
- PostgreSQL ou MySQL (recomendado para produção)
- Nginx
- Supervisor ou systemd
- Domínio configurado

---

## 🐳 Deploy com Docker (Recomendado)

### 1. Criar Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "sistemaWeb.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### 2. Criar docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    command: gunicorn sistemaWeb.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/static
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=langchain_db
      - POSTGRES_USER=langchain_user
      - POSTGRES_PASSWORD=secure_password

  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/static
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
```

### 3. Build e Run

```bash
docker-compose up -d --build
```

---

## 🖥️ Deploy Manual (Ubuntu)

### 1. Preparar Servidor

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install python3-pip python3-venv nginx postgresql -y
```

### 2. Configurar PostgreSQL

```bash
sudo -u postgres psql

CREATE DATABASE langchain_db;
CREATE USER langchain_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE langchain_db TO langchain_user;
\q
```

### 3. Clonar e Configurar Projeto

```bash
cd /var/www
git clone https://github.com/seu-usuario/langchain-ai-system.git
cd langchain-ai-system

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

### 4. Configurar .env

```bash
nano .env
```

```env
DEBUG=False
SECRET_KEY=sua-chave-secreta-super-segura
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DATABASE_URL=postgresql://langchain_user:secure_password@localhost/langchain_db
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 5. Migrar Banco de Dados

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 6. Configurar Gunicorn

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

```ini
[Unit]
Description=Gunicorn daemon for LangChain AI System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/langchain-ai-system
ExecStart=/var/www/langchain-ai-system/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/var/www/langchain-ai-system/gunicorn.sock \
          sistemaWeb.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 7. Configurar Nginx

```bash
sudo nano /etc/nginx/sites-available/langchain
```

```nginx
server {
    listen 80;
    server_name seu-dominio.com www.seu-dominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/langchain-ai-system;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/langchain-ai-system/gunicorn.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/langchain /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 8. Configurar SSL (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com
```

---

## ☁️ Deploy em Cloud

### Heroku

```bash
# Instalar Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login

# Criar app
heroku create langchain-ai-system

# Adicionar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Configurar variáveis
heroku config:set OPENAI_API_KEY=sk-sua-chave
heroku config:set SECRET_KEY=sua-chave-secreta
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Migrar
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### AWS (EC2)

1. Criar instância EC2 (Ubuntu)
2. Configurar Security Groups (portas 80, 443, 22)
3. Seguir passos do deploy manual
4. Configurar RDS para PostgreSQL
5. Usar S3 para arquivos estáticos

### Google Cloud Platform

```bash
# Instalar gcloud CLI
curl https://sdk.cloud.google.com | bash

# Inicializar
gcloud init

# Deploy
gcloud app deploy
```

---

## 🔒 Segurança

### Checklist de Segurança

- [ ] DEBUG=False em produção
- [ ] SECRET_KEY forte e única
- [ ] ALLOWED_HOSTS configurado
- [ ] SSL/HTTPS habilitado
- [ ] Firewall configurado
- [ ] Backup automático do banco
- [ ] Rate limiting habilitado
- [ ] CORS configurado corretamente
- [ ] Logs de segurança ativos
- [ ] Atualizações regulares

### Configurações Recomendadas

```python
# settings.py (produção)

DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://seu-dominio.com",
]
```

---

## 📊 Monitoramento

### Logs

```bash
# Gunicorn logs
sudo journalctl -u gunicorn

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Application logs
tail -f /var/www/langchain-ai-system/logs/django.log
```

### Ferramentas Recomendadas

- **Sentry** - Rastreamento de erros
- **New Relic** - Performance monitoring
- **Datadog** - Infraestrutura
- **Prometheus + Grafana** - Métricas

---

## 🔄 CI/CD

### GitHub Actions

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /var/www/langchain-ai-system
            git pull
            source venv/bin/activate
            pip install -r requirements.txt
            python manage.py migrate
            python manage.py collectstatic --noinput
            sudo systemctl restart gunicorn
```

---

## 💾 Backup

### Backup Automático

```bash
#!/bin/bash
# backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"

# Backup banco de dados
pg_dump langchain_db > $BACKUP_DIR/db_$DATE.sql

# Backup arquivos
tar -czf $BACKUP_DIR/files_$DATE.tar.gz /var/www/langchain-ai-system

# Limpar backups antigos (manter últimos 7 dias)
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
```

```bash
# Adicionar ao crontab
crontab -e

# Backup diário às 2h
0 2 * * * /path/to/backup.sh
```

---

## 🆘 Troubleshooting

### Problema: Gunicorn não inicia

```bash
sudo systemctl status gunicorn
sudo journalctl -u gunicorn -n 50
```

### Problema: Nginx 502 Bad Gateway

```bash
# Verificar socket
ls -l /var/www/langchain-ai-system/gunicorn.sock

# Verificar permissões
sudo chown www-data:www-data /var/www/langchain-ai-system
```

### Problema: Static files não carregam

```bash
python manage.py collectstatic --noinput
sudo systemctl restart nginx
```

---

## 📞 Suporte

Problemas com deploy?
- 📧 Email: deploy@langchain-ai.com
- 💬 Discord: [Link do servidor]
- 📖 Docs: https://docs.langchain-ai.com/deploy

---

**Deploy bem-sucedido!** 🎉
