import pendulum

from airflow import DAG
from airflow.decorators import task

with DAG(
        dag_id='test_dag_2',
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
        from scratch import get_all_the_links_from_google_news
        get_all_the_links_from_google_news('news in inida',2)


    virtualenv_task = callable_virtualenv()
