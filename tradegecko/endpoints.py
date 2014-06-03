from api import ApiEndpoint


class Company(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Company, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'companies/'
        self.required_fields = ['name', 'company_type']
        # TODO populate with available fields for validation
        self.data_name = 'company'
        self.field = []


class Address(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Address, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'addresses/'
        self.required_fields = ['company_id', 'label']
        self.data_name = 'address'
        # TODO populate with available fields for validation
        self.field = []



