from locust import HttpUser, task, between
from datetime import datetime
from mparticle_config import API_KEY, PATH, NAME 
from pprint import pprint
import json

class mpLoadUser(HttpUser):
    requests_sent = 0

    @task
    def live(self):
        now = datetime.utcnow()
        payload = {
            "name": NAME,
            "date": now.strftime("%m/%d/%Y"),
            "requests_sent": mpLoadUser.requests_sent
        }

        print(payload)

        with self.client.post(
            PATH,
            data=json.dumps(payload),
            headers={"X-API-Key": API_KEY},
            catch_response=True
        ) as response:
            if response.text != '{"successful":true}':
                response.failure(f"Incorrect response message {response.text}")
        
        mpLoadUser.requests_sent += 1 
