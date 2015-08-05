from api import ApiEndpoint


class Composition(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(Composition, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'variants/%s/composition'
        self._data_name = 'variants'


class Company(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(Company, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'companies/%s'
        self.required_fields = ['name', 'company_type']
        self._data_name = 'company'


class Address(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(Address, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'addresses/%s'
        self.required_fields = ['company_id', 'label']
        self._data_name = 'address'


class PurchaseOrder(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(PurchaseOrder, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'purchase_orders/%s'
        self.required_fields = ['company_id']
        self._data_name = 'purchase_orders'


class Variant(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(Variant, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'variants/%s'
        self._data_name = 'variants'


class Product(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(Product, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'products/%s'
        self._data_name = 'products'


class Order(ApiEndpoint):
    def __init__(self, base_uri, access_token):
        super(Order, self).__init__(base_uri, access_token)
        self.uri = self.base_uri + 'orders/%s'
        self._data_name = 'order'
