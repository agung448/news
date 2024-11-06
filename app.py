from flask import Flask, render_template
from api_nyt import get_popular_articles

app = Flask(__name__)
API_KEY = 'GrGK6LRD1ibC4dAPuXeW8gkZZyA5Xnlp'

@app.route('/')
def index():
    articles = get_popular_articles(API_KEY)
    return render_template('index.html',articles=articles)

if __name__ == '__main__':
    app.run(debug=True)