<a name="__pageTop"></a>
# metal.models.tags.two_factor_auth_api.TwoFactorAuthApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_tfa_app**](#disable_tfa_app) | **delete** /user/otp/app | Disable two factor authentication
[**disable_tfa_sms**](#disable_tfa_sms) | **delete** /user/otp/sms | Disable two factor authentication
[**enable_tfa_app**](#enable_tfa_app) | **post** /user/otp/app | Enable two factor auth using app
[**enable_tfa_sms**](#enable_tfa_sms) | **post** /user/otp/sms | Enable two factor auth using sms

# **disable_tfa_app**
<a name="disable_tfa_app"></a>
> disable_tfa_app()

Disable two factor authentication

Disables two factor authentication.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import two_factor_auth_api
from metal.types.error import Error
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
    api_instance = two_factor_auth_api.TwoFactorAuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable two factor authentication
        api_response = api_instance.disable_tfa_app()
    except metal.ApiException as e:
        print("Exception when calling TwoFactorAuthApi->disable_tfa_app: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#disable_tfa_app.ApiResponseFor204) | no content
401 | [ApiResponseFor401](#disable_tfa_app.ApiResponseFor401) | unauthorized
404 | [ApiResponseFor404](#disable_tfa_app.ApiResponseFor404) | not found

#### disable_tfa_app.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### disable_tfa_app.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### disable_tfa_app.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[x_auth_token](../../../README.md#x_auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disable_tfa_sms**
<a name="disable_tfa_sms"></a>
> disable_tfa_sms()

Disable two factor authentication

Disables two factor authentication.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import two_factor_auth_api
from metal.types.error import Error
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
    api_instance = two_factor_auth_api.TwoFactorAuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable two factor authentication
        api_response = api_instance.disable_tfa_sms()
    except metal.ApiException as e:
        print("Exception when calling TwoFactorAuthApi->disable_tfa_sms: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#disable_tfa_sms.ApiResponseFor204) | no content
401 | [ApiResponseFor401](#disable_tfa_sms.ApiResponseFor401) | unauthorized
404 | [ApiResponseFor404](#disable_tfa_sms.ApiResponseFor404) | not found

#### disable_tfa_sms.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### disable_tfa_sms.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### disable_tfa_sms.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[x_auth_token](../../../README.md#x_auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable_tfa_app**
<a name="enable_tfa_app"></a>
> enable_tfa_app()

Enable two factor auth using app

Enables two factor authentication using authenticator app.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import two_factor_auth_api
from metal.types.error import Error
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
    api_instance = two_factor_auth_api.TwoFactorAuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enable two factor auth using app
        api_response = api_instance.enable_tfa_app()
    except metal.ApiException as e:
        print("Exception when calling TwoFactorAuthApi->enable_tfa_app: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enable_tfa_app.ApiResponseFor200) | ok
401 | [ApiResponseFor401](#enable_tfa_app.ApiResponseFor401) | unauthorized

#### enable_tfa_app.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### enable_tfa_app.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[x_auth_token](../../../README.md#x_auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable_tfa_sms**
<a name="enable_tfa_sms"></a>
> enable_tfa_sms()

Enable two factor auth using sms

Enables two factor authentication with sms.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import two_factor_auth_api
from metal.types.error import Error
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
    api_instance = two_factor_auth_api.TwoFactorAuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enable two factor auth using sms
        api_response = api_instance.enable_tfa_sms()
    except metal.ApiException as e:
        print("Exception when calling TwoFactorAuthApi->enable_tfa_sms: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enable_tfa_sms.ApiResponseFor200) | ok
401 | [ApiResponseFor401](#enable_tfa_sms.ApiResponseFor401) | unauthorized

#### enable_tfa_sms.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### enable_tfa_sms.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[x_auth_token](../../../README.md#x_auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

