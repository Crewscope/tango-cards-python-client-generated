# tango_client.FundApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit_card**](FundApi.md#create_credit_card) | **POST** /creditCards | Register a new Credit Card.
[**create_credit_card_deposit**](FundApi.md#create_credit_card_deposit) | **POST** /creditCardDeposits | Fund an Account.
[**create_credit_card_unregister**](FundApi.md#create_credit_card_unregister) | **POST** /creditCardUnregisters | Unregister a Credit Card.
[**get_credit_card**](FundApi.md#get_credit_card) | **GET** /creditCards/{token} | Get details for a specific Credit Card.
[**get_credit_card_deposit**](FundApi.md#get_credit_card_deposit) | **GET** /creditCardDeposits/{depositId} | Get details for a specific Credit Card Deposit.
[**list_credit_cards**](FundApi.md#list_credit_cards) | **GET** /creditCards | List all credit cards registered on this Platform.


# **create_credit_card**
> CreditCardView create_credit_card(credit_card_criteria=credit_card_criteria)

Register a new Credit Card.

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
api_instance = tango_client.FundApi(tango_client.ApiClient(configuration))
credit_card_criteria = tango_client.CreateCreditCardCriteria() # CreateCreditCardCriteria | <strong>customerIdentifier</strong> - specify the customer associated with the credit card. Must be the customer the accountIdentifier is associated with.<br/><br/> <strong>accountIdentifier</strong> - specify the account this credit card is associated with<br/><br/> <strong>label</strong> - specify a label for the credit card<br/><br/> <strong>ipAddress</strong> - specify the The IP address of the person adding the credit card<br/><br/> <strong>creditCard - number</strong> - specify the account this order will be deducted from<br/><br/> <strong>creditCard - expiration</strong> - specify the card expiration date in YYYY-MM format<br/><br/> <strong>creditCard - verificationNumber</strong> - specify the 3 or 4-digit card security code on back of card (CVV2, CVC2, or CID)<br/><br/> <strong>billingAddress - firstName</strong> - specify the billing address first name<br/><br/> <strong>billingAddress - lastName</strong> - specify the billing address last name<br/><br/> <strong>billingAddress - addressLine1</strong> - specify the billing address line 1<br/><br/> <strong>billingAddress - addressLine2</strong> - Optional. Specify the billing address line 2<br/><br/> <strong>billingAddress - city</strong> - specify the billing address city<br/><br/> <strong>billingAddress - state</strong> - specify the billing address state<br/><br/> <strong>billingAddress - postalCode</strong> - specify the billing address postal code<br/><br/> <strong>billingAddress - country</strong> - specify the billing address 2-letter country code<br/><br/> <strong>billingAddress - emailAddress</strong> - specify the billing address email<br/><br/> <strong>contactInformation - fullName</strong> - Optional. Used for email receipts. Specify the contact full name.<br/><br/> <strong>contactInformation - emailAddress</strong> - Optional. Used for email receipts. Specify the contact email address.<br/><br/>  (optional)

try:
    # Register a new Credit Card.
    api_response = api_instance.create_credit_card(credit_card_criteria=credit_card_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundApi->create_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_criteria** | [**CreateCreditCardCriteria**](CreateCreditCardCriteria.md)| &lt;strong&gt;customerIdentifier&lt;/strong&gt; - specify the customer associated with the credit card. Must be the customer the accountIdentifier is associated with.&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;accountIdentifier&lt;/strong&gt; - specify the account this credit card is associated with&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;label&lt;/strong&gt; - specify a label for the credit card&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;ipAddress&lt;/strong&gt; - specify the The IP address of the person adding the credit card&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;creditCard - number&lt;/strong&gt; - specify the account this order will be deducted from&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;creditCard - expiration&lt;/strong&gt; - specify the card expiration date in YYYY-MM format&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;creditCard - verificationNumber&lt;/strong&gt; - specify the 3 or 4-digit card security code on back of card (CVV2, CVC2, or CID)&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - firstName&lt;/strong&gt; - specify the billing address first name&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - lastName&lt;/strong&gt; - specify the billing address last name&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - addressLine1&lt;/strong&gt; - specify the billing address line 1&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - addressLine2&lt;/strong&gt; - Optional. Specify the billing address line 2&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - city&lt;/strong&gt; - specify the billing address city&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - state&lt;/strong&gt; - specify the billing address state&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - postalCode&lt;/strong&gt; - specify the billing address postal code&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - country&lt;/strong&gt; - specify the billing address 2-letter country code&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;billingAddress - emailAddress&lt;/strong&gt; - specify the billing address email&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;contactInformation - fullName&lt;/strong&gt; - Optional. Used for email receipts. Specify the contact full name.&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;contactInformation - emailAddress&lt;/strong&gt; - Optional. Used for email receipts. Specify the contact email address.&lt;br/&gt;&lt;br/&gt;  | [optional] 

### Return type

[**CreditCardView**](CreditCardView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_card_deposit**
> CreditCardDepositView create_credit_card_deposit(criteria=criteria)

Fund an Account.

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
api_instance = tango_client.FundApi(tango_client.ApiClient(configuration))
criteria = tango_client.CreateCreditCardDepositCriteria() # CreateCreditCardDepositCriteria | <strong>customerIdentifier</strong> - specify the customer associated with the credit card. Must be the customer the accountIdentifier is associated with.<br/><br/> <strong>accountIdentifier</strong> - specify the account this credit card is associated with<br/><br/> <strong>creditCardToken</strong> - specify the credit card token to fund with<br/><br/> <strong>amount</strong> - specify the amount to fund in USD<br/><br/>  (optional)

try:
    # Fund an Account.
    api_response = api_instance.create_credit_card_deposit(criteria=criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundApi->create_credit_card_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria** | [**CreateCreditCardDepositCriteria**](CreateCreditCardDepositCriteria.md)| &lt;strong&gt;customerIdentifier&lt;/strong&gt; - specify the customer associated with the credit card. Must be the customer the accountIdentifier is associated with.&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;accountIdentifier&lt;/strong&gt; - specify the account this credit card is associated with&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;creditCardToken&lt;/strong&gt; - specify the credit card token to fund with&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;amount&lt;/strong&gt; - specify the amount to fund in USD&lt;br/&gt;&lt;br/&gt;  | [optional] 

### Return type

[**CreditCardDepositView**](CreditCardDepositView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_card_unregister**
> CreditCardUnregisterView create_credit_card_unregister(criteria=criteria)

Unregister a Credit Card.

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
api_instance = tango_client.FundApi(tango_client.ApiClient(configuration))
criteria = tango_client.CreateCreditCardUnregisterCriteria() # CreateCreditCardUnregisterCriteria | <strong>customerIdentifier</strong> - specify the customer associated with the credit card. Must be the customer the accountIdentifier is associated with.<br/><br/> <strong>accountIdentifier</strong> - specify the account this credit card is associated with<br/><br/> <strong>creditCardToken</strong> - specify the credit card token to unregister<br/><br/>  (optional)

try:
    # Unregister a Credit Card.
    api_response = api_instance.create_credit_card_unregister(criteria=criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundApi->create_credit_card_unregister: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria** | [**CreateCreditCardUnregisterCriteria**](CreateCreditCardUnregisterCriteria.md)| &lt;strong&gt;customerIdentifier&lt;/strong&gt; - specify the customer associated with the credit card. Must be the customer the accountIdentifier is associated with.&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;accountIdentifier&lt;/strong&gt; - specify the account this credit card is associated with&lt;br/&gt;&lt;br/&gt; &lt;strong&gt;creditCardToken&lt;/strong&gt; - specify the credit card token to unregister&lt;br/&gt;&lt;br/&gt;  | [optional] 

### Return type

[**CreditCardUnregisterView**](CreditCardUnregisterView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_card**
> CreditCardView get_credit_card(token)

Get details for a specific Credit Card.

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
api_instance = tango_client.FundApi(tango_client.ApiClient(configuration))
token = 'token_example' # str | Credit card token

try:
    # Get details for a specific Credit Card.
    api_response = api_instance.get_credit_card(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundApi->get_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Credit card token | 

### Return type

[**CreditCardView**](CreditCardView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_card_deposit**
> CreditCardDepositView get_credit_card_deposit(deposit_id)

Get details for a specific Credit Card Deposit.

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
api_instance = tango_client.FundApi(tango_client.ApiClient(configuration))
deposit_id = 'deposit_id_example' # str | Credit card deposit identifier returned in Deposit response payload

try:
    # Get details for a specific Credit Card Deposit.
    api_response = api_instance.get_credit_card_deposit(deposit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundApi->get_credit_card_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_id** | **str**| Credit card deposit identifier returned in Deposit response payload | 

### Return type

[**CreditCardDepositView**](CreditCardDepositView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_cards**
> list[CreditCardView] list_credit_cards(show_inactive=show_inactive)

List all credit cards registered on this Platform.

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
api_instance = tango_client.FundApi(tango_client.ApiClient(configuration))
show_inactive = false # bool | Show inactive cards (optional) (default to false)

try:
    # List all credit cards registered on this Platform.
    api_response = api_instance.list_credit_cards(show_inactive=show_inactive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundApi->list_credit_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_inactive** | **bool**| Show inactive cards | [optional] [default to false]

### Return type

[**list[CreditCardView]**](CreditCardView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

