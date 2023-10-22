from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'kafka_workflow',
    default_args=default_args,
    description='A simple Kafka producer-consumer workflow',
    schedule_interval=timedelta(minutes=1),
    start_date=datetime(2023, 10, 10),
    catchup=False,
)

# Assume producer.py and consumer.py are in the ~/airflow/dags/ folder or provide the full path


produce_task = BashOperator(
    task_id='produce_to_kafka',
    bash_command='cd /opt/airflow && make produce-to-kafka',
    dag=dag,
)

consume_task = BashOperator(
    task_id='consume_from_kafka',
    bash_command='cd /opt/airflow && make consume-from-kafka',
    dag=dag,
)

produce_task >> consume_task

