import requests

def get_popular_articles(api_key):
    url = f'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results',[])
    else:
        print("error fetching data from New York Time API:", response.status_code)
        return[]