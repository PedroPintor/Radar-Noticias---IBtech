# Imagem base - Python 3.11 versão slim (menor tamanho)
FROM python:3.11-slim

# Definir variáveis de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Definir diretório de trabalho no container
WORKDIR /app

# Instalar dependências primeiro (para aproveitar o cache em camadas do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que a aplicação utilizará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "run.py"]