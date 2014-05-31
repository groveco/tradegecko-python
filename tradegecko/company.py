from helper import ApiEndpoint


class Company(ApiEndpoint):
    def __init__(self, base_data, access_token):
        super(Company, self).__init__(base_data, access_token)
        self.uri = self.base_uri + 'companies/'
