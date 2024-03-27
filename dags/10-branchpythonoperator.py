from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, date

default_args = {
'start_date': datetime(2024, 3, 15),
'end_date': datetime(2024, 3, 25)
}

def _choose(**context):

    if context["logical_date"].date() < date(2024, 3, 20):
        return "finish_20_march"

    return "start_20_march"

with DAG('10-branching',
         schedule_interval='@daily',
         default_args=default_args) as dag:

    branching = BranchPythonOperator(task_id="branch",
                                     python_callable=_choose)

    finish_20 = BashOperator(task_id='finish_20_march',
                            bash_command="echo 'Running {{ds}}'")

    start_20 = BashOperator(task_id='start_20_march',
                              bash_command="echo 'Running {{ds}}'")

    branching >> [finish_20, start_20]
