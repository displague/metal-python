# metal.types.virtual_network.VirtualNetwork

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assigned_to** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**assigned_to_virtual_circuit** | bool,  | BoolClass,  | True if the virtual network is attached to a virtual circuit. False if not. | [optional] 
**description** | str,  | str,  |  | [optional] 
**facility** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**[instances](#instances)** | list, tuple,  | tuple,  | A list of instances with ports currently associated to this Virtual Network. | [optional] 
**[metal_gateways](#metal_gateways)** | list, tuple,  | tuple,  | A list of metal gateways currently associated to this Virtual Network. | [optional] 
**metro** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**metro_code** | str,  | str,  | The Metro code of the metro in which this Virtual Network is defined. | [optional] 
**vxlan** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instances

A list of instances with ports currently associated to this Virtual Network.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of instances with ports currently associated to this Virtual Network. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

# metal_gateways

A list of metal gateways currently associated to this Virtual Network.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of metal gateways currently associated to this Virtual Network. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MetalGatewayLite**](MetalGatewayLite.md) | [**MetalGatewayLite**](MetalGatewayLite.md) | [**MetalGatewayLite**](MetalGatewayLite.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

