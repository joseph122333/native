from flask import Flask, jsonify, request, render_template
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_news():
    # Extract URLs and news topics from API response
    military = getMilitary()
    military_list= getUrlTitle(military)
    if military_list is None:
        military_list = []
    conspiracy = getConspiracy()
    conspiracy_list= getUrlTitle(conspiracy)
    if conspiracy_list is None:
        conspiracy_list = []
    sports = getSports()
    sports_list= getUrlTitle(sports)
    if sports_list is None:
        sports_list = []
     
    
    print(military_list)
    #news_list = jsonify(news_list)
    return render_template('index.html', military_list=military_list, conspiracy_list=conspiracy_list, sports_list=sports_list)

def getUrlTitle(articles):
    news_list = []
    for article in articles['articles']:
        url = article['url']
        #print(url)
        topic = article['title']
        #print(topic)
        news_list.append({'url': url, 'topic': topic})
    return news_list

def getMilitary():
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
    return(data)

def getSports():
    # Make API call to news source
    url = ('https://newsapi.org/v2/everything?'
       'q=Sports&'
       'from=2023-01-26&'
       'sortBy=popularity&'
       'apiKey=0b6e8b7415534e36b2f18cf4a162a46c')
    response = requests.get(url)
    print(response.status_code)
    data= response.json()
    news_list = []
    return(data)


def getConspiracy():
    # Make API call to news source
    url = ('https://newsapi.org/v2/everything?'
       'q=Conspiracy&'
       'from=2023-01-26&'
       'sortBy=popularity&'
       'apiKey=0b6e8b7415534e36b2f18cf4a162a46c')
    response = requests.get(url)
    print(response.status_code)
    data= response.json()
    news_list = []
    return(data)


if __name__ == '__main__':
    
    app.run(debug=True)
