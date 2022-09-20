from locust import HttpUser, task, TaskSet, between

class FileExtensionTaskSet(TaskSet):
    @task
    def gifv_mp4(self):
        self.client.get('/unsafe/filters:gifv(mp4)/https://images.mamilove.com.tw/test/product/details/1f3f1844-0cc2-11ed-9b01-0242c0a85007.gif')

    @task
    def gifv_webm(self):
        self.client.get('/unsafe/filters:gifv(webm)/https://images.mamilove.com.tw/test/product/details/1f3f1844-0cc2-11ed-9b01-0242c0a85007.gif')

class FilesizeTaskSet(TaskSet):
    @task
    def gifv_mp4_500kb(self):
        self.client.get('/unsafe/filters:gifv(mp4)/https://images.mamilove.com.tw/origin/setting/1020-66dad6da5e-1464252506.gif')

    @task
    def gifv_mp4_1000kb(self):
        self.client.get('/unsafe/filters:gifv(mp4)/https://images.mamilove.com.tw/origin/setting/1166-480ce4d784-1510730146.gif')

    @task
    def gifv_mp4_2000kb(self):
        self.client.get('/unsafe/filters:gifv(mp4)/https://images.mamilove.com.tw/test/product/details/1f3f1844-0cc2-11ed-9b01-0242c0a85007.gif')

class Benchmark(HttpUser):
    tasks = [FileExtensionTaskSet]
    wait_time = between(1, 5)
