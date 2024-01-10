from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# DAG 정의
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_airflow_dag',
    default_args=default_args,
    description='A simple Airflow DAG',
    schedule_interval=timedelta(seconds=10),  # DAG 실행 주기 (10초마다 한 번)
)

# 첫 번째 작업 정의
task1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hello Airflow"',
    dag=dag,
)

# 두 번째 작업 정의
task2 = BashOperator(
    task_id='print_world',
    bash_command='echo "World!"',
    dag=dag,
)

# 작업 간 의존성 정의
task1 >> task2

if __name__ == "__main__":
    dag.cli()

