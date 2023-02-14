# metal.types.vrf_route.VrfRoute

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | The unique identifier for the newly-created resource | [optional] value must be a uuid
**status** | str,  | str,  | The status of the route. Potential values are \&quot;pending\&quot;, \&quot;active\&quot;, \&quot;deleting\&quot;, and \&quot;error\&quot;, representing various lifecycle states of the route and whether or not it has been successfully configured on the network | [optional] must be one of ["pending", "active", "deleting", "error", ] 
**prefix** | str,  | str,  | The IPv4 prefix for the route, in CIDR-style notation | [optional] 
**next_hop** | str,  | str,  | The next-hop IPv4 address for the route | [optional] 
**type** | str,  | str,  | VRF route type, like &#x27;bgp&#x27;, &#x27;connected&#x27;, and &#x27;static&#x27;. Currently, only static routes are supported | [optional] must be one of ["static", ] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**metal_gateway** | [**VrfRouteMetalGateway**](VrfRouteMetalGateway.md) | [**VrfRouteMetalGateway**](VrfRouteMetalGateway.md) |  | [optional] 
**virtual_network** | [**VrfRouteVirtualNetwork**](VrfRouteVirtualNetwork.md) | [**VrfRouteVirtualNetwork**](VrfRouteVirtualNetwork.md) |  | [optional] 
**vrf** | [**VrfRouteVrf**](VrfRouteVrf.md) | [**VrfRouteVrf**](VrfRouteVrf.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

