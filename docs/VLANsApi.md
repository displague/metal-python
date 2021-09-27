# metal.VLANsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_native_vlan**](VLANsApi.md#assign_native_vlan) | **POST** /ports/{id}/native-vlan | Assign a native VLAN
[**assign_port**](VLANsApi.md#assign_port) | **POST** /ports/{id}/assign | Assign a port to virtual network
[**create_port_vlan_assignment_batch**](VLANsApi.md#create_port_vlan_assignment_batch) | **POST** /ports/{id}/vlan-assignments/batches | Create a new Port-VLAN Assignment management batch
[**create_virtual_network**](VLANsApi.md#create_virtual_network) | **POST** /projects/{id}/virtual-networks | Create a virtual network
[**delete_native_vlan**](VLANsApi.md#delete_native_vlan) | **DELETE** /ports/{id}/native-vlan | Remove native VLAN
[**delete_virtual_network**](VLANsApi.md#delete_virtual_network) | **DELETE** /virtual-networks/{id} | Delete a virtual network
[**find_port_vlan_assignment_batch_by_port_id_and_batch_id**](VLANsApi.md#find_port_vlan_assignment_batch_by_port_id_and_batch_id) | **GET** /ports/{id}/vlan-assignments/batches/{batch_id} | Retrieve a VLAN Assignment Batch&#39;s details
[**find_port_vlan_assignment_batches**](VLANsApi.md#find_port_vlan_assignment_batches) | **GET** /ports/{id}/vlan-assignments/batches | List the VLAN Assignment Batches for a port
[**find_port_vlan_assignment_by_port_id_and_assignment_id**](VLANsApi.md#find_port_vlan_assignment_by_port_id_and_assignment_id) | **GET** /ports/{id}/vlan-assignments/{assignment_id} | Show a particular Port VLAN assignment&#39;s details
[**find_port_vlan_assignments**](VLANsApi.md#find_port_vlan_assignments) | **GET** /ports/{id}/vlan-assignments | List Current VLAN assignments for a port
[**find_virtual_networks**](VLANsApi.md#find_virtual_networks) | **GET** /projects/{id}/virtual-networks | Retrieve all virtual networks
[**get_virtual_network**](VLANsApi.md#get_virtual_network) | **GET** /virtual-networks/{id} | Get a virtual network
[**unassign_port**](VLANsApi.md#unassign_port) | **POST** /ports/{id}/unassign | Unassign a port


# **assign_native_vlan**
> Port assign_native_vlan(id, vnid)

Assign a native VLAN

Sets a virtual network on this port as a \"native VLAN\". The VLAN must have already been assigned using the using the \"Assign a port to a virtual network\" operation.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
vnid = 'vnid_example' # str | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').

    try:
        # Assign a native VLAN
        api_response = api_instance.assign_native_vlan(id, vnid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->assign_native_vlan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **vnid** | **str**| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 

### Return type

[**Port**](Port.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_port**
> Port assign_port(id, vnid)

Assign a port to virtual network

Assign a port for a hardware to virtual network.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
vnid = metal.PortAssignInput() # PortAssignInput | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').

    try:
        # Assign a port to virtual network
        api_response = api_instance.assign_port(id, vnid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->assign_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **vnid** | [**PortAssignInput**](PortAssignInput.md)| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 

### Return type

[**Port**](Port.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_port_vlan_assignment_batch**
> PortVlanAssignmentBatch create_port_vlan_assignment_batch(id, vlan_assignments)

Create a new Port-VLAN Assignment management batch

Create a new asynchronous batch request which handles adding and/or removing the VLANs to which the port is assigned.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
vlan_assignments = metal.PortVlanAssignmentBatchCreateInput() # PortVlanAssignmentBatchCreateInput | VLAN Assignment batch details

    try:
        # Create a new Port-VLAN Assignment management batch
        api_response = api_instance.create_port_vlan_assignment_batch(id, vlan_assignments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->create_port_vlan_assignment_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **vlan_assignments** | [**PortVlanAssignmentBatchCreateInput**](PortVlanAssignmentBatchCreateInput.md)| VLAN Assignment batch details | 

### Return type

[**PortVlanAssignmentBatch**](PortVlanAssignmentBatch.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_network**
> VirtualNetwork create_virtual_network(id, virtual_network)

Create a virtual network

Creates an virtual network.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Project UUID
virtual_network = metal.VirtualNetworkCreateInput() # VirtualNetworkCreateInput | Virtual Network to create

    try:
        # Create a virtual network
        api_response = api_instance.create_virtual_network(id, virtual_network)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->create_virtual_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Project UUID | 
 **virtual_network** | [**VirtualNetworkCreateInput**](VirtualNetworkCreateInput.md)| Virtual Network to create | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_native_vlan**
> Port delete_native_vlan(id)

Remove native VLAN

Removes the native VLAN from this port

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID

    try:
        # Remove native VLAN
        api_response = api_instance.delete_native_vlan(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->delete_native_vlan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 

### Return type

[**Port**](Port.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_network**
> VirtualNetwork delete_virtual_network(id)

Delete a virtual network

Deletes a virtual network.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Virtual Network UUID

    try:
        # Delete a virtual network
        api_response = api_instance.delete_virtual_network(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->delete_virtual_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Virtual Network UUID | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_port_vlan_assignment_batch_by_port_id_and_batch_id**
> PortVlanAssignmentBatch find_port_vlan_assignment_batch_by_port_id_and_batch_id(id, batch_id)

Retrieve a VLAN Assignment Batch's details

Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign or unassign, and the current state of the batch.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
batch_id = 'batch_id_example' # str | Batch ID

    try:
        # Retrieve a VLAN Assignment Batch's details
        api_response = api_instance.find_port_vlan_assignment_batch_by_port_id_and_batch_id(id, batch_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->find_port_vlan_assignment_batch_by_port_id_and_batch_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **batch_id** | [**str**](.md)| Batch ID | 

### Return type

[**PortVlanAssignmentBatch**](PortVlanAssignmentBatch.md)

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

# **find_port_vlan_assignment_batches**
> PortVlanAssignmentBatchList find_port_vlan_assignment_batches(id)

List the VLAN Assignment Batches for a port

Show all the VLAN assignment batches that have been created for managing this port's VLAN assignments

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID

    try:
        # List the VLAN Assignment Batches for a port
        api_response = api_instance.find_port_vlan_assignment_batches(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->find_port_vlan_assignment_batches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 

### Return type

[**PortVlanAssignmentBatchList**](PortVlanAssignmentBatchList.md)

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

# **find_port_vlan_assignment_by_port_id_and_assignment_id**
> PortVlanAssignment find_port_vlan_assignment_by_port_id_and_assignment_id(id, assignment_id, include=include, exclude=exclude)

Show a particular Port VLAN assignment's details

Show the details of a specific Port-VLAN assignment, including the current state and if the VLAN is set as native.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
assignment_id = 'assignment_id_example' # str | Assignment ID
include = ["port","virtual_network"] # list[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional) (default to ["port","virtual_network"])
exclude = ['exclude_example'] # list[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Show a particular Port VLAN assignment's details
        api_response = api_instance.find_port_vlan_assignment_by_port_id_and_assignment_id(id, assignment_id, include=include, exclude=exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->find_port_vlan_assignment_by_port_id_and_assignment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **assignment_id** | [**str**](.md)| Assignment ID | 
 **include** | [**list[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] [default to [&quot;port&quot;,&quot;virtual_network&quot;]]
 **exclude** | [**list[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**PortVlanAssignment**](PortVlanAssignment.md)

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

# **find_port_vlan_assignments**
> PortVlanAssignmentList find_port_vlan_assignments(id, include=include, exclude=exclude)

List Current VLAN assignments for a port

Show the port's current VLAN assignments, including if this VLAN is set as native, and the current state of the assignment (ex. 'assigned' or 'unassigning')

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
include = ["port","virtual_network"] # list[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional) (default to ["port","virtual_network"])
exclude = ['exclude_example'] # list[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # List Current VLAN assignments for a port
        api_response = api_instance.find_port_vlan_assignments(id, include=include, exclude=exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->find_port_vlan_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **include** | [**list[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] [default to [&quot;port&quot;,&quot;virtual_network&quot;]]
 **exclude** | [**list[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**PortVlanAssignmentList**](PortVlanAssignmentList.md)

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

# **find_virtual_networks**
> VirtualNetworkList find_virtual_networks(id, include=include, exclude=exclude, facility=facility, metro=metro)

Retrieve all virtual networks

Provides a list of virtual networks for a single project.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Project UUID
include = ['include_example'] # list[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
exclude = ['exclude_example'] # list[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)
facility = 'facility_example' # str | Filter by Facility ID (uuid) or Facility Code (optional)
metro = 'metro_example' # str | Filter by Metro ID (uuid) or Metro Code (optional)

    try:
        # Retrieve all virtual networks
        api_response = api_instance.find_virtual_networks(id, include=include, exclude=exclude, facility=facility, metro=metro)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->find_virtual_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Project UUID | 
 **include** | [**list[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**list[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 
 **facility** | **str**| Filter by Facility ID (uuid) or Facility Code | [optional] 
 **metro** | **str**| Filter by Metro ID (uuid) or Metro Code | [optional] 

### Return type

[**VirtualNetworkList**](VirtualNetworkList.md)

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

# **get_virtual_network**
> VirtualNetwork get_virtual_network(id)

Get a virtual network

Get a virtual network.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Virtual Network UUID

    try:
        # Get a virtual network
        api_response = api_instance.get_virtual_network(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->get_virtual_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Virtual Network UUID | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

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
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_port**
> Port unassign_port(id, vnid)

Unassign a port

Unassign a port for a hardware.

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
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
vnid = metal.PortAssignInput() # PortAssignInput | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: '1001').

    try:
        # Unassign a port
        api_response = api_instance.unassign_port(id, vnid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->unassign_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **vnid** | [**PortAssignInput**](PortAssignInput.md)| Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;). | 

### Return type

[**Port**](Port.md)

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
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

