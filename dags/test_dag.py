import pendulum

from airflow import DAG
from airflow.decorators import task

with DAG(
        dag_id='example_python_operator',
        schedule=None,
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=['example'],
) as dag:
    # @task.virtualenv(
    #     task_id="virtualenv_python", requirements=(lambda: open("/opt/airflow/dags/requirements.txt").readlines())(), system_site_packages=False
    # )
    @task(task_id="virtualenv_python")
    def callable_virtualenv():
        from pyppeteer.launcher import Launcher
        print(' '.join(Launcher().cmd))

        import sys
        sys.path.append('/opt/airflow/dags/programs/scratch')
        sys.path.append('/opt/airflow/dags/programs/config')
        import nltk
        from newspaper import Article
        import ssl
        from bs4 import BeautifulSoup
        from requests_html import HTMLSession
        import jinja2
        from datetime import datetime
        from config import TOPIC, MAX_ARTICLES, TEMPLATE_FILE, OUTPUT_HTML
        from scratch import set_global_ssl, download_nltk_resources, create_news_summary_output
        print(TOPIC, MAX_ARTICLES, TEMPLATE_FILE, OUTPUT_HTML)
        OUTPUT_HTML = f'/opt/airflow/dags/{OUTPUT_HTML}'
        set_global_ssl()
        download_nltk_resources()
        create_news_summary_output(TOPIC, TEMPLATE_FILE,OUTPUT_HTML, MAX_ARTICLES)


    virtualenv_task = callable_virtualenv()
