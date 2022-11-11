# tango_client.7ExchangeRatesApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rates**](7ExchangeRatesApi.md#get_exchange_rates) | **GET** /exchangerates | Get a list of exchange rates.


# **get_exchange_rates**
> ExchangeRatesWithDisclaimer get_exchange_rates()

Get a list of exchange rates.

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
api_instance = tango_client.7ExchangeRatesApi(tango_client.ApiClient(configuration))

try:
    # Get a list of exchange rates.
    api_response = api_instance.get_exchange_rates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 7ExchangeRatesApi->get_exchange_rates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangeRatesWithDisclaimer**](ExchangeRatesWithDisclaimer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

