import os
import json

from endpoints import Company, Address, Variant, Product, Order

import logging
logger = logging.getLogger(__name__)


def find_credentials():
    try:
        app_id = os.environ["TRADEGECKO_APP_ID"]
        app_secret = os.environ["TRADEGECKO_APP_SECRET"]
        access_token = os.environ["TRADEGECKO_ACCESS_TOKEN"]
        return app_id, app_secret, access_token
    except KeyError:
        return None, None, None


class TradeGeckoRestClient(object):

    def __init__(self, app_id=None, app_secret=None, access_token=None):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token
        self.base_uri = os.environ.get("TRADEGECKO_API_URI", 'https://api.tradegecko.com/')

        if not (app_id and app_secret and access_token):
            self.app_id, self.app_secret, self.access_token = find_credentials()

        if not (app_id and app_secret and access_token):
            raise Exception("Could not find env vars TRADEGECKO_APP_ID, TRADEGECKO_APP_SECRET, and TRADEGECKO_ACCESS_TOKEN")

        # Endpoints
        self.company = Company(self.base_uri, self.access_token)
        self.address = Address(self.base_uri, self.access_token)
        self.variant = Variant(self.base_uri, self.access_token)
        self.product = Product(self.base_uri, self.access_token)
        self.order = Order(self.base_uri, self.access_token)