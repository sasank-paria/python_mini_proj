from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
#nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
googlenews=GoogleNews(start='03/29/2022',end='03/30/2022')
googlenews.search('covid19')
result=googlenews.get_news('title')
print(result)