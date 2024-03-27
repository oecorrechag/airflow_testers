from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Define the DAG
with DAG(dag_id="my_dag_with_two_tasks", start_date=datetime(2024, 3, 25)) as dag:

  # First task
  task_1 = DummyOperator(task_id="first_task")

  # Second task
  task_2 = DummyOperator(task_id="second_task")

  # Set task dependencies (task_1 needs to finish before task_2 starts)
  task_1 >> task_2
