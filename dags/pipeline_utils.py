import nltk
from newspaper import Article
import ssl
import jinja2
from datetime import datetime
# from pipeline_config import *
from gnews import GNews


def set_global_ssl():
    '''Sets SSL bypass for the program'''
    print('Setting global SSL')
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
    print('Downloading ntlk resources')
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')


def get_news_from_article(url):
    '''
    :param url: str
    :return: Article
    '''
    print(f'Getting NewsArticle for {url}')
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article
    except:
        return None


def get_all_the_links_from_google_news(topic, max_articles=5):
    print(f'Getting all the news links for {topic}')
    news = GNews(language='en', country='IN', period='1d', max_results=max_articles)
    links = [article['url'] for article in news.get_news(topic)]
    print(f'Got {len(links)} links')
    return links


def create_news_summary_output(topic, template_text, output_file_path, max_articles=5):
    print('Creating summaries and html file')
    articles = [get_news_from_article(url) for url in get_all_the_links_from_google_news(topic, max_articles)]
    articles = [a for a in articles if (a and a.summary != '')]

    template = jinja2.Template(template_text)

    context = {
        "articles": articles,
        "today": datetime.today().strftime('%b %d, %Y')
    }

    with open(output_file_path, mode="w", encoding="utf-8") as output_page:
        output_page.write(template.render(context))
        print(f"wrote {output_file_path}")

    print('create_news_summary_output - complete')


if __name__ == '__main__':
    set_global_ssl()
    download_nltk_resources()
    TOPIC = 'news in india'
    TEMPLATE_FILE_PATH = '/Users/pavelchowdhury/Documents/automated_report_generation/dags/news_template.html'
    OUTPUT_FILE_PATH = '/Users/pavelchowdhury/Documents/automated_report_generation/dags/NewsSummary.html'
    # links = get_all_the_links_from_google_news(topic=TOPIC, max_articles=3)
    # articles = [get_news_from_article(link) for link in links]
    # articles = [article for article in articles if (article and article.summary)]
    # for a in articles:
    #     print(a.title, a.summary, a.top_image, sep='\n')
    with open(TEMPLATE_FILE_PATH, 'r') as file:
        TEMPLATE_TEXT = file.read()
    create_news_summary_output(topic=TOPIC, template_text=TEMPLATE_TEXT, output_file_path=OUTPUT_FILE_PATH,
                               max_articles=5)
