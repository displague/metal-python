# VrfRoute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the newly-created resource | [optional] [readonly] 
**status** | **str** | The status of the route. Potential values are \&quot;pending\&quot;, \&quot;active\&quot;, \&quot;deleting\&quot;, and \&quot;error\&quot;, representing various lifecycle states of the route and whether or not it has been successfully configured on the network | [optional] [readonly] 
**prefix** | **str** | The IPv4 prefix for the route, in CIDR-style notation | [optional] 
**next_hop** | **str** | The next-hop IPv4 address for the route | [optional] 
**type** | **str** | VRF route type, like &#39;bgp&#39;, &#39;connected&#39;, and &#39;static&#39;. Currently, only static routes are supported | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**metal_gateway** | [**VrfRouteMetalGateway**](VrfRouteMetalGateway.md) |  | [optional] 
**virtual_network** | [**VrfRouteVirtualNetwork**](VrfRouteVirtualNetwork.md) |  | [optional] 
**vrf** | [**VrfRouteVrf**](VrfRouteVrf.md) |  | [optional] 
**href** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


