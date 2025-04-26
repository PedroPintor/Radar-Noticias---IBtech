import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def get_news():
    news_list = []
    
    # G1 - Natureza e Meio Ambiente
    g1_urls = [
        'https://g1.globo.com/natureza/',
        'https://g1.globo.com/meio-ambiente/'
    ]
    
    for url in g1_urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for item in soup.find_all('div', class_='feed-post-body', limit=3):
                title = item.find('a', class_='feed-post-link')
                description = item.find('div', class_='feed-post-body-resumo')
                time = item.find('span', class_='feed-post-datetime')
                image = item.find('img')
                
                if title:
                    news_list.append({
                        'title': title.text.strip(),
                        'link': title['href'],
                        'source': 'G1',
                        'category': 'Meio Ambiente',
                        'description': description.text.strip() if description else '',
                        'date': time.text.strip() if time else '',
                        'image': image['src'] if image else '',
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
        except Exception as e:
            print(f"Erro ao acessar {url}: {str(e)}")

    # UOL - Sustentabilidade
    try:
        uol_url = 'https://noticias.uol.com.br/meio-ambiente/'
        response = requests.get(uol_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('div', class_='thumbnails-wrapper', limit=3):
            title = item.find('h3', class_='thumb-title')
            link = item.find('a')
            description = item.find('p', class_='thumb-description')
            time = item.find('time')
            image = item.find('img')
            
            if title and link:
                news_list.append({
                    'title': title.text.strip(),
                    'link': link['href'],
                    'source': 'UOL',
                    'category': 'Sustentabilidade',
                    'description': description.text.strip() if description else '',
                    'date': time.text.strip() if time else '',
                    'image': image['src'] if image else '',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
    except Exception as e:
        print(f"Erro ao acessar UOL: {str(e)}")

    # Folha - Sustentabilidade
    try:
        folha_url = 'https://www1.folha.uol.com.br/ambiente/'
        response = requests.get(folha_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('div', class_='c-headline__content', limit=3):
            title = item.find('h2', class_='c-headline__title')
            link = item.find('a')
            description = item.find('p', class_='c-headline__standfirst')
            time = item.find('time')
            image = item.find('img')
            
            if title and link:
                news_list.append({
                    'title': title.text.strip(),
                    'link': link['href'],
                    'source': 'Folha de S.Paulo',
                    'category': 'Ambiente',
                    'description': description.text.strip() if description else '',
                    'date': time.text.strip() if time else '',
                    'image': image['src'] if image else '',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
    except Exception as e:
        print(f"Erro ao acessar Folha: {str(e)}")

    # Ordenar por timestamp e limitar a 10 notícias
    news_list.sort(key=lambda x: x['timestamp'], reverse=True)
    return news_list[:10] 