#! python3

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime as dt
import sys
# you need this so airflow can properly import modules, look for permanent way to do this. 
sys.path.append('/home/thomas/airflow/dags/foodyscores/')
# import from asks gahealth
from tasks.gahealth import grabHealthScores,processGaHealthScores

default_args = {
    'owner': 'tbae2',
    'depends_on_past': False,
    'start_date': dt.datetime.today()
}


dag = DAG(
    dag_id='foody_scores',
    description='DAG to process and correlate food health scores and yelp',
    default_args=default_args
)



extractGaHealth = PythonOperator(
    task_id = 'extract_ga_health_scores',
    python_callable=grabHealthScores,
    dag=dag
)

processGaHealth = PythonOperator(
    task_id = 'processs_extracted_ga_health_scores',
    python_callable=processGaHealthScores,
    dag=dag
)



extractGaHealth >> processGaHealth