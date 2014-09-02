.. image:: https://travis-ci.org/epantry/tradegecko-python.png?branch=master


Python wrapper for TradeGecko API.
==================================

**Install**

``pip install tradegecko-python``


**How to use**

Initialize client

``tg = TradeGeckoRestClient(access_token, refresh_token)``

Create company

``tg.company.create(**company_data)``

Update company

``tg.company.create(company_id, **company_data)``
