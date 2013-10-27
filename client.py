import requests, json, settings


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
        return requests.get(
        '{0}{1}'.format(self.api_url, uri),
        json.dumps(payload)
        ).text