from helper import send_request


class Company(object):
    def __init__(self):
        self.uri = 'companies/'

    def get(self):
        return send_request('GET', self.uri)


