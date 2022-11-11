# tango_client.EmailTemplatesApi

All URIs are relative to *https://integration-api.tangocard.com/raas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_template**](EmailTemplatesApi.md#create_email_template) | **POST** /emailTemplates | Create a new email template
[**delete_email_template**](EmailTemplatesApi.md#delete_email_template) | **DELETE** /emailTemplates/{etid} | Delete a specific Email Template on this Platform.
[**get_email_template**](EmailTemplatesApi.md#get_email_template) | **GET** /emailTemplates/{etid} | Get details for a specific Email Template on this Platform.
[**list_email_templates**](EmailTemplatesApi.md#list_email_templates) | **GET** /emailTemplates | Get a list of all Email Templates on this Platform.
[**update_email_template**](EmailTemplatesApi.md#update_email_template) | **PATCH** /emailTemplates/{etid} | Update details for a specific Email Template on this Platform.


# **create_email_template**
> EmailTemplateViewVerbose create_email_template(create_email_template_criteria=create_email_template_criteria)

Create a new email template

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
api_instance = tango_client.EmailTemplatesApi(tango_client.ApiClient(configuration))
create_email_template_criteria = tango_client.CreateEmailTemplateCriteria() # CreateEmailTemplateCriteria | <strong>name</strong> - A unique name to give the template.<br/><br/><strong>fromName</strong> - The name that will appear in the From line of the email.<br/><br/><strong>subject</strong> - The Subject of the email.<br/><br/><strong>headerImage</strong> - A Base64 encoded string of an image that will show as the header of the email.<br/><br/><strong>headerImageAltText</strong> - The Alt Text for the Header Image in the email.<br/><br/><strong>accentColor</strong> - A Hex color value, six hexadecimal digits preceded by a pound sign, used as an accent in the email.<br/><br/><strong>messageBody</strong> - The message body for the email. This is often used to let the recipient know why they have received the reward.<br/><br/><strong>closing</strong> - After the reward credential, a space to close the message to the recipient<br/><br/><strong>customerServiceMessage</strong> - (Optional) If left null, Tango Card's Customer Support contact information will be included. Otherwise contact information for your customer support, if you are taking responsibility for providing first tier customer support of your recipients. <br/><br/><strong>accessControl</strong> - (Optional) Which Customers and/or Accounts should have access to this template.<br/><br/><strong>accessControl - type</strong> - The type of access being specified: PLATFORM, CUSTOMER or ACCOUNT.<br/><br/><strong>accessControl - identifier</strong> - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.<br/><br/><strong>defaults</strong> - If you want this template to be used at order time for the given Platform, Customer or Account when the Email Template Identifier (etid) is not provided with the order.<br/><br/><strong>defaults - type</strong> - The type of default being specified: PLATFORM, CUSTOMER or ACCOUNT.<br/><br/><strong>defaults - identifier</strong> - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.<br/><br/> (optional)

try:
    # Create a new email template
    api_response = api_instance.create_email_template(create_email_template_criteria=create_email_template_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplatesApi->create_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_email_template_criteria** | [**CreateEmailTemplateCriteria**](CreateEmailTemplateCriteria.md)| &lt;strong&gt;name&lt;/strong&gt; - A unique name to give the template.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;fromName&lt;/strong&gt; - The name that will appear in the From line of the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;subject&lt;/strong&gt; - The Subject of the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;headerImage&lt;/strong&gt; - A Base64 encoded string of an image that will show as the header of the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;headerImageAltText&lt;/strong&gt; - The Alt Text for the Header Image in the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accentColor&lt;/strong&gt; - A Hex color value, six hexadecimal digits preceded by a pound sign, used as an accent in the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;messageBody&lt;/strong&gt; - The message body for the email. This is often used to let the recipient know why they have received the reward.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;closing&lt;/strong&gt; - After the reward credential, a space to close the message to the recipient&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;customerServiceMessage&lt;/strong&gt; - (Optional) If left null, Tango Card&#39;s Customer Support contact information will be included. Otherwise contact information for your customer support, if you are taking responsibility for providing first tier customer support of your recipients. &lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accessControl&lt;/strong&gt; - (Optional) Which Customers and/or Accounts should have access to this template.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accessControl - type&lt;/strong&gt; - The type of access being specified: PLATFORM, CUSTOMER or ACCOUNT.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accessControl - identifier&lt;/strong&gt; - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;defaults&lt;/strong&gt; - If you want this template to be used at order time for the given Platform, Customer or Account when the Email Template Identifier (etid) is not provided with the order.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;defaults - type&lt;/strong&gt; - The type of default being specified: PLATFORM, CUSTOMER or ACCOUNT.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;defaults - identifier&lt;/strong&gt; - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.&lt;br/&gt;&lt;br/&gt; | [optional] 

### Return type

[**EmailTemplateViewVerbose**](EmailTemplateViewVerbose.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_template**
> delete_email_template(etid)

Delete a specific Email Template on this Platform.

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
api_instance = tango_client.EmailTemplatesApi(tango_client.ApiClient(configuration))
etid = 'etid_example' # str | Email Template Identifier (ETID) is returned in the email template response payload

try:
    # Delete a specific Email Template on this Platform.
    api_instance.delete_email_template(etid)
except ApiException as e:
    print("Exception when calling EmailTemplatesApi->delete_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etid** | **str**| Email Template Identifier (ETID) is returned in the email template response payload | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> EmailTemplateViewVerbose get_email_template(etid)

Get details for a specific Email Template on this Platform.

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
api_instance = tango_client.EmailTemplatesApi(tango_client.ApiClient(configuration))
etid = 'etid_example' # str | Email Template Identifier (ETID) is returned in the email template response payload

try:
    # Get details for a specific Email Template on this Platform.
    api_response = api_instance.get_email_template(etid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplatesApi->get_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etid** | **str**| Email Template Identifier (ETID) is returned in the email template response payload | 

### Return type

[**EmailTemplateViewVerbose**](EmailTemplateViewVerbose.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_email_templates**
> EmailTemplateListView list_email_templates(elements_per_block=elements_per_block, page=page)

Get a list of all Email Templates on this Platform.

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
api_instance = tango_client.EmailTemplatesApi(tango_client.ApiClient(configuration))
elements_per_block = 56 # int | specify the number of elements in a block. (optional)
page = 56 # int | specify the page number to return. (optional)

try:
    # Get a list of all Email Templates on this Platform.
    api_response = api_instance.list_email_templates(elements_per_block=elements_per_block, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplatesApi->list_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elements_per_block** | **int**| specify the number of elements in a block. | [optional] 
 **page** | **int**| specify the page number to return. | [optional] 

### Return type

[**EmailTemplateListView**](EmailTemplateListView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_template**
> EmailTemplateViewVerbose update_email_template(etid, update_email_template_criteria=update_email_template_criteria)

Update details for a specific Email Template on this Platform.

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
api_instance = tango_client.EmailTemplatesApi(tango_client.ApiClient(configuration))
etid = 'etid_example' # str | Email Template Identifier (ETID) is returned in the email template response payload
update_email_template_criteria = tango_client.UpdateEmailTemplateCriteria() # UpdateEmailTemplateCriteria | <strong>name</strong> - (Optional) A unique name to give the template.<br/><br/><strong>fromName</strong> - (Optional) The name that will appear in the From line of the email.<br/><br/><strong>subject</strong> - (Optional) The Subject of the email.<br/><br/><strong>headerImage</strong> - (Optional) A Base64 encoded string of an image that will show as the header of the email.<br/><br/><strong>headerImageAltText</strong> - (Optional) The Alt Text for the Header Image in the email.<br/><br/><strong>accentColor</strong> - (Optional) A Hex color value, six hexadecimal digits preceded by a pound sign, used as an accent in the email.<br/><br/><strong>messageBody</strong> - (Optional) The message body for the email. This is often used to let the recipient know why they have received the reward.<br/><br/><strong>closing</strong> - (Optional) After the reward credential, a space to close the message to the recipient<br/><br/><strong>customerServiceMessage</strong> - (Optional) If left null, Tango Card's Customer Support contact information will be included. Otherwise contact information for your customer support, if you are taking responsibility for providing first tier customer support of your recipients. <br/><br/><strong>accessControl</strong> - (Optional) Which Customers and/or Accounts should have access to this template.<br/><br/><strong>accessControl - type</strong> - The type of access being specified: PLATFORM, CUSTOMER or ACCOUNT.<br/><br/><strong>accessControl - identifier</strong> - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.<br/><br/><strong>defaults</strong> - If you want this template to be used at order time for the given Platform, Customer or Account when the Email Template Identifier (etid) is not provided with the order.<br/><br/><strong>defaults - type</strong> - The type of default being specified: PLATFORM, CUSTOMER or ACCOUNT.<br/><br/><strong>defaults - identifier</strong> - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.<br/><br/> (optional)

try:
    # Update details for a specific Email Template on this Platform.
    api_response = api_instance.update_email_template(etid, update_email_template_criteria=update_email_template_criteria)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplatesApi->update_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etid** | **str**| Email Template Identifier (ETID) is returned in the email template response payload | 
 **update_email_template_criteria** | [**UpdateEmailTemplateCriteria**](UpdateEmailTemplateCriteria.md)| &lt;strong&gt;name&lt;/strong&gt; - (Optional) A unique name to give the template.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;fromName&lt;/strong&gt; - (Optional) The name that will appear in the From line of the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;subject&lt;/strong&gt; - (Optional) The Subject of the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;headerImage&lt;/strong&gt; - (Optional) A Base64 encoded string of an image that will show as the header of the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;headerImageAltText&lt;/strong&gt; - (Optional) The Alt Text for the Header Image in the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accentColor&lt;/strong&gt; - (Optional) A Hex color value, six hexadecimal digits preceded by a pound sign, used as an accent in the email.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;messageBody&lt;/strong&gt; - (Optional) The message body for the email. This is often used to let the recipient know why they have received the reward.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;closing&lt;/strong&gt; - (Optional) After the reward credential, a space to close the message to the recipient&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;customerServiceMessage&lt;/strong&gt; - (Optional) If left null, Tango Card&#39;s Customer Support contact information will be included. Otherwise contact information for your customer support, if you are taking responsibility for providing first tier customer support of your recipients. &lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accessControl&lt;/strong&gt; - (Optional) Which Customers and/or Accounts should have access to this template.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accessControl - type&lt;/strong&gt; - The type of access being specified: PLATFORM, CUSTOMER or ACCOUNT.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;accessControl - identifier&lt;/strong&gt; - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;defaults&lt;/strong&gt; - If you want this template to be used at order time for the given Platform, Customer or Account when the Email Template Identifier (etid) is not provided with the order.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;defaults - type&lt;/strong&gt; - The type of default being specified: PLATFORM, CUSTOMER or ACCOUNT.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;defaults - identifier&lt;/strong&gt; - If the type is PLATFORM, the platform name or can be left blank. If the type is CUSTOMER OR ACCOUNT, the customerIdentifier or the accountIdentifier, respectively.&lt;br/&gt;&lt;br/&gt; | [optional] 

### Return type

[**EmailTemplateViewVerbose**](EmailTemplateViewVerbose.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

