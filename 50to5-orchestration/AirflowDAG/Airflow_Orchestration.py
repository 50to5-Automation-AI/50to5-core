from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from initialization_agent import InitializationAgent
from quality_control_agent import QualityControlAgent
import logging

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'agent_swarm_orchestration',
    default_args=default_args,
    description='A DAG to orchestrate the workflow of the Agent Swarm',
    schedule_interval=timedelta(days=1),
)

def initialize_environment():
    init_agent = InitializationAgent(
        name="InitializationAgent",
        system_message="Initialize the environment.",
        redis_config={'host': 'localhost', 'port': 6379},
        logger=logging.getLogger("InitializationAgent"),
        db_config={'dbname': 'agent_db', 'user': 'agent_user', 'password': 'password', 'host': 'localhost', 'port': '5432'}
    )
    init_agent.initialize_environment()

def monitor_quality():
    qc_agent = QualityControlAgent(
        name="QualityControlAgent",
        description="Ensures the quality control and state management of the system.",
        db_config={'dbname': 'agent_db', 'user': 'agent_user', 'password': 'password', 'host': 'localhost', 'port': '5432'}
    )
    qc_agent.monitor_state()

initialize_environment_task = PythonOperator(
    task_id='initialize_environment',
    python_callable=initialize_environment,
    dag=dag,
)

monitor_quality_task = PythonOperator(
    task_id='monitor_quality',
    python_callable=monitor_quality,
    dag=dag,
)

initialize_environment_task >> monitor_quality_task
