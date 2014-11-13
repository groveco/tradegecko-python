import os
import json

from endpoints import Company, Address, Variant, Product, Order

from helper import send_request, generate_data
import logging
logger = logging.getLogger(__name__)


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

    def _get_tokens(self, grant_type, auth_type, auth):
        """
        For code-based auth (a way of getting an initial set of token + refresh) use:
            grant_type="authorization_code"
            auth_type="code"
            auth=<your authorization code>
        You can get an auth code for your app from https://go.tradegecko.com/oauth/applications

        For getting a new token via a refresh token, use:
            grant_type="refresh_token"
            auth_type="refresh_token"
            auth=self.refresh_token
        """
        if not grant_type or not auth or not auth_type:
            raise Exception("Missing authenticatino parameters. See _get_tokens docstring for more info.")

        uri = self.base_uri + 'oauth/token'
        data = {
            auth_type: auth,
            'grant_type': grant_type
        }
        data = generate_data(self.base_data, data)

        rsp = send_request('POST', uri, data)

        if rsp.status_code == 200:
            logger.info('TRADEGECKO AUTH REQUEST: POST %s \nDATA="%s" \nRESPONSE="%s" \nSTATUS_CODE: %s' % (uri, data, rsp.content, rsp.status_code))
            rsp_data = rsp.json()
            return rsp_data['access_token'], rsp_data['refresh_token']
        else:
            logger.info('TRADEGECKO AUTH REQUEST: POST %s \nDATA="%s" \nRESPONSE="%s" \nSTATUS_CODE: %s' % (uri, data, rsp.content, rsp.status_code))
            return False, False

    def get_refresh_token(self):
        return self._get_tokens('refresh_token', 'refresh_token', self.refresh_token)

    def get_refresh_token_from_auth_code(self, code):
        return self._get_tokens('authorization_code', 'code', code)