from api import ApiEndpoint


class Company(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Company, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'companies/'
        self.required_fields = ['name', 'company_type']
        # TODO populate with available fields for validation
        self.data_name = 'company'
        self.fields = []


class Address(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Address, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'addresses/'
        self.required_fields = ['company_id', 'label']
        self.data_name = 'address'
        # TODO populate with available fields for validation
        self.fields = []


class PurchaseOrder(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(PurchaseOrder, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'purchase_orders/'
        self.required_fields = ['company_id']
        self.data_name = 'purchase_orders'
        # TODO populate with available fields for validation
        self.fields = []