import requests
import json

# get credentials in json file
with open(
    "/home/gustavocosta/Repositories/gsc_individual/github_api/credentials.json",
    encoding='utf-8') as creds:
    creds = json.load(creds)

class ExtractData():
    def __init__(self, url, username, params=None) -> None:
        """define args"""
        self.username = username
        self.header = {
            "Accept": "application/vnd.github+json",
            "Authorization": creds['github_token'],
            "X-GitHub-Api-Version": "2022-11-28"
        }
        self.url = url
        self.params = params
        pass

    def request_get(self):
        """make https get request"""
        return requests.get(self.url, headers=self.header, params=self.params)
    
    def response_json(self):
        """retrieve the json data of the get request"""
        return self.request_get().json()
    
    def received_events_url(self):
        """get value from key received_events_url"""
        return self.response_json()['received_events_url']
    
    def get_received_events(self):
        """make https get request in value got from key received_events_url"""
        return requests.get(self.received_events_url(), headers=self.header, params=self.params)
    
    def get_received_events_json(self):
        """retrieve the json data of received_events_url request"""
        return self.get_received_events().json()
