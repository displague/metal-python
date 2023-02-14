# metal.types.port_vlan_assignment.PortVlanAssignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**native** | bool,  | BoolClass,  |  | [optional] 
**port** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**state** | str,  | str,  |  | [optional] must be one of ["assigned", "unassigning", ] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**virtual_network** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**vlan** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

