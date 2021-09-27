# metal.PaymentMethodsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentMethodsApi.md#create_payment_method) | **POST** /organizations/{id}/payment-methods | Create a payment method for the given organization
[**delete_payment_method**](PaymentMethodsApi.md#delete_payment_method) | **DELETE** /payment-methods/{id} | Delete the payment method
[**find_organization_payment_methods**](PaymentMethodsApi.md#find_organization_payment_methods) | **GET** /organizations/{id}/payment-methods | Retrieve all payment methods of an organization
[**find_payment_method_by_id**](PaymentMethodsApi.md#find_payment_method_by_id) | **GET** /payment-methods/{id} | Retrieve a payment method
[**update_payment_method**](PaymentMethodsApi.md#update_payment_method) | **PUT** /payment-methods/{id} | Update the payment method


# **create_payment_method**
> PaymentMethod create_payment_method(id, payment_method)

Create a payment method for the given organization

Creates a payment method.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.PaymentMethodsApi(api_client)
    id = 'id_example' # str | Organization UUID
payment_method = metal.PaymentMethodCreateInput() # PaymentMethodCreateInput | Payment Method to create

    try:
        # Create a payment method for the given organization
        api_response = api_instance.create_payment_method(id, payment_method)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->create_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Organization UUID | 
 **payment_method** | [**PaymentMethodCreateInput**](PaymentMethodCreateInput.md)| Payment Method to create | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(id)

Delete the payment method

Deletes the payment method.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.PaymentMethodsApi(api_client)
    id = 'id_example' # str | Payment Method UUID

    try:
        # Delete the payment method
        api_instance.delete_payment_method(id)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->delete_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Payment Method UUID | 

### Return type

void (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_organization_payment_methods**
> PaymentMethodList find_organization_payment_methods(id, include=include, exclude=exclude, page=page, per_page=per_page)

Retrieve all payment methods of an organization

Returns all payment methods of an organization.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.PaymentMethodsApi(api_client)
    id = 'id_example' # str | Organization UUID
include = ['include_example'] # list[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
exclude = ['exclude_example'] # list[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
page = 1 # int | Page to return (optional) (default to 1)
per_page = 10 # int | Items returned per page (optional) (default to 10)

    try:
        # Retrieve all payment methods of an organization
        api_response = api_instance.find_organization_payment_methods(id, include=include, exclude=exclude, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->find_organization_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Organization UUID | 
 **include** | [**list[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**list[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **page** | **int**| Page to return | [optional] [default to 1]
 **per_page** | **int**| Items returned per page | [optional] [default to 10]

### Return type

[**PaymentMethodList**](PaymentMethodList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_payment_method_by_id**
> PaymentMethod find_payment_method_by_id(id, include=include, exclude=exclude)

Retrieve a payment method

Returns a payment method

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.PaymentMethodsApi(api_client)
    id = 'id_example' # str | Payment Method UUID
include = ['include_example'] # list[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
exclude = ['exclude_example'] # list[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve a payment method
        api_response = api_instance.find_payment_method_by_id(id, include=include, exclude=exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->find_payment_method_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Payment Method UUID | 
 **include** | [**list[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**list[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> PaymentMethod update_payment_method(id, payment_method)

Update the payment method

Updates the payment method.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.PaymentMethodsApi(api_client)
    id = 'id_example' # str | Payment Method UUID
payment_method = metal.PaymentMethodUpdateInput() # PaymentMethodUpdateInput | Payment Method to update

    try:
        # Update the payment method
        api_response = api_instance.update_payment_method(id, payment_method)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->update_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Payment Method UUID | 
 **payment_method** | [**PaymentMethodUpdateInput**](PaymentMethodUpdateInput.md)| Payment Method to update | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

