# metal.types.port_vlan_assignment_batch.PortVlanAssignmentBatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[error_messages](#error_messages)** | list, tuple,  | tuple,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**port** | [**Port**](Port.md) | [**Port**](Port.md) |  | [optional] 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**state** | str,  | str,  |  | [optional] must be one of ["queued", "in_progress", "completed", "failed", ] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[vlan_assignments](#vlan_assignments)** | list, tuple,  | tuple,  |  | [optional] 
**project** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error_messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# vlan_assignments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PortVlanAssignmentBatchVlanAssignmentsInner**](PortVlanAssignmentBatchVlanAssignmentsInner.md) | [**PortVlanAssignmentBatchVlanAssignmentsInner**](PortVlanAssignmentBatchVlanAssignmentsInner.md) | [**PortVlanAssignmentBatchVlanAssignmentsInner**](PortVlanAssignmentBatchVlanAssignmentsInner.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

