from flask import Flask, jsonify, request, render_template
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_news():
    # Make API call to news source
    url = ('https://newsapi.org/v2/everything?'
       'q=Military&'
       'from=2023-01-26&'
       'sortBy=popularity&'
       'apiKey=0b6e8b7415534e36b2f18cf4a162a46c')
    response = requests.get(url)
    print(response.status_code)
    data= response.json()
    news_list = []
    print(data)
    # Extract URLs and news topics from API response
    for article in data['articles']:
        url = article['url']
        print(url)
        topic = article['title']
        print(topic)
        news_list.append({'url': url, 'topic': topic})
    
    #news_list = jsonify(news_list)
    return render_template('index.html', news_list=news_list)

if __name__ == '__main__':
    app.run(debug=True)
