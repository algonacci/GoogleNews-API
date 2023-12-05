import os
from flask import Flask, jsonify
from newsapi import NewsApiClient

app = Flask(__name__)

# Initialize NewsApiClient
# Replace with your API key
newsapi = NewsApiClient(api_key='81e804516d3e4aa1a30c220d12b165c8')


@app.route('/news/<keyword>')
def get_news(keyword):
    try:
        # Search for news articles containing the keyword
        articles = newsapi.get_everything(q=keyword,
                                          language='id',
                                          )

        # Extract and format relevant information from the articles
        formatted_articles = []
        for article in articles['articles']:
            formatted_article = {
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'publishedAt': article['publishedAt'],
                'source': article['source']['name']
            }
            formatted_articles.append(formatted_article)

        return jsonify({'articles': formatted_articles})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
