from airflow.sdk import dag, task, Context

@dag
def xcom_dag():
    
    @task
    def t1(context: Context):
        val = 42
        context['ti'].xcom_push(key='my_key', value=val)

    @task
    def t2(context: Context):
        val = context['ti'].xcom_pull(task_id='t1', key='my_key')
        print(val)

    t1() >> t2()

xcom_dag()