
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


# Mock sentiment analysis API
def mock_sentiment_api(text):
    import random
    return random.uniform(0, 1)


def fetch_yourstory_articles(ticker, limit=5):
    url = f"https://yourstory.com/search?q={ticker}&page=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

    # articles = soup.find_all('h2', class_='title')[:limit]
    # print(articles)
    # return [article.text for article in articles]

fetch_yourstory_articles('HDFC')

# Fetch articles from Finshots
def fetch_finshots_articles(ticker, limit=5):
    url = f"https://finshots.in/search/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2', class_='title')[:limit]
    return [article.text for article in articles]



# Fetch and process data
def fetch_and_process_data():
    tickers = ['HDFC', 'Tata Motors']
    all_articles = []

    for ticker in tickers:
        yourstory_articles = fetch_yourstory_articles(ticker)
        finshots_articles = fetch_finshots_articles(ticker)
        articles = yourstory_articles + finshots_articles
        unique_articles = list(set(articles))  # Deduplication

        for article in unique_articles:
            sentiment_score = mock_sentiment_api(article)
            all_articles.append({'ticker': ticker, 'article': article, 'sentiment_score': sentiment_score})

    return pd.DataFrame(all_articles)


def pipeline():
    data = fetch_and_process_data()
    # persist_data(data)
    data.to_csv("result.csv")
    print(f"Pipeline executed at {time.strftime('%Y-%m-%d %H:%M:%S')}")


# pipeline()