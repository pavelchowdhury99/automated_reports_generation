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
    @task.virtualenv(
        task_id="virtualenv_python", requirements=["Jinja2==3.1.2","requests-html==0.10.0","bs4==0.0.1","lxml==4.9.1","newspaper3k==0.2.8","nltk==3.7","requests-html==0.10.0","urllib3==1.26.12"], system_site_packages=True
    )
    def callable_virtualenv():
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
        from config import TOPIC,MAX_ARTICLES,TEMPLATE_FILE,OUTPUT_HTML
        from scratch import set_global_ssl,download_nltk_resources,create_news_summary_output
        print(TOPIC,MAX_ARTICLES,TEMPLATE_FILE,OUTPUT_HTML)
        OUTPUT_HTML=f'/opt/airflow/dags/{OUTPUT_HTML}'
        set_global_ssl()
        download_nltk_resources()
        create_news_summary_output(TOPIC, TEMPLATE_FILE, MAX_ARTICLES)



    virtualenv_task = callable_virtualenv()