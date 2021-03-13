# To use this library you must run "pip install news-api"
# Otherwise must build the requests from scratch
from newsapi import NewsApiClient

API_KEY = ''
api = NewsApiClient(api_key=API_KEY)

# Key variables for API call
SPORT = 'football'
SORT = 'publishedAt'    # relevancy, popularity, publishedAt

# Getting the data from the API
news_data = api.get_everything(q=SPORT, sort_by=SORT)

# Make sure that it was successful, then parse the data
if news_data['status'] == 'ok':
    for article in news_data['articles']:
        print(article['title'])
        print(article['description'])
        print(article['url'])
