import json

from nose.tools import assert_true, assert_false, assert_equal
from mock import patch, Mock

from tradegecko.api import ApiEndpoint


access_token = 'access_token'
base_data = {
    'client_id': 'app_id',
    'client_secret': 'app_secret',
    'redirect_uri': 'redirect_uri'
}

api = ApiEndpoint(base_data, access_token)
api.rsp = Mock()


def test_validate_post_data_correct_fields():
    api.required_fields = ['field1', 'field2']
    data = {'field1': 'foo', 'field2': 'bar'}

    assert_true(api._validate_post_data(data))


def test_validate_post_data_incorrect_fields():
    api.required_fields = ['field1', 'field3']
    data = {'field1': 'foo', 'field2': 'bar'}

    assert_false(api._validate_post_data(data))


def test_build_data_returns_json():
    api._data_name = 'test'
    data = {
        'foo': 'bar',
        'bar': {
            'foo': 'bar'
        }}

    test_data = {'test': data}
    actual_json = json.dumps(test_data)
    test_json = api._build_data(data)

    assert_equal(actual_json, test_json)

@patch('requests.request')
def test_send_request_(mock):
    rsp = Mock()
    rsp.status_code = 200
    mock.return_value = rsp
    function_return = api._send_request('GET', 'uri')

    assert_equal(function_return, 200) # returns status code
    assert_true(mock.called) # request is called

# All
@patch.object(ApiEndpoint, '_send_request')
def test_all_request_success(mock):
    mock.return_value = 200
    api.rsp.json.return_value = {'foo': 'bar'}
    function_return = api.all()

    assert_equal(function_return, {'foo': 'bar'}) # dict on request success


@patch.object(ApiEndpoint, '_send_request')
def test_all_request_failure(mock):
    mock.return_value = 400
    function_return = api.all()

    assert_equal(function_return, False) # False on request failure

# Retrieve
@patch.object(ApiEndpoint, '_send_request')
def test_get_request_success(mock):
    mock.return_value = 200
    api.rsp.json.return_value = {'foo': 'bar'}
    function_return = api.get(123)

    assert_equal(function_return, {'foo': 'bar'}) # dict on request success


@patch.object(ApiEndpoint, '_send_request')
def test_get_request_failure(mock):
    mock.return_value = 400
    function_return = api.get(123)

    assert_equal(function_return, False) # False on request failure

# Delete
@patch.object(ApiEndpoint, '_send_request')
def test_delete_request_success(mock):
    mock.return_value = 204
    function_return = api.delete(123)

    assert_true(function_return) # Request response on success


@patch.object(ApiEndpoint, '_send_request')
def test_delete_request_failure(mock):
    mock.return_value = 400
    function_return = api.delete(123)

    assert_equal(function_return, False) # False on request failure

# create
@patch.object(ApiEndpoint, '_send_request')
@patch.object(ApiEndpoint, '_build_data')
def test_create_request_success(mock_data, mock_request):
    data = {'foo': 'bar'}
    json_data = json.dumps(data)
    mock_request.return_value = 201
    mock_data.return_value = json_data
    function_return = api.create(data)

    assert_equal(function_return, data) # Dict on success


@patch.object(ApiEndpoint, '_send_request')
@patch.object(ApiEndpoint, '_build_data')
def test_create_request_success(mock_data, mock_request):
    data = {'foo': 'bar'}
    json_data = json.dumps(data)
    mock_request.return_value = 400
    mock_data.return_value = json_data
    function_return = api.create(data)

    assert_false(function_return) # False on failure

# update
@patch.object(ApiEndpoint, '_send_request')
@patch.object(ApiEndpoint, '_build_data')
def test_update_request_success(mock_data, mock_request):
    data = {'foo': 'bar'}
    json_data = json.dumps(data)
    mock_request.return_value = 204
    mock_data.return_value = json_data
    function_return = api.update(1234, data)

    assert_equal(function_return, data) # Dict on success


@patch.object(ApiEndpoint, '_send_request')
@patch.object(ApiEndpoint, '_build_data')
def test_update_request_success(mock_data, mock_request):
    data = {'foo': 'bar'}
    json_data = json.dumps(data)
    mock_request.return_value = 400
    mock_data.return_value = json_data
    function_return = api.update(1234, data)

    assert_false(function_return) # False on failure
