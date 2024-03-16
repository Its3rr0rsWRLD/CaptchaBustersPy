# captchabusters/__init__.py
import requests
import json

class CaptchaBusters:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://captchabusters.com/api'

    def create_task(self, task):
        response = requests.post(f"{self.base_url}/createTask", json={
            "clientKey": self.api_key,
            "task": task
        })
        return response.json()

    def get_task_result(self, task_id):
        response = requests.post(f"{self.base_url}/getTaskResult", json={
            "clientKey": self.api_key,
            "taskId": task_id
        })
        return response.json()

    def get_balance(self):
        response = requests.post(f"{self.base_url}/getBalance", json={
            "clientKey": self.api_key
        })
        return response.json()