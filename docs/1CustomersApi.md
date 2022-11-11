# tango_client.1CustomersApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](1CustomersApi.md#create_customer) | **POST** /customers | Create a new Customer on this Platform.
[**create_customer_account**](1CustomersApi.md#create_customer_account) | **POST** /customers/{customerIdentifier}/accounts | Create an Account under a specific Customer on this Platform.
[**get_customer**](1CustomersApi.md#get_customer) | **GET** /customers/{customerIdentifier} | Get details for a specific Customer on this Platform.
[**list_customer_accounts1**](1CustomersApi.md#list_customer_accounts1) | **GET** /customers/{customerIdentifier}/accounts | Get a list of all Accounts created for a specific Customer on this Platform.
[**list_customers**](1CustomersApi.md#list_customers) | **GET** /customers | Get a list of all Customers on this Platform.


# **create_customer**
> CustomerViewNew create_customer(form=form)

Create a new Customer on this Platform.

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
api_instance = tango_client.1CustomersApi(tango_client.ApiClient(configuration))
form = tango_client.CreateCustomerCriteria() # CreateCustomerCriteria | <strong>displayName</strong> - a friendly name for this customer <br /><br /><strong>customerIdentifier</strong> - an official identifier for this customer. This identifier needs to be lowercase if alphabetic characters are used. (optional)

try:
    # Create a new Customer on this Platform.
    api_response = api_instance.create_customer(form=form)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 1CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form** | [**CreateCustomerCriteria**](CreateCustomerCriteria.md)| &lt;strong&gt;displayName&lt;/strong&gt; - a friendly name for this customer &lt;br /&gt;&lt;br /&gt;&lt;strong&gt;customerIdentifier&lt;/strong&gt; - an official identifier for this customer. This identifier needs to be lowercase if alphabetic characters are used. | [optional] 

### Return type

[**CustomerViewNew**](CustomerViewNew.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_account**
> AccountView create_customer_account(customer_identifier, account_criteria=account_criteria)

Create an Account under a specific Customer on this Platform.

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
api_instance = tango_client.1CustomersApi(tango_client.ApiClient(configuration))
customer_identifier = 'customer_identifier_example' # str | The customerIdentifier for the Customer under which you are creating a new account
account_criteria = tango_client.CreateAccountCriteria() # CreateAccountCriteria | <strong>contactEmail</strong> - An email address for a designated representative for this account.<br /><br /><strong>displayName</strong> - A friendly name for this account<br /><br /><strong>identifier</strong> - A unique identifier for this account. This identifier must be lowercase if alphabetic characters are used. (optional)

try:
    # Create an Account under a specific Customer on this Platform.
    api_response = api_instance.create_customer_account(customer_identifier, account_criteria=account_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 1CustomersApi->create_customer_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_identifier** | **str**| The customerIdentifier for the Customer under which you are creating a new account | 
 **account_criteria** | [**CreateAccountCriteria**](CreateAccountCriteria.md)| &lt;strong&gt;contactEmail&lt;/strong&gt; - An email address for a designated representative for this account.&lt;br /&gt;&lt;br /&gt;&lt;strong&gt;displayName&lt;/strong&gt; - A friendly name for this account&lt;br /&gt;&lt;br /&gt;&lt;strong&gt;identifier&lt;/strong&gt; - A unique identifier for this account. This identifier must be lowercase if alphabetic characters are used. | [optional] 

### Return type

[**AccountView**](AccountView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> CustomerViewSummary get_customer(customer_identifier)

Get details for a specific Customer on this Platform.

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
api_instance = tango_client.1CustomersApi(tango_client.ApiClient(configuration))
customer_identifier = 'customer_identifier_example' # str | customerIdentifier

try:
    # Get details for a specific Customer on this Platform.
    api_response = api_instance.get_customer(customer_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 1CustomersApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_identifier** | **str**| customerIdentifier | 

### Return type

[**CustomerViewSummary**](CustomerViewSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_accounts1**
> list[AccountViewSummary] list_customer_accounts1(customer_identifier)

Get a list of all Accounts created for a specific Customer on this Platform.

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
api_instance = tango_client.1CustomersApi(tango_client.ApiClient(configuration))
customer_identifier = 'customer_identifier_example' # str | customerIdentifier

try:
    # Get a list of all Accounts created for a specific Customer on this Platform.
    api_response = api_instance.list_customer_accounts1(customer_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 1CustomersApi->list_customer_accounts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_identifier** | **str**| customerIdentifier | 

### Return type

[**list[AccountViewSummary]**](AccountViewSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> list[CustomerViewSummary] list_customers()

Get a list of all Customers on this Platform.

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
api_instance = tango_client.1CustomersApi(tango_client.ApiClient(configuration))

try:
    # Get a list of all Customers on this Platform.
    api_response = api_instance.list_customers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling 1CustomersApi->list_customers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomerViewSummary]**](CustomerViewSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

