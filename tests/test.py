from tradegecko.api import ApiEndpoint
from nose.tools import assert_true, assert_false


access_token = 'access_token'
base_data = {
    'client_id': 'app_id',
    'client_secret': 'app_secret',
    'redirect_uri': 'redirect_uri'
}

api = ApiEndpoint(base_data, access_token)


def test_validate_post_data_correct_fields():
    api.required_fields = ['field1', 'field2']
    data = {'field1': 'foo', 'field2': 'bar'}

    assert_true(api._validate_post_data(data))


def test_validate_post_data_incorrect_fields():
    api.required_fields = ['field1', 'field3']
    data = {'field1': 'foo', 'field2': 'bar'}

    assert_false(api._validate_post_data(data))
