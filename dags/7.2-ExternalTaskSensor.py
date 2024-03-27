from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(dag_id="7.2-externalTaskSensor",
         description="DAG Secundario",
         schedule_interval="@daily",
         start_date=datetime(2024, 3, 20),
         end_date=datetime(2024, 3, 26),
         max_active_runs=1) as dag:

    t0 = DummyOperator(task_id="zero_task")

    t1 = ExternalTaskSensor(task_id="waiting_dag",
                            external_dag_id="7.1-externalTaskSensor",
                            external_task_id="tarea1",
                            poke_interval=10)

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 10 && echo 'DAG 2 finalizado!'",
                      depends_on_past=True)

    tn = DummyOperator(task_id="final_task")

    t0 >> t1 >> t2 >> tn
