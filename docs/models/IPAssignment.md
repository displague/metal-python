# metal.types.ip_assignment.IPAssignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  |  | [optional] 
**address_family** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**assigned_to** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**cidr** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**enabled** | bool,  | BoolClass,  |  | [optional] 
**gateway** | str,  | str,  |  | [optional] 
**global_ip** | bool,  | BoolClass,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**manageable** | bool,  | BoolClass,  |  | [optional] 
**management** | bool,  | BoolClass,  |  | [optional] 
**metro** | [**IPAssignmentMetro**](IPAssignmentMetro.md) | [**IPAssignmentMetro**](IPAssignmentMetro.md) |  | [optional] 
**netmask** | str,  | str,  |  | [optional] 
**network** | str,  | str,  |  | [optional] 
**parent_block** | [**ParentBlock**](ParentBlock.md) | [**ParentBlock**](ParentBlock.md) |  | [optional] 
**public** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

