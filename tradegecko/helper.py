import requests
import json


def generate_data(base, new):
        #merge dictionary and return json
        return json.dumps(dict(base.items() + new.items()))


def send_request(method, uri, data):
    headers = {'content-type': 'application/json'}
    return requests.request(method, uri, data=data, headers=headers)


class ApiEndpoint(object):

    def __init__(self, base_data, access_token):
        self.base_data = base_data
        self.access_token = access_token
        self.header = {
            'Authorization': 'Bearer ' + self.access_token,
            'content-type': 'application/json'
        }
        self.rsp = None
        self.base_uri = 'https://api.tradegecko.com/'
        self.uri = None

    def _build_header(self, header):
        try:
            return dict(self.header.items() + header.items())
            # return self.header.update(header)
        except AttributeError:
            return self.header

    def send_request(self, method, uri, data=None, header=None):
        headers = self._build_header(header)
        self.rsp = requests.request(method, uri, data=data, headers=headers)
        return self.rsp.status_code

    def get(self):
        return self.send_request('GET', self.uri)