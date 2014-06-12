from api import ApiEndpoint


class Company(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Company, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'companies/'
        self.required_fields = ['name', 'company_type']
        self._data_name = 'company'


class Address(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Address, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'addresses/'
        self.required_fields = ['company_id', 'label']
        self._data_name = 'address'


class PurchaseOrder(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(PurchaseOrder, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'purchase_orders/'
        self.required_fields = ['company_id']
        self._data_name = 'purchase_orders'


class Variant(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Variant, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'variants/'
        self.required_fields = []
        self._data_name = 'variants'