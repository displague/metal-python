# metal.types.plan.Plan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[available_in](#available_in)** | list, tuple,  | tuple,  | Shows which facilities the plan is available in, and the facility-based price if it is different from the default price. | [optional] 
**[available_in_metros](#available_in_metros)** | list, tuple,  | tuple,  | Shows which metros the plan is available in, and the metro-based price if it is different from the default price. | [optional] 
**class** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[deployment_types](#deployment_types)** | list, tuple,  | tuple,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**legacy** | bool,  | BoolClass,  |  | [optional] 
**line** | str,  | str,  |  | [optional] must be one of ["baremetal", ] 
**name** | str,  | str,  |  | [optional] 
**[pricing](#pricing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**specs** | [**PlanSpecs**](PlanSpecs.md) | [**PlanSpecs**](PlanSpecs.md) |  | [optional] 
**type** | str,  | str,  | The plan type | [optional] must be one of ["standard", "workload_optimized", "custom", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# available_in

Shows which facilities the plan is available in, and the facility-based price if it is different from the default price.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Shows which facilities the plan is available in, and the facility-based price if it is different from the default price. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlanAvailableInInner**](PlanAvailableInInner.md) | [**PlanAvailableInInner**](PlanAvailableInInner.md) | [**PlanAvailableInInner**](PlanAvailableInInner.md) |  | 

# available_in_metros

Shows which metros the plan is available in, and the metro-based price if it is different from the default price.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Shows which metros the plan is available in, and the metro-based price if it is different from the default price. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlanAvailableInMetrosInner**](PlanAvailableInMetrosInner.md) | [**PlanAvailableInMetrosInner**](PlanAvailableInMetrosInner.md) | [**PlanAvailableInMetrosInner**](PlanAvailableInMetrosInner.md) |  | 

# deployment_types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["on_demand", "spot_market", ] 

# pricing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

