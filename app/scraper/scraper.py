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
            print(f"Erro ao obter notícias do G1: {e}")
    
    # UOL - Meio Ambiente
    try:
        response = requests.get('https://noticias.uol.com.br/meio-ambiente/')
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('div', class_='thumbnails-item', limit=3):
            title_tag = item.find('h3')
            link = item.find('a')
            image = item.find('img')
            
            if title_tag and link:
                news_list.append({
                    'title': title_tag.text.strip(),
                    'link': link['href'],
                    'source': 'UOL',
                    'category': 'Meio Ambiente',
                    'description': '',
                    'date': '',
                    'image': image['src'] if image else '',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
    except Exception as e:
        print(f"Erro ao obter notícias do UOL: {e}")
    
    # Folha de São Paulo - Ambiente
    try:
        response = requests.get('https://www1.folha.uol.com.br/ambiente/')
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('div', class_='c-main-headline', limit=3):
            title_tag = item.find('h2', class_='c-main-headline__title')
            link = item.find('a')
            description = item.find('p')
            
            if title_tag and link:
                news_list.append({
                    'title': title_tag.text.strip(),
                    'link': link['href'],
                    'source': 'Folha de S.Paulo',
                    'category': 'Ambiente',
                    'description': description.text.strip() if description else '',
                    'date': '',
                    'image': '',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
    except Exception as e:
        print(f"Erro ao obter notícias da Folha: {e}")
    
    return news_list