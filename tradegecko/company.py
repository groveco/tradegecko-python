from helper import ApiEndpoint


class Company(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Company, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'companies/'
        self.required_fields = ['name', 'company_type']

    def post(self, data):
        if self._validate_post_data(data):
            return super(Company, self).__init__(data)
        return False

