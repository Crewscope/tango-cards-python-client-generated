# tango_client.4CatalogsApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog**](4CatalogsApi.md#get_catalog) | **GET** /catalogs | Get all items in the Platform&#39;s Catalog.


# **get_catalog**
> CatalogViewVerbose get_catalog(brand_key=brand_key, brand_name=brand_name, utid=utid, reward_name=reward_name, status=status, currency_code=currency_code, country=country, verbose=verbose)

Get all items in the Platform's Catalog.

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
api_instance = tango_client.4CatalogsApi(tango_client.ApiClient(configuration))
brand_key = 'brand_key_example' # str | brandKey (optional)
brand_name = 'brand_name_example' # str | brandName (optional)
utid = 'utid_example' # str | utid (optional)
reward_name = 'reward_name_example' # str | rewardName (optional)
status = 'status_example' # str | status (optional)
currency_code = 'currency_code_example' # str | currencyCode (optional)
country = 'country_example' # str | country (optional)
verbose = true # bool | Verbose payload (optional) (default to true)

try:
    # Get all items in the Platform's Catalog.
    api_response = api_instance.get_catalog(brand_key=brand_key, brand_name=brand_name, utid=utid, reward_name=reward_name, status=status, currency_code=currency_code, country=country, verbose=verbose)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 4CatalogsApi->get_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_key** | **str**| brandKey | [optional] 
 **brand_name** | **str**| brandName | [optional] 
 **utid** | **str**| utid | [optional] 
 **reward_name** | **str**| rewardName | [optional] 
 **status** | **str**| status | [optional] 
 **currency_code** | **str**| currencyCode | [optional] 
 **country** | **str**| country | [optional] 
 **verbose** | **bool**| Verbose payload | [optional] [default to true]

### Return type

[**CatalogViewVerbose**](CatalogViewVerbose.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

