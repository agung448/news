from flask import Flask, render_template
from api_nyt import get_popular_articles

app = Flask(__name__)
API_KEY = ''

@app.route('/')
def index():
    articles = get_popular_articles(API_KEY)
    return render_template('index.html',articles=articles)

if __name__ == '__main__':
    app.run(debug=True)