##
import nltk
from newspaper import Article
import ssl
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def set_global_ssl():
    '''Sets SSL bypass for the program'''
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


# download punkt if not present
def download_nltk_resources():
    '''
    Downloads NLTK's punkt resource from given
    list and handles ssl and already existing errors
    '''
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')


def get_news_from_article(url):
    '''
    :param url: str
    :return: Article
    '''
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article


def get_all_the_links_from_google_news(topic,max_articles=10):
    topic = '+'.join(topic.split())
    url = f'https://www.google.com/search?q={topic}&tbm=nws&tbs=qdr:d'
    with HTMLSession() as session:
        res = session.get('https://www.google.com/search?q=mobiles+phones&tbm=nws&tbs=qdr:d')
        res.html.render()
    page = BeautifulSoup(res.text, 'html.parser')
    # links = [a.get('href') for a in page.find_all('a', {'class_': 'WlydOe', 'jsnname': 'YKoRaf'})]
    # links = [a.get('href') for a in page.find_all('a', {'class': 'WlydOe'})]
    links = [a.get('href') for a in page.find_all('a', {'jsname': "YKoRaf",'class': 'WlydOe'})]
    return links[:max_articles]


if __name__ == '__main__':
    # Global configs
    set_global_ssl()
    topic = 'news in india'
    max_articles = 100
    country = 'India'
    last_n_days = '1d'
    language = 'en'

    ## testing newspaper3k
    # url = 'https://www.hindustantimes.com/india-news/skill-development-the-way-forward-for-new-india-pm-to-iti-students-101663437733979.html'
    # url = 'news.google.com/./articles/CAIiEKRJx1MS6qn_5NNxbi5cb9QqFwgEKg4IACoGCAoww7k_MMevCDCj7PkG?uo=CAUibmh0dHBzOi8vd3d3LmhpbmR1c3RhbnRpbWVzLmNvbS9pbmRpYS1uZXdzL2hvdy1pbmRpYS1wbGFucy10by1zb2x2ZS1pdHMtbG9naXN0aWNzLWdyaWRsb2NrLTEwMTY2MzY1MjY5OTUyOS5odG1s0gEA&hl=en-IN&gl=IN&ceid=IN%3Aen'
    # article = get_news_from_article(url)
    # print(article.authors)
    # print(article.publish_date)
    # print(article.title)
    # print(article.top_image)
    # print(article.summary)

    ## Getting links of all the articles
    print(len(get_all_the_links_from_google_news(topic,max_articles)))
