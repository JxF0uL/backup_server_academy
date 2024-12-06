# Usar uma imagem base com Python 3.12 e Alpine
FROM python:3.12-alpine

# Configurar diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app

# Instalar dependências do sistema
RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    curl \
    bash \
    make

# Atualizar o pip
RUN pip install --no-cache-dir --upgrade pip

# Copiar e instalar as dependências do projeto
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Coletar os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor a porta do Gunicorn
EXPOSE 8090

# Comando para rodar o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8090", "AOEP.wsgi:application"]
