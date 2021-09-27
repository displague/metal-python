# metal.GlobalBgpRangesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_global_bgp_ranges**](GlobalBgpRangesApi.md#find_global_bgp_ranges) | **GET** /projects/{id}/global-bgp-ranges | Retrieve all global bgp ranges


# **find_global_bgp_ranges**
> GlobalBgpRangeList find_global_bgp_ranges(id)

Retrieve all global bgp ranges

Returns all global bgp ranges for a project

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
    api_instance = metal.GlobalBgpRangesApi(api_client)
    id = 'id_example' # str | Project UUID

    try:
        # Retrieve all global bgp ranges
        api_response = api_instance.find_global_bgp_ranges(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlobalBgpRangesApi->find_global_bgp_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Project UUID | 

### Return type

[**GlobalBgpRangeList**](GlobalBgpRangeList.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

