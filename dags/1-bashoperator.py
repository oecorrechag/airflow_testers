from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

with DAG(dag_id="bashoperator",
         description="Utilizando bash Operator",
         max_active_runs=1,
         start_date=datetime(2024, 3, 1), 
         end_date=datetime(2024, 3, 20)) as dag:

    t1= BashOperator(task_id="hello_with_bash",
                     bash_command="echo 'Hi Platzi people from bash operator'")
    
    t1
