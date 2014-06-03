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
        self.json = None
        self.base_uri = 'https://api.tradegecko.com/'
        self.uri = None
        self.required_fields = []

    def _validate_post_data(self, data):
        for k in self.required_fields:
            if k not in data.keys():
                return False
        return True

    def _send_request(self, method, uri, data=None):
        self.rsp = requests.request(method, uri, data=data, headers=self.header)
        return self.rsp.status_code

    # all records
    def all(self):
        if self._send_request('GET', self.uri) == 200:
            return self.rsp.json()
        else:
            return False

    # retrieve a specific record
    def get(self, pk):
        uri = self.uri + str(pk)
        if self._send_request('GET', uri) == 200:
            return self.rsp.json()
        else:
            return False

    # delete a specific record
    def delete(self, pk):
        uri = self.uri + str(pk)
        if self._send_request('DELETE', uri) == 204:
            return self.rsp
        else:
            return False

    # create a new record
    def post(self, data):
        data = json.dumps(data)
        if self._send_request('POST', self.uri, data=data) == 201:
            return self.rsp.json()
        else:
            return False

    # update a specific record
    def update(self, pk, data):
        uri = self.uri + str(pk)
        data = json.dumps(data)
        if self._send_request('PUT', uri, data=data) == 204:
            return self.rsp
        else:
            return False