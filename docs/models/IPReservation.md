# metal.types.ip_reservation.IPReservation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | must be one of ["global_ipv4", "public_ipv4", "private_ipv4", "public_ipv6", ] 
**addon** | bool,  | BoolClass,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**address_family** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[assignments](#assignments)** | list, tuple,  | tuple,  |  | [optional] 
**available** | str,  | str,  |  | [optional] 
**bill** | bool,  | BoolClass,  |  | [optional] 
**cidr** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**enabled** | bool,  | BoolClass,  |  | [optional] 
**details** | str,  | str,  |  | [optional] 
**facility** | [**IPReservationFacility**](IPReservationFacility.md) | [**IPReservationFacility**](IPReservationFacility.md) |  | [optional] 
**gateway** | str,  | str,  |  | [optional] 
**global_ip** | bool,  | BoolClass,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**manageable** | bool,  | BoolClass,  |  | [optional] 
**management** | bool,  | BoolClass,  |  | [optional] 
**metal_gateway** | [**MetalGatewayLite**](MetalGatewayLite.md) | [**MetalGatewayLite**](MetalGatewayLite.md) |  | [optional] 
**metro** | [**IPReservationMetro**](IPReservationMetro.md) | [**IPReservationMetro**](IPReservationMetro.md) |  | [optional] 
**netmask** | str,  | str,  |  | [optional] 
**network** | str,  | str,  |  | [optional] 
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**project_lite** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**requested_by** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**public** | bool,  | BoolClass,  |  | [optional] 
**state** | str,  | str,  |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 

# assignments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IPAssignment**](IPAssignment.md) | [**IPAssignment**](IPAssignment.md) | [**IPAssignment**](IPAssignment.md) |  | 

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

