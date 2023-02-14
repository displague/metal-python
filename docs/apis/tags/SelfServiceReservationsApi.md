<a name="__pageTop"></a>
# metal.models.tags.self_service_reservations_api.SelfServiceReservationsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_self_service_reservation**](#create_self_service_reservation) | **post** /projects/{project_id}/self-service/reservations | Create a reservation
[**find_self_service_reservation**](#find_self_service_reservation) | **get** /projects/{project_id}/self-service/reservations/{id} | Retrieve a reservation
[**find_self_service_reservations**](#find_self_service_reservations) | **get** /projects/{project_id}/self-service/reservations | Retrieve all reservations

# **create_self_service_reservation**
<a name="create_self_service_reservation"></a>
> SelfServiceReservationResponse create_self_service_reservation(project_idcreate_self_service_reservation_request)

Create a reservation

Creates a reservation.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import self_service_reservations_api
from metal.types.error import Error
from metal.types.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from metal.types.self_service_reservation_response import SelfServiceReservationResponse
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
    api_instance = self_service_reservations_api.SelfServiceReservationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': "project_id_example",
    }
    body = CreateSelfServiceReservationRequest(
        item=[
            SelfServiceReservationItemRequest(
                amount=3.14,
                metro_id="metro_id_example",
                plan_id="plan_id_example",
                quantity=1,
                term="term_example",
            )
        ],
        notes="notes_example",
        period=CreateSelfServiceReservationRequestPeriod(
            count=12,
            unit="monthly",
        ),
        start_date="1970-01-01T00:00:00.00Z",
    )
    try:
        # Create a reservation
        api_response = api_instance.create_self_service_reservation(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling SelfServiceReservationsApi->create_self_service_reservation: %s\n" % e)
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
[**CreateSelfServiceReservationRequest**](../../models/CreateSelfServiceReservationRequest.md) |  | 


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
201 | [ApiResponseFor201](#create_self_service_reservation.ApiResponseFor201) | created
401 | [ApiResponseFor401](#create_self_service_reservation.ApiResponseFor401) | unauthorized
422 | [ApiResponseFor422](#create_self_service_reservation.ApiResponseFor422) | unprocessable entity

#### create_self_service_reservation.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SelfServiceReservationResponse**](../../models/SelfServiceReservationResponse.md) |  | 


#### create_self_service_reservation.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_self_service_reservation.ApiResponseFor422
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

# **find_self_service_reservation**
<a name="find_self_service_reservation"></a>
> SelfServiceReservationResponse find_self_service_reservation(idproject_id)

Retrieve a reservation

Returns a reservation

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import self_service_reservations_api
from metal.types.error import Error
from metal.types.self_service_reservation_response import SelfServiceReservationResponse
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
    api_instance = self_service_reservations_api.SelfServiceReservationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'project_id': "project_id_example",
    }
    try:
        # Retrieve a reservation
        api_response = api_instance.find_self_service_reservation(
            path_params=path_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling SelfServiceReservationsApi->find_self_service_reservation: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_self_service_reservation.ApiResponseFor200) | ok
401 | [ApiResponseFor401](#find_self_service_reservation.ApiResponseFor401) | unauthorized
404 | [ApiResponseFor404](#find_self_service_reservation.ApiResponseFor404) | not found

#### find_self_service_reservation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SelfServiceReservationResponse**](../../models/SelfServiceReservationResponse.md) |  | 


#### find_self_service_reservation.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### find_self_service_reservation.ApiResponseFor404
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

# **find_self_service_reservations**
<a name="find_self_service_reservations"></a>
> SelfServiceReservationList find_self_service_reservations(project_id)

Retrieve all reservations

Returns all reservations.

### Example

* Api Key Authentication (x_auth_token):
```python
import metal
from metal.models.tags import self_service_reservations_api
from metal.types.error import Error
from metal.types.self_service_reservation_list import SelfServiceReservationList
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
    api_instance = self_service_reservations_api.SelfServiceReservationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': "project_id_example",
    }
    query_params = {
    }
    try:
        # Retrieve all reservations
        api_response = api_instance.find_self_service_reservations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling SelfServiceReservationsApi->find_self_service_reservations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'project_id': "project_id_example",
    }
    query_params = {
        'page': 1,
        'per_page': 10,
    }
    try:
        # Retrieve all reservations
        api_response = api_instance.find_self_service_reservations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except metal.ApiException as e:
        print("Exception when calling SelfServiceReservationsApi->find_self_service_reservations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
per_page | PerPageSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

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
200 | [ApiResponseFor200](#find_self_service_reservations.ApiResponseFor200) | ok
401 | [ApiResponseFor401](#find_self_service_reservations.ApiResponseFor401) | unauthorized

#### find_self_service_reservations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SelfServiceReservationList**](../../models/SelfServiceReservationList.md) |  | 


#### find_self_service_reservations.ApiResponseFor401
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

