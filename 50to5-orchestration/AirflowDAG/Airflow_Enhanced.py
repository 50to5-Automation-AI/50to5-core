from airflow.operators.dummy_operator import DummyOperator

# Define the reset task
def reset_environment():
    init_agent_config = config["initialization_agent"]
    initialization_agent = create_initialization_agent(init_agent_config)
    initialization_agent.reset_database_state()

reset_environment_task = PythonOperator(
    task_id='reset_environment',
    python_callable=reset_environment,
    dag=dag,
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Chain the tasks
start >> initialize_environment_task >> monitor_quality_task >> end
initialize_environment_task.on_failure_callback = reset_environment_task.execute
monitor_quality_task.on_failure_callback = reset_environment_task.execute
