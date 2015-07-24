import logging
import requests
import json
import math

logger = logging.getLogger(__name__)


class TGRequestFailure(Exception):
    pass


class TGAuthFailure(TGRequestFailure):
    pass


class TGUnprocessableEntityFailure(TGRequestFailure):
    pass


class TGRateLimitFailure(TGRequestFailure):
    pass


class ApiEndpoint(object):

    def __init__(self, base_uri, access_token):
        self.access_token = access_token
        self.header = {
            'Authorization': 'Bearer ' + self.access_token,
            'content-type': 'application/json'
        }
        self.rsp = None
        self.json = None
        self.base_uri = base_uri
        self.uri = ''
        self.required_fields = []
        self._data_name = ''

    def _send_request(self, method, uri, data=None, params=None):
        self.rsp = requests.request(method, uri, data=data, headers=self.header, params=params)
        logger.info('TRADEGECKO API REQUEST: %s %s \nDATA="%s" \nPARAMS="%s" \nRESPONSE="%s" \nSTATUS_CODE: %s' % (method, uri, data, params, self.rsp.content, self.rsp.status_code))
        if self.rsp.status_code == 401:
            raise TGAuthFailure
        if self.rsp.status_code == 422:
            raise TGUnprocessableEntityFailure(self.rsp.content)
        if self.rsp.status_code == 429:
            raise TGRateLimitFailure
        return self.rsp.status_code

    def _build_data(self, data):
        return json.dumps({self._data_name: data})

    # all records
    def all(self, page=1):
        uri = self.uri % ''
        params = {'page': page}
        if self._send_request('GET', uri, params=params) == 200:
            return self.rsp.json()
        else:
            return False

    # retrieve a specific record
    def get(self, pk):
        uri = self.uri % str(pk)
        if self._send_request('GET', uri) == 200:
            return self.rsp.json()
        else:
            return False

    # records filtered by field value
    def filter(self, **kwargs):
        uri = self.uri % ''
        if self._send_request('GET', uri, params=kwargs) == 200:
            return self.rsp.json()
        else:
            return False

    # delete a specific record
    def delete(self, pk):
        uri = self.uri % str(pk)
        if self._send_request('DELETE', uri) == 204:
            return self.rsp
        else:
            return False

    # create a new record
    def create(self, data):
        uri = self.uri % ''
        data = self._build_data(data)

        if self._send_request('POST', uri, data=data) == 201:
            return self.rsp.json()[self._data_name]['id']
        else:
            raise TGRequestFailure("Creation Failed")

    # update a specific record
    def update(self, pk, data):
        uri = self.uri % str(pk)
        data = self._build_data(data)

        if self._send_request('PUT', uri, data=data) == 204:
            return True
        else:
            raise TGRequestFailure("Update Failed")

    def page_count(self, limit=100):
        tg_items = self.filter(page='1', limit='1')
        return int(math.ceil(tg_items['meta']['total'] / float(limit)))

