# tango_client.2AccountsApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](2AccountsApi.md#get_account) | **GET** /accounts/{identifier} | Get details for a specific Account on this Platform.
[**list_customer_accounts**](2AccountsApi.md#list_customer_accounts) | **GET** /accounts | Get a list of Accounts created on this Platform.


# **get_account**
> AccountView get_account(identifier)

Get details for a specific Account on this Platform.

### Example
```python
from __future__ import print_function
import time
import tango_client
from tango_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = tango_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = tango_client.2AccountsApi(tango_client.ApiClient(configuration))
identifier = 'identifier_example' # str | identifier

try:
    # Get details for a specific Account on this Platform.
    api_response = api_instance.get_account(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 2AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| identifier | 

### Return type

[**AccountView**](AccountView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_accounts**
> list[AccountView] list_customer_accounts()

Get a list of Accounts created on this Platform.

### Example
```python
from __future__ import print_function
import time
import tango_client
from tango_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = tango_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = tango_client.2AccountsApi(tango_client.ApiClient(configuration))

try:
    # Get a list of Accounts created on this Platform.
    api_response = api_instance.list_customer_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 2AccountsApi->list_customer_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AccountView]**](AccountView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

