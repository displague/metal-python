<a name="__pageTop"></a>
# metal.models.tags.operating_systems_api.OperatingSystemsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_operating_system_version**](#find_operating_system_version) | **get** /operating-system-versions | Retrieve all operating system versions
[**find_operating_systems**](#find_operating_systems) | **get** /operating-systems | Retrieve all operating systems

# **find_operating_system_version**
<a name="find_operating_system_version"></a>
> OperatingSystemList find_operating_system_version()

Retrieve all operating system versions

Provides a listing of available operating system versions.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import operating_systems_api
from metal.types.error import Error
from metal.types.operating_system_list import OperatingSystemList
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
    api_instance = operating_systems_api.OperatingSystemsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve all operating system versions
        api_response = api_instance.find_operating_system_version()
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling OperatingSystemsApi->find_operating_system_version: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_operating_system_version.ApiResponseFor200) | ok
401 | [ApiResponseFor401](#find_operating_system_version.ApiResponseFor401) | unauthorized

#### find_operating_system_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OperatingSystemList**](../../models/OperatingSystemList.md) |  | 


#### find_operating_system_version.ApiResponseFor401
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

# **find_operating_systems**
<a name="find_operating_systems"></a>
> OperatingSystemList find_operating_systems()

Retrieve all operating systems

Provides a listing of available operating systems to provision your new device with.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import operating_systems_api
from metal.types.error import Error
from metal.types.operating_system_list import OperatingSystemList
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
    api_instance = operating_systems_api.OperatingSystemsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve all operating systems
        api_response = api_instance.find_operating_systems()
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling OperatingSystemsApi->find_operating_systems: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_operating_systems.ApiResponseFor200) | ok
401 | [ApiResponseFor401](#find_operating_systems.ApiResponseFor401) | unauthorized

#### find_operating_systems.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OperatingSystemList**](../../models/OperatingSystemList.md) |  | 


#### find_operating_systems.ApiResponseFor401
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

