from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_first_page(self):
        self.client.get("")
        print("First Page")

    @task
    def get_latest_news(self):
        self.client.get("collection/latest")
        print("Latest News")
        self.interrupt(reschedule=False)

    @task
    def get_special_news(self):
        self.client.get("topic/বিশেষ-সংবাদ")
        print("Special News")
        self.interrupt(reschedule=False)

    @task
    def get_politics(self):
        self.client.get("politics")
        print("Politics")
        self.interrupt(reschedule=False)

    @task
    def get_coronavirus(self):
        self.client.get("topic/করোনাভাইরাস")
        print("Coronavirus")
        self.interrupt(reschedule=False)

    @task
    def get_bangladesh(self):
        self.client.get("bangladesh")
        print("Bangladesh")
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://www.prothomalo.com/"
    tasks = [MyHTTPCat]
    wait_time = constant(1)
