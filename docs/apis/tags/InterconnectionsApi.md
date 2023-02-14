<a name="__pageTop"></a>
# metal.models.tags.interconnections_api.InterconnectionsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interconnection_port_virtual_circuit**](#create_interconnection_port_virtual_circuit) | **post** /connections/{connection_id}/ports/{port_id}/virtual-circuits | Create a new Virtual Circuit
[**create_organization_interconnection**](#create_organization_interconnection) | **post** /organizations/{organization_id}/connections | Request a new interconnection for the organization
[**create_project_interconnection**](#create_project_interconnection) | **post** /projects/{project_id}/connections | Request a new interconnection for the project&#x27;s organization
[**delete_interconnection**](#delete_interconnection) | **delete** /connections/{connection_id} | Delete interconnection
[**delete_virtual_circuit**](#delete_virtual_circuit) | **delete** /virtual-circuits/{id} | Delete a virtual circuit
[**get_interconnection**](#get_interconnection) | **get** /connections/{connection_id} | Get interconnection
[**get_interconnection_port**](#get_interconnection_port) | **get** /connections/{connection_id}/ports/{id} | Get a interconnection port
[**get_virtual_circuit**](#get_virtual_circuit) | **get** /virtual-circuits/{id} | Get a virtual circuit
[**list_interconnection_port_virtual_circuits**](#list_interconnection_port_virtual_circuits) | **get** /connections/{connection_id}/ports/{port_id}/virtual-circuits | List a interconnection port&#x27;s virtual circuits
[**list_interconnection_ports**](#list_interconnection_ports) | **get** /connections/{connection_id}/ports | List a interconnection&#x27;s ports
[**list_interconnection_virtual_circuits**](#list_interconnection_virtual_circuits) | **get** /connections/{connection_id}/virtual-circuits | List a interconnection&#x27;s virtual circuits
[**organization_list_interconnections**](#organization_list_interconnections) | **get** /organizations/{organization_id}/connections | List organization connections
[**project_list_interconnections**](#project_list_interconnections) | **get** /projects/{project_id}/connections | List project connections
[**update_interconnection**](#update_interconnection) | **put** /connections/{connection_id} | Update interconnection
[**update_virtual_circuit**](#update_virtual_circuit) | **put** /virtual-circuits/{id} | Update a virtual circuit

# **create_interconnection_port_virtual_circuit**
<a name="create_interconnection_port_virtual_circuit"></a>
> CreateInterconnectionPortVirtualCircuit201Response create_interconnection_port_virtual_circuit(connection_idport_idcreate_interconnection_port_virtual_circuit_request)

Create a new Virtual Circuit

Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF ID and subnet, along with the NNI VLAN value.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.create_interconnection_port_virtual_circuit201_response import CreateInterconnectionPortVirtualCircuit201Response
from metal.types.create_interconnection_port_virtual_circuit_request import CreateInterconnectionPortVirtualCircuitRequest
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
        'port_id': "port_id_example",
    }
    body = CreateInterconnectionPortVirtualCircuitRequest(None)
    try:
        # Create a new Virtual Circuit
        api_response = api_instance.create_interconnection_port_virtual_circuit(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->create_interconnection_port_virtual_circuit: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInterconnectionPortVirtualCircuitRequest**](../../models/CreateInterconnectionPortVirtualCircuitRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 
port_id | PortIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# PortIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_interconnection_port_virtual_circuit.ApiResponseFor201) | ok
403 | [ApiResponseFor403](#create_interconnection_port_virtual_circuit.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#create_interconnection_port_virtual_circuit.ApiResponseFor404) | not found

#### create_interconnection_port_virtual_circuit.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInterconnectionPortVirtualCircuit201Response**](../../models/CreateInterconnectionPortVirtualCircuit201Response.md) |  | 


#### create_interconnection_port_virtual_circuit.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_interconnection_port_virtual_circuit.ApiResponseFor404
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

# **create_organization_interconnection**
<a name="create_organization_interconnection"></a>
> Interconnection create_organization_interconnection(organization_idinterconnection_create_input)

Request a new interconnection for the organization

Creates a new interconnection request. A Project ID must be specified in the request body for connections on shared ports.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_create_input import InterconnectionCreateInput
from metal.types.interconnection import Interconnection
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_id': "organization_id_example",
    }
    body = InterconnectionCreateInput(
        contact_email="contact_email_example",
        description="description_example",
        metro="metro_example",
        mode="standard",
        name="name_example",
        project="project_example",
        redundancy="redundancy_example",
        service_token_type="a_side",
        speed=10000000000,
        tags=[
            "tags_example"
        ],
        type="type_example",
        vlans=[1000,1001],
        vrfs=[
            "vrfs_example"
        ],
    )
    try:
        # Request a new interconnection for the organization
        api_response = api_instance.create_organization_interconnection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->create_organization_interconnection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionCreateInput**](../../models/InterconnectionCreateInput.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_id | OrganizationIdSchema | | 

# OrganizationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_organization_interconnection.ApiResponseFor201) | created
403 | [ApiResponseFor403](#create_organization_interconnection.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#create_organization_interconnection.ApiResponseFor404) | not found
422 | [ApiResponseFor422](#create_organization_interconnection.ApiResponseFor422) | unprocessable entity

#### create_organization_interconnection.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Interconnection**](../../models/Interconnection.md) |  | 


#### create_organization_interconnection.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_organization_interconnection.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_organization_interconnection.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[x_auth_token](../../../README.md#x_auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_project_interconnection**
<a name="create_project_interconnection"></a>
> Interconnection create_project_interconnection(project_idinterconnection_create_input)

Request a new interconnection for the project's organization

Creates a new interconnection request

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_create_input import InterconnectionCreateInput
from metal.types.interconnection import Interconnection
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': "project_id_example",
    }
    body = InterconnectionCreateInput(
        contact_email="contact_email_example",
        description="description_example",
        metro="metro_example",
        mode="standard",
        name="name_example",
        project="project_example",
        redundancy="redundancy_example",
        service_token_type="a_side",
        speed=10000000000,
        tags=[
            "tags_example"
        ],
        type="type_example",
        vlans=[1000,1001],
        vrfs=[
            "vrfs_example"
        ],
    )
    try:
        # Request a new interconnection for the project's organization
        api_response = api_instance.create_project_interconnection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->create_project_interconnection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionCreateInput**](../../models/InterconnectionCreateInput.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_project_interconnection.ApiResponseFor201) | created
403 | [ApiResponseFor403](#create_project_interconnection.ApiResponseFor403) | forbidden
422 | [ApiResponseFor422](#create_project_interconnection.ApiResponseFor422) | unprocessable entity

#### create_project_interconnection.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Interconnection**](../../models/Interconnection.md) |  | 


#### create_project_interconnection.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_project_interconnection.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[x_auth_token](../../../README.md#x_auth_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_interconnection**
<a name="delete_interconnection"></a>
> Interconnection delete_interconnection(connection_id)

Delete interconnection

Delete a interconnection, its associated ports and virtual circuits.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection import Interconnection
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
    }
    try:
        # Delete interconnection
        api_response = api_instance.delete_interconnection(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->delete_interconnection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#delete_interconnection.ApiResponseFor202) | accepted
403 | [ApiResponseFor403](#delete_interconnection.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#delete_interconnection.ApiResponseFor404) | not found

#### delete_interconnection.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Interconnection**](../../models/Interconnection.md) |  | 


#### delete_interconnection.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_interconnection.ApiResponseFor404
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

# **delete_virtual_circuit**
<a name="delete_virtual_circuit"></a>
> CreateInterconnectionPortVirtualCircuit201Response delete_virtual_circuit(id)

Delete a virtual circuit

Delete a virtual circuit from a Dedicated Port.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.create_interconnection_port_virtual_circuit201_response import CreateInterconnectionPortVirtualCircuit201Response
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete a virtual circuit
        api_response = api_instance.delete_virtual_circuit(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->delete_virtual_circuit: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#delete_virtual_circuit.ApiResponseFor202) | accepted
403 | [ApiResponseFor403](#delete_virtual_circuit.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#delete_virtual_circuit.ApiResponseFor404) | not found

#### delete_virtual_circuit.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInterconnectionPortVirtualCircuit201Response**](../../models/CreateInterconnectionPortVirtualCircuit201Response.md) |  | 


#### delete_virtual_circuit.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_virtual_circuit.ApiResponseFor404
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

# **get_interconnection**
<a name="get_interconnection"></a>
> Interconnection get_interconnection(connection_id)

Get interconnection

Get the details of a interconnection

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection import Interconnection
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
    }
    try:
        # Get interconnection
        api_response = api_instance.get_interconnection(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->get_interconnection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_interconnection.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#get_interconnection.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#get_interconnection.ApiResponseFor404) | not found

#### get_interconnection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Interconnection**](../../models/Interconnection.md) |  | 


#### get_interconnection.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_interconnection.ApiResponseFor404
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

# **get_interconnection_port**
<a name="get_interconnection_port"></a>
> InterconnectionPort get_interconnection_port(connection_idid)

Get a interconnection port

Get the details of an interconnection port.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_port import InterconnectionPort
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
        'id': "id_example",
    }
    try:
        # Get a interconnection port
        api_response = api_instance.get_interconnection_port(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->get_interconnection_port: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 
id | IdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_interconnection_port.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#get_interconnection_port.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#get_interconnection_port.ApiResponseFor404) | not found

#### get_interconnection_port.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionPort**](../../models/InterconnectionPort.md) |  | 


#### get_interconnection_port.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_interconnection_port.ApiResponseFor404
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

# **get_virtual_circuit**
<a name="get_virtual_circuit"></a>
> CreateInterconnectionPortVirtualCircuit201Response get_virtual_circuit(id)

Get a virtual circuit

Get the details of a virtual circuit

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.create_interconnection_port_virtual_circuit201_response import CreateInterconnectionPortVirtualCircuit201Response
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Get a virtual circuit
        api_response = api_instance.get_virtual_circuit(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->get_virtual_circuit: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_virtual_circuit.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#get_virtual_circuit.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#get_virtual_circuit.ApiResponseFor404) | not found

#### get_virtual_circuit.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInterconnectionPortVirtualCircuit201Response**](../../models/CreateInterconnectionPortVirtualCircuit201Response.md) |  | 


#### get_virtual_circuit.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_virtual_circuit.ApiResponseFor404
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

# **list_interconnection_port_virtual_circuits**
<a name="list_interconnection_port_virtual_circuits"></a>
> VirtualCircuitList list_interconnection_port_virtual_circuits(connection_idport_id)

List a interconnection port's virtual circuits

List the virtual circuit record(s) associatiated with a particular interconnection port.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.virtual_circuit_list import VirtualCircuitList
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
        'port_id': "port_id_example",
    }
    try:
        # List a interconnection port's virtual circuits
        api_response = api_instance.list_interconnection_port_virtual_circuits(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_port_virtual_circuits: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 
port_id | PortIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# PortIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_interconnection_port_virtual_circuits.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#list_interconnection_port_virtual_circuits.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#list_interconnection_port_virtual_circuits.ApiResponseFor404) | not found

#### list_interconnection_port_virtual_circuits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VirtualCircuitList**](../../models/VirtualCircuitList.md) |  | 


#### list_interconnection_port_virtual_circuits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### list_interconnection_port_virtual_circuits.ApiResponseFor404
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

# **list_interconnection_ports**
<a name="list_interconnection_ports"></a>
> InterconnectionPortList list_interconnection_ports(connection_id)

List a interconnection's ports

List the ports associated to an interconnection.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_port_list import InterconnectionPortList
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
    }
    try:
        # List a interconnection's ports
        api_response = api_instance.list_interconnection_ports(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_ports: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_interconnection_ports.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#list_interconnection_ports.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#list_interconnection_ports.ApiResponseFor404) | not found

#### list_interconnection_ports.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionPortList**](../../models/InterconnectionPortList.md) |  | 


#### list_interconnection_ports.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### list_interconnection_ports.ApiResponseFor404
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

# **list_interconnection_virtual_circuits**
<a name="list_interconnection_virtual_circuits"></a>
> VirtualCircuitList list_interconnection_virtual_circuits(connection_id)

List a interconnection's virtual circuits

List the virtual circuit record(s) associated with a particular interconnection id.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.virtual_circuit_list import VirtualCircuitList
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
    }
    try:
        # List a interconnection's virtual circuits
        api_response = api_instance.list_interconnection_virtual_circuits(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->list_interconnection_virtual_circuits: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_interconnection_virtual_circuits.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#list_interconnection_virtual_circuits.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#list_interconnection_virtual_circuits.ApiResponseFor404) | not found

#### list_interconnection_virtual_circuits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VirtualCircuitList**](../../models/VirtualCircuitList.md) |  | 


#### list_interconnection_virtual_circuits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### list_interconnection_virtual_circuits.ApiResponseFor404
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

# **organization_list_interconnections**
<a name="organization_list_interconnections"></a>
> InterconnectionList organization_list_interconnections(organization_id)

List organization connections

List the connections belonging to the organization

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_list import InterconnectionList
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'organization_id': "organization_id_example",
    }
    try:
        # List organization connections
        api_response = api_instance.organization_list_interconnections(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->organization_list_interconnections: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
organization_id | OrganizationIdSchema | | 

# OrganizationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#organization_list_interconnections.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#organization_list_interconnections.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#organization_list_interconnections.ApiResponseFor404) | not found

#### organization_list_interconnections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionList**](../../models/InterconnectionList.md) |  | 


#### organization_list_interconnections.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### organization_list_interconnections.ApiResponseFor404
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

# **project_list_interconnections**
<a name="project_list_interconnections"></a>
> InterconnectionList project_list_interconnections(project_id)

List project connections

List the connections belonging to the project

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_list import InterconnectionList
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': "project_id_example",
    }
    try:
        # List project connections
        api_response = api_instance.project_list_interconnections(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->project_list_interconnections: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#project_list_interconnections.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#project_list_interconnections.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#project_list_interconnections.ApiResponseFor404) | not found

#### project_list_interconnections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionList**](../../models/InterconnectionList.md) |  | 


#### project_list_interconnections.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### project_list_interconnections.ApiResponseFor404
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

# **update_interconnection**
<a name="update_interconnection"></a>
> Interconnection update_interconnection(connection_idinterconnection_update_input)

Update interconnection

Update the details of a interconnection

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.interconnection_update_input import InterconnectionUpdateInput
from metal.types.interconnection import Interconnection
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connection_id': "connection_id_example",
    }
    body = InterconnectionUpdateInput(
        contact_email="contact_email_example",
        description="description_example",
        mode="standard",
        name="name_example",
        redundancy="redundancy_example",
        tags=[
            "tags_example"
        ],
    )
    try:
        # Update interconnection
        api_response = api_instance.update_interconnection(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->update_interconnection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InterconnectionUpdateInput**](../../models/InterconnectionUpdateInput.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection_id | ConnectionIdSchema | | 

# ConnectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_interconnection.ApiResponseFor200) | ok
403 | [ApiResponseFor403](#update_interconnection.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#update_interconnection.ApiResponseFor404) | not found

#### update_interconnection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Interconnection**](../../models/Interconnection.md) |  | 


#### update_interconnection.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_interconnection.ApiResponseFor404
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

# **update_virtual_circuit**
<a name="update_virtual_circuit"></a>
> CreateInterconnectionPortVirtualCircuit201Response update_virtual_circuit(idupdate_virtual_circuit_request)

Update a virtual circuit

Update the details of a virtual circuit.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import interconnections_api
from metal.types.error import Error
from metal.types.create_interconnection_port_virtual_circuit201_response import CreateInterconnectionPortVirtualCircuit201Response
from metal.types.update_virtual_circuit_request import UpdateVirtualCircuitRequest
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
    api_instance = interconnections_api.InterconnectionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = UpdateVirtualCircuitRequest(None)
    try:
        # Update a virtual circuit
        api_response = api_instance.update_virtual_circuit(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling InterconnectionsApi->update_virtual_circuit: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateVirtualCircuitRequest**](../../models/UpdateVirtualCircuitRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_virtual_circuit.ApiResponseFor200) | ok
202 | [ApiResponseFor202](#update_virtual_circuit.ApiResponseFor202) | accepted
403 | [ApiResponseFor403](#update_virtual_circuit.ApiResponseFor403) | forbidden
404 | [ApiResponseFor404](#update_virtual_circuit.ApiResponseFor404) | not found

#### update_virtual_circuit.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInterconnectionPortVirtualCircuit201Response**](../../models/CreateInterconnectionPortVirtualCircuit201Response.md) |  | 


#### update_virtual_circuit.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInterconnectionPortVirtualCircuit201Response**](../../models/CreateInterconnectionPortVirtualCircuit201Response.md) |  | 


#### update_virtual_circuit.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_virtual_circuit.ApiResponseFor404
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

