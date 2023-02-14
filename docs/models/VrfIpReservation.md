# metal.types.vrf_ip_reservation.VrfIpReservation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vrf** | [**Vrf**](Vrf.md) | [**Vrf**](Vrf.md) |  | 
**type** | str,  | str,  |  | must be one of ["vrf", ] 
**address_family** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cidr** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**created_by** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**details** | str,  | str,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**metal_gateway** | [**MetalGatewayLite**](MetalGatewayLite.md) | [**MetalGatewayLite**](MetalGatewayLite.md) |  | [optional] 
**netmask** | str,  | str,  |  | [optional] 
**network** | str,  | str,  |  | [optional] 
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**state** | str,  | str,  |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**public** | bool,  | BoolClass,  |  | [optional] 
**management** | bool,  | BoolClass,  |  | [optional] 
**manageable** | bool,  | BoolClass,  |  | [optional] 
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**bill** | bool,  | BoolClass,  |  | [optional] 
**project_lite** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**gateway** | str,  | str,  |  | [optional] 
**metro** | [**Metro**](Metro.md) | [**Metro**](Metro.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

