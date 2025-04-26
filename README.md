# 🌎 Radar de Notícias sobre Sustentabilidade

Um aplicativo web que coleta e exibe notícias sobre sustentabilidade, meio ambiente e ODS de diferentes fontes.

## 🛠️ Tecnologias Utilizadas

- Python + Flask
- BeautifulSoup + Requests
- Docker
- HTML/CSS/JavaScript

## 📋 Funcionalidades

- Coleta de notícias de múltiplas fontes (G1, UOL, Folha)
- Filtros por fonte e categoria
- Exibição de imagens e descrições
- Interface responsiva e moderna

## 🚀 Como Executar

### 1. Com Docker (Recomendado)

```bash
# Construir a imagem
docker build -t radar-ibtech .

# Executar o container
docker run -p 5000:5000 radar-ibtech
```

### 2. Localmente

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py
```

Acesse: http://localhost:5000

## 📝 Estrutura do Projeto

```
radar-ibtech/
│
├── app/
│   ├── __init__.py       # Inicializador do Flask App
│   ├── routes.py         # Rotas e lógica
│   ├── scraper.py        # Funções de scraping
│   ├── templates/        # Templates HTML
│   └── static/          # Arquivos estáticos
│
├── requirements.txt      # Dependências
├── Dockerfile           # Configuração Docker
└── README.md           # Documentação
```

## 📄 Licença

Este projeto está sob a licença MIT. 