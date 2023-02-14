# metal.types.spot_market_request_create_input_instance_attributes.SpotMarketRequestCreateInputInstanceAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**always_pxe** | bool,  | BoolClass,  |  | [optional] 
**billing_cycle** | str,  | str,  |  | [optional] 
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[features](#features)** | list, tuple,  | tuple,  |  | [optional] 
**hostname** | str,  | str,  |  | [optional] 
**[hostnames](#hostnames)** | list, tuple,  | tuple,  |  | [optional] 
**locked** | bool,  | BoolClass,  |  | [optional] 
**no_ssh_keys** | bool,  | BoolClass,  |  | [optional] 
**operating_system** | str,  | str,  |  | [optional] 
**plan** | str,  | str,  |  | [optional] 
**private_ipv4_subnet_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[project_ssh_keys](#project_ssh_keys)** | list, tuple,  | tuple,  |  | [optional] 
**public_ipv4_subnet_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**termination_time** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[user_ssh_keys](#user_ssh_keys)** | list, tuple,  | tuple,  | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] 
**userdata** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# features

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# hostnames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# project_ssh_keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# user_ssh_keys

The UUIDs of users whose SSH keys should be included on the provisioned device.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The UUIDs of users whose SSH keys should be included on the provisioned device. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

