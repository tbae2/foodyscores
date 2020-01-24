#! python3

from airflow import DAG
from airflow.operators import python_operator
import datetime as dt


default_args = {
    'owner': 'tbae2',
    'depends_on_past': False,
    'start_date': dt.datetime
}


dag = DAG(
    dag_id='foody_scores',
    description='DAG to process and correlate food health scores and yelp',
    default_args=default_args
)

