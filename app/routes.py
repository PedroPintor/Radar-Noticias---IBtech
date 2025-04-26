from flask import Blueprint, render_template
from app.scraper import get_news

main = Blueprint('main', __name__)

@main.route('/')
def index():
    news = get_news()
    return render_template('index.html', news=news) 