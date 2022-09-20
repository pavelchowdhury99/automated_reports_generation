# Automated Report Generation Using Python and Airflow

## Flow
1. Scrap gold price as of today from Google
2. Store in SQL
3. Build New Scraper and Summarizer for n article for each topic given config topic
4. Put into pdf
5. Send via email
6. Put everything in airflow and schedule for everyday