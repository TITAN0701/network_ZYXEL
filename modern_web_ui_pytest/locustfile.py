from locust import HttpUser, task, between


class WebUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def login(self):
        self.client.get("/login")
        self.client.post(
            "/authenticate",
            data={
                "username": "tomsmith",
                "password": "SuperSecretPassword!",
            },
        )
