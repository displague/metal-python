# metal.types.bgp_session.BgpSession

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address_family** | str,  | str,  |  | must be one of ["ipv4", "ipv6", ] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**default_route** | bool,  | BoolClass,  |  | [optional] 
**device** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**[learned_routes](#learned_routes)** | list, tuple,  | tuple,  |  | [optional] 
**status** | str,  | str,  |  The status of the BGP Session. Multiple status values may be reported when the device is connected to multiple switches, one value per switch. Each status will start with \&quot;unknown\&quot; and progress to \&quot;up\&quot; or \&quot;down\&quot; depending on the connected device. Subsequent \&quot;unknown\&quot; values indicate a problem acquiring status from the switch.  | [optional] must be one of ["unknown", "up", "down", ] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# learned_routes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | IPv4 or IPv6 range | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

