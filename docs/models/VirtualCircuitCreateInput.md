# metal.types.virtual_circuit_create_input.VirtualCircuitCreateInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**project_id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**description** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**nni_vlan** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**speed** | decimal.Decimal, int,  | decimal.Decimal,  | speed can be passed as integer number representing bps speed or string (e.g. &#x27;52m&#x27; or &#x27;100g&#x27; or &#x27;4 gbps&#x27;) | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**vnid** | str, uuid.UUID,  | str,  | A Virtual Network record UUID or the VNID of a Metro Virtual Network in your project (sent as integer). | [optional] value must be a uuid
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

