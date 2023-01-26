# metal.InterconnectionsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interconnection_port_virtual_circuit**](InterconnectionsApi.md#create_interconnection_port_virtual_circuit) | **POST** /connections/{connection_id}/ports/{port_id}/virtual-circuits | Create a new Virtual Circuit
[**create_organization_interconnection**](InterconnectionsApi.md#create_organization_interconnection) | **POST** /organizations/{organization_id}/connections | Request a new interconnection for the organization
[**create_project_interconnection**](InterconnectionsApi.md#create_project_interconnection) | **POST** /projects/{project_id}/connections | Request a new interconnection for the project&#39;s organization
[**delete_interconnection**](InterconnectionsApi.md#delete_interconnection) | **DELETE** /connections/{connection_id} | Delete interconnection
[**delete_virtual_circuit**](InterconnectionsApi.md#delete_virtual_circuit) | **DELETE** /virtual-circuits/{id} | Delete a virtual circuit
[**get_interconnection**](InterconnectionsApi.md#get_interconnection) | **GET** /connections/{connection_id} | Get interconnection
[**get_interconnection_port**](InterconnectionsApi.md#get_interconnection_port) | **GET** /connections/{connection_id}/ports/{id} | Get a interconnection port
[**get_virtual_circuit**](InterconnectionsApi.md#get_virtual_circuit) | **GET** /virtual-circuits/{id} | Get a virtual circuit
[**list_interconnection_port_virtual_circuits**](InterconnectionsApi.md#list_interconnection_port_virtual_circuits) | **GET** /connections/{connection_id}/ports/{port_id}/virtual-circuits | List a interconnection port&#39;s virtual circuits
[**list_interconnection_ports**](InterconnectionsApi.md#list_interconnection_ports) | **GET** /connections/{connection_id}/ports | List a interconnection&#39;s ports
[**list_interconnection_virtual_circuits**](InterconnectionsApi.md#list_interconnection_virtual_circuits) | **GET** /connections/{connection_id}/virtual-circuits | List a interconnection&#39;s virtual circuits
[**organization_list_interconnections**](InterconnectionsApi.md#organization_list_interconnections) | **GET** /organizations/{organization_id}/connections | List organization connections
[**project_list_interconnections**](InterconnectionsApi.md#project_list_interconnections) | **GET** /projects/{project_id}/connections | List project connections
[**update_interconnection**](InterconnectionsApi.md#update_interconnection) | **PUT** /connections/{connection_id} | Update interconnection
[**update_virtual_circuit**](InterconnectionsApi.md#update_virtual_circuit) | **PUT** /virtual-circuits/{id} | Update a virtual circuit


# **create_interconnection_port_virtual_circuit**
> CreateInterconnectionPortVirtualCircuit201Response create_interconnection_port_virtual_circuit(connection_id, port_id, create_interconnection_port_virtual_circuit_request)

Create a new Virtual Circuit

Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF ID and subnet, along with the NNI VLAN value.

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection
port_id = 'port_id_example' # str | UUID of the interconnection port
create_interconnection_port_virtual_circuit_request = metal.CreateInterconnectionPortVirtualCircuitRequest() # CreateInterconnectionPortVirtualCircuitRequest | Virtual Circuit details

    try:
        # Create a new Virtual Circuit
        api_response = api_instance.create_interconnection_port_virtual_circuit(connection_id, port_id, create_interconnection_port_virtual_circuit_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->create_interconnection_port_virtual_circuit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 
 **port_id** | **str**| UUID of the interconnection port | 
 **create_interconnection_port_virtual_circuit_request** | [**CreateInterconnectionPortVirtualCircuitRequest**](CreateInterconnectionPortVirtualCircuitRequest.md)| Virtual Circuit details | 

### Return type

[**CreateInterconnectionPortVirtualCircuit201Response**](CreateInterconnectionPortVirtualCircuit201Response.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_interconnection**
> Interconnection create_organization_interconnection(organization_id, interconnection_create_input)

Request a new interconnection for the organization

Creates a new interconnection request. A Project ID must be specified in the request body for connections on shared ports.

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
    api_instance = metal.InterconnectionsApi(api_client)
    organization_id = 'organization_id_example' # str | UUID of the organization
interconnection_create_input = metal.InterconnectionCreateInput() # InterconnectionCreateInput | Interconnection details

    try:
        # Request a new interconnection for the organization
        api_response = api_instance.create_organization_interconnection(organization_id, interconnection_create_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->create_organization_interconnection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| UUID of the organization | 
 **interconnection_create_input** | [**InterconnectionCreateInput**](InterconnectionCreateInput.md)| Interconnection details | 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_interconnection**
> Interconnection create_project_interconnection(project_id, interconnection_create_input)

Request a new interconnection for the project's organization

Creates a new interconnection request

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
    api_instance = metal.InterconnectionsApi(api_client)
    project_id = 'project_id_example' # str | UUID of the project
interconnection_create_input = metal.InterconnectionCreateInput() # InterconnectionCreateInput | Interconnection details

    try:
        # Request a new interconnection for the project's organization
        api_response = api_instance.create_project_interconnection(project_id, interconnection_create_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->create_project_interconnection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| UUID of the project | 
 **interconnection_create_input** | [**InterconnectionCreateInput**](InterconnectionCreateInput.md)| Interconnection details | 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**403** | forbidden |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interconnection**
> Interconnection delete_interconnection(connection_id)

Delete interconnection

Delete a interconnection, its associated ports and virtual circuits.

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Interconnection UUID

    try:
        # Delete interconnection
        api_response = api_instance.delete_interconnection(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->delete_interconnection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Interconnection UUID | 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_circuit**
> CreateInterconnectionPortVirtualCircuit201Response delete_virtual_circuit(id)

Delete a virtual circuit

Delete a virtual circuit from a Dedicated Port.

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
    api_instance = metal.InterconnectionsApi(api_client)
    id = 'id_example' # str | Virtual Circuit UUID

    try:
        # Delete a virtual circuit
        api_response = api_instance.delete_virtual_circuit(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->delete_virtual_circuit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Virtual Circuit UUID | 

### Return type

[**CreateInterconnectionPortVirtualCircuit201Response**](CreateInterconnectionPortVirtualCircuit201Response.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | accepted |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interconnection**
> Interconnection get_interconnection(connection_id)

Get interconnection

Get the details of a interconnection

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Interconnection UUID

    try:
        # Get interconnection
        api_response = api_instance.get_interconnection(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->get_interconnection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Interconnection UUID | 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interconnection_port**
> InterconnectionPort get_interconnection_port(connection_id, id)

Get a interconnection port

Get the details of an interconnection port.

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection
id = 'id_example' # str | Port UUID

    try:
        # Get a interconnection port
        api_response = api_instance.get_interconnection_port(connection_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->get_interconnection_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 
 **id** | **str**| Port UUID | 

### Return type

[**InterconnectionPort**](InterconnectionPort.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_circuit**
> CreateInterconnectionPortVirtualCircuit201Response get_virtual_circuit(id)

Get a virtual circuit

Get the details of a virtual circuit

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
    api_instance = metal.InterconnectionsApi(api_client)
    id = 'id_example' # str | Virtual Circuit UUID

    try:
        # Get a virtual circuit
        api_response = api_instance.get_virtual_circuit(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->get_virtual_circuit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Virtual Circuit UUID | 

### Return type

[**CreateInterconnectionPortVirtualCircuit201Response**](CreateInterconnectionPortVirtualCircuit201Response.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_interconnection_port_virtual_circuits**
> VirtualCircuitList list_interconnection_port_virtual_circuits(connection_id, port_id)

List a interconnection port's virtual circuits

List the virtual circuit record(s) associatiated with a particular interconnection port.

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection
port_id = 'port_id_example' # str | UUID of the interconnection port

    try:
        # List a interconnection port's virtual circuits
        api_response = api_instance.list_interconnection_port_virtual_circuits(connection_id, port_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_port_virtual_circuits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 
 **port_id** | **str**| UUID of the interconnection port | 

### Return type

[**VirtualCircuitList**](VirtualCircuitList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_interconnection_ports**
> InterconnectionPortList list_interconnection_ports(connection_id)

List a interconnection's ports

List the ports associated to an interconnection.

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection

    try:
        # List a interconnection's ports
        api_response = api_instance.list_interconnection_ports(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 

### Return type

[**InterconnectionPortList**](InterconnectionPortList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_interconnection_virtual_circuits**
> VirtualCircuitList list_interconnection_virtual_circuits(connection_id)

List a interconnection's virtual circuits

List the virtual circuit record(s) associated with a particular interconnection id.

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | UUID of the interconnection

    try:
        # List a interconnection's virtual circuits
        api_response = api_instance.list_interconnection_virtual_circuits(connection_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_virtual_circuits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| UUID of the interconnection | 

### Return type

[**VirtualCircuitList**](VirtualCircuitList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_list_interconnections**
> InterconnectionList organization_list_interconnections(organization_id)

List organization connections

List the connections belonging to the organization

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
    api_instance = metal.InterconnectionsApi(api_client)
    organization_id = 'organization_id_example' # str | UUID of the organization

    try:
        # List organization connections
        api_response = api_instance.organization_list_interconnections(organization_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->organization_list_interconnections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| UUID of the organization | 

### Return type

[**InterconnectionList**](InterconnectionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_list_interconnections**
> InterconnectionList project_list_interconnections(project_id)

List project connections

List the connections belonging to the project

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
    api_instance = metal.InterconnectionsApi(api_client)
    project_id = 'project_id_example' # str | UUID of the project

    try:
        # List project connections
        api_response = api_instance.project_list_interconnections(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->project_list_interconnections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| UUID of the project | 

### Return type

[**InterconnectionList**](InterconnectionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interconnection**
> Interconnection update_interconnection(connection_id, interconnection_update_input)

Update interconnection

Update the details of a interconnection

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
    api_instance = metal.InterconnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | Interconnection UUID
interconnection_update_input = metal.InterconnectionUpdateInput() # InterconnectionUpdateInput | Updated interconnection details

    try:
        # Update interconnection
        api_response = api_instance.update_interconnection(connection_id, interconnection_update_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->update_interconnection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Interconnection UUID | 
 **interconnection_update_input** | [**InterconnectionUpdateInput**](InterconnectionUpdateInput.md)| Updated interconnection details | 

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_circuit**
> CreateInterconnectionPortVirtualCircuit201Response update_virtual_circuit(id, update_virtual_circuit_request)

Update a virtual circuit

Update the details of a virtual circuit.

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
    api_instance = metal.InterconnectionsApi(api_client)
    id = 'id_example' # str | Virtual Circuit UUID
update_virtual_circuit_request = metal.UpdateVirtualCircuitRequest() # UpdateVirtualCircuitRequest | Updated Virtual Circuit details

    try:
        # Update a virtual circuit
        api_response = api_instance.update_virtual_circuit(id, update_virtual_circuit_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InterconnectionsApi->update_virtual_circuit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Virtual Circuit UUID | 
 **update_virtual_circuit_request** | [**UpdateVirtualCircuitRequest**](UpdateVirtualCircuitRequest.md)| Updated Virtual Circuit details | 

### Return type

[**CreateInterconnectionPortVirtualCircuit201Response**](CreateInterconnectionPortVirtualCircuit201Response.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**202** | accepted |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

