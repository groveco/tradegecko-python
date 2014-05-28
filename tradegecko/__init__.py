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
    def __init__(self, app_id=None, app_secret=None):
        if not app_id or app_secret:
            self.app_id, self.app_secret = find_credentials()
        else:
            self.app_id = app_id
            self.app_secret = app_secret

        if not self.app_id or not self.app_secret:
            #TODO create specific exception
            #TODO refactor
            raise Exception("Auth Error")

        self.base_uri = 'https://api.tradegecko.com/'
        ##TODO env var
        self.redirect_uri = 'http://www.epantry.com'

        self.base_data = {
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'redirect_uri': self.redirect_uri
        }


    def generate_data(self, data):
        #merge dictionary and return json 
        return json.dumps(dict(self.base_data.items() + data.items()))

    def refresh_token(self):
        uri = self.base_uri + 'oauth/token'
        header = {'content-type': 'application/json'}
        data = {
            'refresh_token': os.environ['TRADEGECKO_REFRESH'],
            'grant_type': 'refresh_token'
        }
        data = self.generate_data(data)

        rsp = requests.post(uri, headers=header, data=data)
        
        if rsp.status_code == 200:
            rsp_data = rsp.json()
            os.environ['TRADEGECKO_ACCESS'] = rsp_data['access_token']
            os.environ['TRADEGECKO_REFRESH'] = rsp_data['refresh_token']
            return True
        else:
            return False



