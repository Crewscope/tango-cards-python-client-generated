# tango_client.OrdersApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](OrdersApi.md#create_order) | **POST** /orders | Create an Order under a specific Account.
[**get_order**](OrdersApi.md#get_order) | **GET** /orders/{referenceOrderID} | Get details for a specific Order.
[**get_order_resends**](OrdersApi.md#get_order_resends) | **POST** /orders/{referenceOrderID}/resends | Resend a specific Order.
[**list_orders**](OrdersApi.md#list_orders) | **GET** /orders | Get a list of Orders placed under this Platform.


# **create_order**
> OrderViewSummary create_order(create_order_criteria=create_order_criteria)

Create an Order under a specific Account.

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
api_instance = tango_client.OrdersApi(tango_client.ApiClient(configuration))
create_order_criteria = tango_client.CreateOrderCriteria() # CreateOrderCriteria | <strong>accountIdentifier</strong> - specify the account this order will be deducted from<br/><br/><strong>amount</strong> - specify the face value of of the reward. Always required, including for fixed value items.<br/><br/><strong>campaign</strong> - optional campaign that may be used to administratively categorize a specific order.<br/><br/><strong>customerIdentifier</strong> - specify the customer associated with the order. Must be the customer the accountIdentifier is associated with.<br/><br/><strong>emailSubject</strong> - Optional. If not specified, a default email subject will be used for the specified reward.<br/><br/><strong>externalRefID</strong> - Optional. Idempotenent field that can be used for client-side order cross reference and prevent accidental order duplication. Will be returned in order response, order details, and order history.<br/><br/><strong>message</strong> - optional gift message<br/><br/><strong>recipient - email</strong> - required if sendEmail is true<br/><br/><strong>recipient - firstName</strong> - required if sendEmail is true (100 character max)<br/><br/><strong>recipient - lastName</strong> - always optional (100 character max)<br/><br/><strong>sendEmail</strong> - should Tango Card send the email to the recipient?<br/><br/><strong>sender - firstName</strong> - always optional (100 character max)<br/><br/><strong>sender - lastName</strong> - always optional (100 character max)<br/><br/><strong>sender - email</strong> - always optional<br/><br/><strong>utid</strong> - the unique identifier for the reward you are sending as provided in the Get Catalog call<br/><br/><strong>etid</strong> - Optional. The unique identifier for the email template you would like to use. Only applicable if sendEmail is true.<br/><br/><strong>notes</strong> - Optional order notes (up to 150 characters) (optional)

try:
    # Create an Order under a specific Account.
    api_response = api_instance.create_order(create_order_criteria=create_order_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_criteria** | [**CreateOrderCriteria**](CreateOrderCriteria.md)| &lt;strong&gt;accountIdentifier&lt;/strong&gt; - specify the account this order will be deducted from&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;amount&lt;/strong&gt; - specify the face value of of the reward. Always required, including for fixed value items.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;campaign&lt;/strong&gt; - optional campaign that may be used to administratively categorize a specific order.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;customerIdentifier&lt;/strong&gt; - specify the customer associated with the order. Must be the customer the accountIdentifier is associated with.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;emailSubject&lt;/strong&gt; - Optional. If not specified, a default email subject will be used for the specified reward.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;externalRefID&lt;/strong&gt; - Optional. Idempotenent field that can be used for client-side order cross reference and prevent accidental order duplication. Will be returned in order response, order details, and order history.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;message&lt;/strong&gt; - optional gift message&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;recipient - email&lt;/strong&gt; - required if sendEmail is true&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;recipient - firstName&lt;/strong&gt; - required if sendEmail is true (100 character max)&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;recipient - lastName&lt;/strong&gt; - always optional (100 character max)&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;sendEmail&lt;/strong&gt; - should Tango Card send the email to the recipient?&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;sender - firstName&lt;/strong&gt; - always optional (100 character max)&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;sender - lastName&lt;/strong&gt; - always optional (100 character max)&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;sender - email&lt;/strong&gt; - always optional&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;utid&lt;/strong&gt; - the unique identifier for the reward you are sending as provided in the Get Catalog call&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;etid&lt;/strong&gt; - Optional. The unique identifier for the email template you would like to use. Only applicable if sendEmail is true.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;notes&lt;/strong&gt; - Optional order notes (up to 150 characters) | [optional] 

### Return type

[**OrderViewSummary**](OrderViewSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrderViewVerbose get_order(reference_order_id)

Get details for a specific Order.

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
api_instance = tango_client.OrdersApi(tango_client.ApiClient(configuration))
reference_order_id = 'reference_order_id_example' # str | Reference order ID is returned in the order response payload

try:
    # Get details for a specific Order.
    api_response = api_instance.get_order(reference_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_order_id** | **str**| Reference order ID is returned in the order response payload | 

### Return type

[**OrderViewVerbose**](OrderViewVerbose.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_resends**
> ResendView get_order_resends(reference_order_id, order_resend_criteria=order_resend_criteria)

Resend a specific Order.

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
api_instance = tango_client.OrdersApi(tango_client.ApiClient(configuration))
reference_order_id = 'reference_order_id_example' # str | Reference order ID is returned in the order response payload
order_resend_criteria = tango_client.OrderResendRequestCriteria() # OrderResendRequestCriteria | <strong>newEmail</strong> - A new email to resend this order to. (optional)

try:
    # Resend a specific Order.
    api_response = api_instance.get_order_resends(reference_order_id, order_resend_criteria=order_resend_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_resends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_order_id** | **str**| Reference order ID is returned in the order response payload | 
 **order_resend_criteria** | [**OrderResendRequestCriteria**](OrderResendRequestCriteria.md)| &lt;strong&gt;newEmail&lt;/strong&gt; - A new email to resend this order to. | [optional] 

### Return type

[**ResendView**](ResendView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> OrderListView list_orders(account_identifier=account_identifier, customer_identifier=customer_identifier, external_ref_id=external_ref_id, start_date=start_date, end_date=end_date, elements_per_block=elements_per_block, page=page)

Get a list of Orders placed under this Platform.

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
api_instance = tango_client.OrdersApi(tango_client.ApiClient(configuration))
account_identifier = 'account_identifier_example' # str | specify the account to be queried. (optional)
customer_identifier = 'customer_identifier_example' # str | specify the customer to be queried (optional)
external_ref_id = 'external_ref_id_example' # str | specify the external reference ID to be queried (optional)
start_date = 'start_date_example' # str | specify the starting date or date time to be queried according to RFC 3339, i.e. \"2016-01-01\" or \"2016-01-01T00:00:00Z\". See https://www.ietf.org/rfc/rfc3339.txt  (optional)
end_date = 'end_date_example' # str | specify the ending date or date time to be queried according to RFC 3339, i.e. \"2016-01-01\" or \"2016-01-01T00:00:00Z\". See https://www.ietf.org/rfc/rfc3339.txt  (optional)
elements_per_block = 56 # int | specify the number of elements in a block. (optional)
page = 56 # int | specify the page number to return. (optional)

try:
    # Get a list of Orders placed under this Platform.
    api_response = api_instance.list_orders(account_identifier=account_identifier, customer_identifier=customer_identifier, external_ref_id=external_ref_id, start_date=start_date, end_date=end_date, elements_per_block=elements_per_block, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_identifier** | **str**| specify the account to be queried. | [optional] 
 **customer_identifier** | **str**| specify the customer to be queried | [optional] 
 **external_ref_id** | **str**| specify the external reference ID to be queried | [optional] 
 **start_date** | **str**| specify the starting date or date time to be queried according to RFC 3339, i.e. \&quot;2016-01-01\&quot; or \&quot;2016-01-01T00:00:00Z\&quot;. See https://www.ietf.org/rfc/rfc3339.txt  | [optional] 
 **end_date** | **str**| specify the ending date or date time to be queried according to RFC 3339, i.e. \&quot;2016-01-01\&quot; or \&quot;2016-01-01T00:00:00Z\&quot;. See https://www.ietf.org/rfc/rfc3339.txt  | [optional] 
 **elements_per_block** | **int**| specify the number of elements in a block. | [optional] 
 **page** | **int**| specify the page number to return. | [optional] 

### Return type

[**OrderListView**](OrderListView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

