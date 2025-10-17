from airflow.sdk import dag, task
from time import sleep

@dag
def celery_dag():
    @task
    def a():
        sleep(3)

    @task(
            queue="high_cpu"
    )
    def b():
        sleep(3)

    @task(
            queue="high_cpu"
    )
    def c():
        sleep(3)

    @task
    def d():
        sleep(3)

    a() >> [b(), c()] >> d()

celery_dag()