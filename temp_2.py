# import requests
# from bs4 import BeautifulSoup
# res = requests.get('https://www.google.com/search?q=news+in+inida&tbm=nws&tbs=qdr:d')
# page = BeautifulSoup(res.text, 'html.parser')
# # links = [a.get('href') for a in page.find_all('a', {'jsname': "YKoRaf", 'class': 'WlydOe'})]
# links = [a.get('href') for a in page.find_all('a')]
# print(links)

from GoogleNews import GoogleNews
import ssl
def set_global_ssl():
    '''Sets SSL bypass for the program'''
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

set_global_ssl()
news = GoogleNews(lang='en', region='India', period='1d', encode='utf-8')
news.get_news('news in india')
print(news.results())