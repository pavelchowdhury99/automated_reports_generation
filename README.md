# Automated Report Generation Using Python and Airflow

## Objective 
To create an Reporting ETL pipeline using Airflow and Python and update after particular intervals.

## Tools used
- Python
  - Webscraping
  - newspaper package
  - Pycharm IDE
- ETL Pipeline using Airflow
- Version control - Git using GitHub
- Docker and docker-compose

## Design Architecture
1. Get the latest news related to a phrase/keyword from 1st page of Google search result.
2. Get all the links, content of the pages and images link
3. Create summary of each news article
4. Put into an HTML file
5. Run this procedure after given intervals using Airflow

## Learnings from this exercise
- Creating news article summarizer
- Introduction to Docker and Docker Compose
- Introduction to Airflow
- Creation of reporting pipeline using Python

## References 
1. [Airflow docker-compose](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
2. [Newspaper Package](https://newspaper.readthedocs.io/en/latest/)
3. [gnews Package](https://pypi.org/project/gnews/)
4. [Download and install Docker](https://docs.docker.com/get-docker/)
5. [Docker-compose](https://docs.docker.com/compose/install/)
6. [Docker references](https://docs.docker.com/reference/)
7. [Airflow Python Operator](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html)
8. [Airflow Documentation](https://airflow.apache.org/docs/)


## Walkthrough
[![How to generate automated reports using Python & Airflow? | Report automation with Python](https://yt-embed.herokuapp.com/embed?v=7GIr71X9_tc)](https://youtu.be/7GIr71X9_tc "How to generate automated reports using Python & Airflow? | Report automation with Python")
