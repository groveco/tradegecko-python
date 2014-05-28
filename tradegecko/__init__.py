import logging
import os
import requests
import json

def find_credentials():
    try:
        app_id = os.environ["TRADEGECKO_APP_ID"]
        app_secret = os.environ["TRADEGECKO_APP_SECRET"]
        return app_id, app_secret
    except KeyError:
        return None, None


class TradeGeckoRestClient(object):
    def __init__(self, app_id=None, app_secret=None, access_token=None, refresh_token=None):
        if not app_id or app_secret:
            self.app_id, self.app_secret = find_credentials()
        else:
            self.app_id = app_id
            self.app_secret = app_secret
            self.access_token = access_token
            self.refresh_token = refresh_token

        if not self.app_id or not self.app_secret or not self.access_token:
            #TODO create specific exception
            #TODO refactor
            raise Exception("Auth Error")

        self.base_uri = 'https://api.tradegecko.com/'
        ##TODO env var
        self.redirect_uri = os.environ['TRADEGECKO_REDIRECT']

        self.base_data = {
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'redirect_uri': self.redirect_uri
        }

    def generate_data(self, data):
        #merge dictionary and return json 
        return json.dumps(dict(self.base_data.items() + data.items()))

    def send_request(self, method, uri, data):
        data = self.generate_data(data)
        headers = {'content-type': 'application/json'}
        return requests.request(method, uri, data=data, headers=headers)

    def refresh_token(self):
        if not self.refresh_token:
            raise Exception("Missing refresh token")

        uri = self.base_uri + 'oauth/token'
        data = {
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token'
        }

        rsp = self.send_request('POST', uri, data)

        if rsp.status_code == 200:
            rsp_data = rsp.json()
            return rsp_data['access_token'], rsp_data['refresh_token']
        else:
            return False



