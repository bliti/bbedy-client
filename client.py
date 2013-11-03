import requests, json
from settings import *


class Client(object):
    
    
    def __init__(self):
        self.api_url = API_URL
    

    #make a GET request
    def _get(self, uri):
        """returns txt body of response"""
        return requests.get('{0}{1}'.format(self.api_url, uri)).text
    

    #make a POST request
    def _post(self, uri, payload):
        """payload=dict() of params. returns text body of response"""
        return requests.post(
        '{0}{1}'.format(self.api_url, uri),payload).text


    def send(self, body, receiver):
        data = {}
        data['body'] = body
        data['receiver'] = receiver
        data['user_token'] = USER_TOKEN
        data['access_token'] = ACCESS_TOKEN
        return self._post('send/', data)
        
    
    def messages(self):
        data = {}
        data['user_token'] = USER_TOKEN
        data['access_token'] = ACCESS_TOKEN
        return self._post('messages/', data)
        