from airflow.sdk import dag, task, Context

@dag
def branch():
    
    @task
    def a():
        return 1

    @task.branch
    def b(val: int):
        if val == 1:
            return "equal_1"
        return "different_than_1"
    
    @task
    def equal_1():
        print("Equal to 1")
    
    @task
    def diferrent_than_1():
        print("Different than 1")

    val = a()
    b(val) >> [equal_1(), diferrent_than_1()]

branch()