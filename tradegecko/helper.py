import requests
import json


def generate_data(base, new):
        #merge dictionary and return json
        return json.dumps(dict(base.items() + new.items()))


def send_request(self, method, uri, data):
    data = self.generate_data(data)
    headers = {'content-type': 'application/json'}
    return requests.request(method, uri, data=data, headers=headers)