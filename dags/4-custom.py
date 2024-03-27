from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(dag_id="customoperator",
         description="Nuestro primer customoperator",
         max_active_runs=1,
         start_date=datetime(2024, 3, 1)) as dag:

    t1 = HelloOperator(task_id="hello",
                       name="OC")

    t1
