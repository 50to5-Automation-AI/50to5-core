from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import logging
import json
from initialize_agents import load_config, create_initialization_agent, create_quality_control_agent

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
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

config = load_config('config.json')

def initialize_environment():
    init_agent_config = config["initialization_agent"]
    initialization_agent = create_initialization_agent(init_agent_config)
    initialization_agent.initialize_environment()

def monitor_quality():
    qc_agent_config = config["quality_control_agent"]
    quality_control_agent = create_quality_control_agent(qc_agent_config)
    quality_control_agent.monitor_state()

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