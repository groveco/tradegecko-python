import os
import json

from endpoints import Company, Address, Variant, Product, Order

from helper import send_request, generate_data


def find_credentials():
    try:
        app_id = os.environ["TRADEGECKO_APP_ID"]
        app_secret = os.environ["TRADEGECKO_APP_SECRET"]
        return app_id, app_secret
    except KeyError:
        return None, None


class TradeGeckoRestClient(object):

    def __init__(self, app_id=None, app_secret=None, access_token=None, refresh_token=None):
        self.app_id = app_id
        self.app_secret = app_secret
        self.refresh_token = refresh_token
        self.access_token = access_token
        # TODO setup env var
        self.base_uri = 'https://api.tradegecko.com/'
        self.redirect_uri = os.environ['TRADEGECKO_REDIRECT']
        self.base_data = {} # built in _setup_base_data

        if not app_id or app_secret:
            self.app_id, self.app_secret = find_credentials()

        self._test_credentials()
        self._setup_base_data()

        # Endpoints
        self.company = Company(self.base_data, self.access_token)
        self.address = Address(self.base_data, self.access_token)
        self.variant = Variant(self.base_data, self.access_token)
        self.product = Product(self.base_data, self.access_token)
        self.order = Order(self.base_data, self.access_token)

    def _test_credentials(self):
        if not self.app_id or not self.app_secret or not self.access_token:
            #TODO create specific exception
            #TODO refactor
            raise Exception("Auth Error")

    def _setup_base_data(self):
        self.base_data = {
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'redirect_uri': self.redirect_uri
        }

    def generate_data(self, data):
        #merge dictionary and return json
        return json.dumps(dict(self.base_data.items() + data.items()))

    def get_refresh_token(self):
        if not self.refresh_token:
            raise Exception("Missing refresh token")

        uri = self.base_uri + 'oauth/token'
        data = {
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token'
        }
        data = generate_data(self.base_data, data)

        rsp = send_request('POST', uri, data)

        if rsp.status_code == 200:
            rsp_data = rsp.json()
            return rsp_data['access_token'], rsp_data['refresh_token']
        else:
            return False, False
