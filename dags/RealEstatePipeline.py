from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='RealEstatePipeline',
    default_args=default_args,
    start_date=datetime(2024,1,1),
    schedule='@daily',
    catchup=False
) as dag:

    extractData=BashOperator(
        task_id='extractData',
        bash_command='python3 ~/Documents/Projects/RealEstate/Code/BatchExtract.py',
        dag=dag
    )

    saveToFiles=BashOperator(
        task_id='saveToFiles',
        bash_command='python3 ~/Documents/Projects/RealEstate/Code/SaveToFiles.py',
        dag=dag
    )

    saveToDatabase=BashOperator(
        task_id='saveToDatabase',
        bash_command='python3 ~/Documents/Projects/RealEstate/Code/SaveToDatabase.py',
        dag=dag
    )

    extractData >> saveToFiles >> saveToDatabase