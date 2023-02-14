# metal.types.device_create_input_ip_addresses_inner.DeviceCreateInputIpAddressesInner

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address_family** | decimal.Decimal, int, float,  | decimal.Decimal,  | Address Family for IP Address | [optional] must be one of [4, 6, ] 
**cidr** | decimal.Decimal, int, float,  | decimal.Decimal,  | Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses) | [optional] 
**[ip_reservations](#ip_reservations)** | list, tuple,  | tuple,  | UUIDs of any IP reservations to use when assigning IPs | [optional] 
**public** | bool,  | BoolClass,  | Address Type for IP Address | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ip_reservations

UUIDs of any IP reservations to use when assigning IPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | UUIDs of any IP reservations to use when assigning IPs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

