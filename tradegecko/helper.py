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
        for k in self.require_fields:
            if k not in data.keys():
                return False
        return True

    def _build_header(self, header):
        try:
            return dict(self.header.items() + header.items())
            # return self.header.update(header)
        except AttributeError:
            return self.header

    def _send_request(self, method, uri, data=None, header=None):
        headers = self._build_header(header)
        self.rsp = requests.request(method, uri, data=data, headers=headers)
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
            return self.rsp.json()
        else:
            return False

    # create a new record
    def post(self, data):
        if self._send_request('POST', self.uri, data=data) == 201:
            return self.rsp.json()
        else:
            return False

    # update a specific record
    def update(self, data):
        if self._send_request('PUT', self.uri, data=data) == 204:
            return self.rsp.json()
        else:
            return False