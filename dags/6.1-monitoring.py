from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def myfunction():
    pass

with DAG(dag_id="6.1-monitoring",
        description="Monitoreando nuestro DAG",
        schedule_interval="@daily",
        max_active_runs=1,
        start_date=datetime(2024, 3, 1),
        end_date=datetime(2024, 3, 20)) as dag:

    t0 = DummyOperator(task_id="zero_task")

    t1 = BashOperator(task_id="tarea1",
                    bash_command="sleep 2 && echo 'Primera tarea!'")

    t2 = BashOperator(task_id="tarea2",
                    bash_command="sleep 2 && echo 'Segunda tarea!'")

    t3 = BashOperator(task_id="tarea3",
                    bash_command="sleep 2 && echo 'Tercera tarea!'")

    t4 = PythonOperator(task_id="tarea4",
                    python_callable=myfunction)

    t5 = BashOperator(task_id="tarea5",
                    bash_command="sleep 2 && echo 'Quinta tarea!'")

    tn = DummyOperator(task_id="final_task")

    t0 >> t1 >> t2 >> t3 >> t4 >> t5 >> tn
