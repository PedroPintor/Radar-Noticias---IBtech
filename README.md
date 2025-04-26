# 🌎 Radar Notícias IBtech

Um aplicativo web que coleta e exibe notícias sobre sustentabilidade e meio ambiente de diferentes fontes.

## ✨ Funcionalidades

- 📰 Coleta notícias de G1, UOL e Folha
- 🔍 Filtros por fonte e categoria
- 📱 Interface responsiva e moderna

## 🛠️ Tecnologias

- 🐍 Python + Flask
- 🌐 HTML/CSS/JavaScript
- 🐳 Docker
- 🔄 BeautifulSoup + Requests

## 🚀 Como Executar

### 1. Com Docker (Recomendado)

```bash
# Construir a imagem
docker build -t radar-noticias-ibtech .

# Executar o container
docker run -p 5000:5000 radar-noticias-ibtech
```

### Com Python Local

```bash
# Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências e executar
pip install -r requirements.txt
python run.py
```

Acesse: http://localhost:5000

## 📁 Estrutura

```
radar-noticias-ibtech/
├── app/
│   ├── __init__.py     # Inicialização da aplicação
│   ├── routes/         # Rotas da aplicação
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── scraper/        # Funções de scraping
│   │   ├── __init__.py
│   │   └── scraper.py
│   ├── static/         # CSS e recursos
│   │   └── style.css
│   └── templates/      # HTML
│       └── index.html
├── run.py              # Script de execução
├── requirements.txt    # Dependências
├── Dockerfile          # Configuração Docker
└── .dockerignore       # Arquivos ignorados pelo Docker
```

---

💻 Desenvolvido para IBtech | 2025
