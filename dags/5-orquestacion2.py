from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="orquestacion2", 
         description='Programando la orquestación2',
         schedule_interval="0 7 * * 1",
         default_args={"depends_on_past": True}, 
         max_active_runs=1,
         start_date=datetime(2024, 1, 25)) as dag:

    t0 = DummyOperator(task_id="zero_task")

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 2 && echo 'Tarea 1'")

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 2 && echo 'Tarea 2'")

    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 2 && echo 'Tarea 3'")

    t4 = BashOperator(task_id="tarea4",
                      bash_command="sleep 2 && echo 'Tarea 4'")

    tn = DummyOperator(task_id="final_task")

    t0 >> t1 >> t2 >> [t3,t4] >> tn
