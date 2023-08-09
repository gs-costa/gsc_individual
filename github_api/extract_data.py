import requests
import json
from pprint import pprint

with open("/home/gustavocosta/Repositories/gsc_individual/github_api/credentials.json", encoding='utf-8') as creds:
    creds = json.load(creds)

class ExtractData():
    def __init__(self, url, username) -> None:
        self.username = username
        self.header = {
            "Accept": "application/vnd.github+json",
            "Authorization": creds['github_token'],
            "X-GitHub-Api-Version": "2022-11-28"
        }
        self.url = url
        pass

    def request_get(self):
        return requests.get(self.url, headers=self.header)
    
    def response_json(self):
        return self.request_get().json()
    
    def received_events_url(self):
        return self.response_json()['received_events_url']
    
    def get_received_events(self):
        return requests.get(self.received_events_url(), headers=self.header)
    
    def get_received_events_json(self):
        return self.get_received_events().json()
