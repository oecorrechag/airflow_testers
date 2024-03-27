from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule

def print_hello():
    return print('_____________________hello world with python in airflow_____________________')

default_args = {}

with DAG(dag_id="6.2-monitoring",
        description="Monitoreando nuestro DAG",
        schedule_interval="@daily",
        start_date=datetime(2024, 3, 1),
        end_date=datetime(2024, 3, 20),
        default_args=default_args,
        max_active_runs=1) as dag:

    t0 = DummyOperator(task_id="zero_task")

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 5 && echo 'Primera tarea!'",
                      trigger_rule=TriggerRule.ALL_SUCCESS,
                      retries=2,  #intentos
                      retry_delay=5, # tiempo entre intentos
                      depends_on_past=False)

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 3 && echo 'Segunda tarea!'",
                      retries=2,
                      retry_delay=5,
                      trigger_rule=TriggerRule.ALL_SUCCESS,
                      depends_on_past=True)

    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 2 && echo 'Tercera tarea!'",
                      retries=2,
                      retry_delay=5,
                      trigger_rule=TriggerRule.ALWAYS,
                      depends_on_past=True)

    t4 = PythonOperator(task_id="tarea4",
                        python_callable=print_hello,
                        retries=2,
                        retry_delay=5,
                        trigger_rule=TriggerRule.ALL_SUCCESS,
                        depends_on_past=True)

    t5 = BashOperator(task_id="tarea5",
                      bash_command="sleep 2 && echo 'Quinta tarea!'",
                      retries=2,
                      retry_delay=5,
                      depends_on_past=True)

    tn = DummyOperator(task_id="final_task")

    t0 >> t1 >> t2 >> t3 >> t4 >> t5 >> tn