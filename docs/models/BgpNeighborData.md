# metal.types.bgp_neighbor_data.BgpNeighborData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address_family** | decimal.Decimal, int, float,  | decimal.Decimal,  | Address Family for IP Address. Accepted values are 4 or 6 | [optional] 
**customer_as** | decimal.Decimal, int, float,  | decimal.Decimal,  | The customer&#x27;s ASN. In a local BGP deployment, this will be an internal ASN used to route within the data center. For a global BGP deployment, this will be the your own ASN, configured when you set up BGP for your project. | [optional] 
**customer_ip** | str,  | str,  | The device&#x27;s IP address. For an IPv4 BGP session, this is typically the private bond0 address for the device. | [optional] 
**md5_enabled** | bool,  | BoolClass,  | True if an MD5 password is configured for the project. | [optional] 
**md5_password** | str,  | str,  | The MD5 password configured for the project, if set. | [optional] 
**multihop** | bool,  | BoolClass,  | True when the BGP session should be configured as multihop. | [optional] 
**peer_as** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Peer ASN to use when configuring BGP on your device. | [optional] 
**[peer_ips](#peer_ips)** | list, tuple,  | tuple,  | A list of one or more IP addresses to use for the Peer IP section of your BGP configuration. For non-multihop sessions, this will typically be a single gateway address for the device. For multihop sessions, it will be a list of IPs. | [optional] 
**[routes_in](#routes_in)** | list, tuple,  | tuple,  | A list of project subnets | [optional] 
**[routes_out](#routes_out)** | list, tuple,  | tuple,  | A list of outgoing routes. Only populated if the BGP session has default route enabled. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# peer_ips

A list of one or more IP addresses to use for the Peer IP section of your BGP configuration. For non-multihop sessions, this will typically be a single gateway address for the device. For multihop sessions, it will be a list of IPs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of one or more IP addresses to use for the Peer IP section of your BGP configuration. For non-multihop sessions, this will typically be a single gateway address for the device. For multihop sessions, it will be a list of IPs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# routes_in

A list of project subnets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of project subnets | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BgpRoute**](BgpRoute.md) | [**BgpRoute**](BgpRoute.md) | [**BgpRoute**](BgpRoute.md) |  | 

# routes_out

A list of outgoing routes. Only populated if the BGP session has default route enabled.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of outgoing routes. Only populated if the BGP session has default route enabled. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BgpRoute**](BgpRoute.md) | [**BgpRoute**](BgpRoute.md) | [**BgpRoute**](BgpRoute.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

