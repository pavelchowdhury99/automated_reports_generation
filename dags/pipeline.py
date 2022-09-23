import pendulum

from airflow import DAG
from airflow.decorators import task

with DAG(
        dag_id='news_paper_summary_report_daily',
        schedule=None,
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=['reporting_pipeline'],
) as dag:
    @task(task_id="news_paper_summary_report_daily")
    def news_paper_summary_report_daily():
        import sys

        sys.path.append('/opt/airflow/dags/programs/pipeline_utils')
        sys.path.append('/opt/airflow/dags/programs/pipeline_config')

        from pipeline_config import TOPIC, MAX_ARTICLES, TEMPLATE_FILE, OUTPUT_HTML
        from pipeline_utils import set_global_ssl, download_nltk_resources, create_news_summary_output

        print(TOPIC, MAX_ARTICLES, TEMPLATE_FILE, OUTPUT_HTML)

        print('reading template html')
        with open(TEMPLATE_FILE, 'r') as file:
            TEMPLATE = file.read()

        print('Starting with pipeline')
        set_global_ssl()
        download_nltk_resources()
        create_news_summary_output(TOPIC, TEMPLATE, OUTPUT_HTML, MAX_ARTICLES)


    news_paper_summary_report_daily = news_paper_summary_report_daily()
