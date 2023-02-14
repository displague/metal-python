# metal.types.plan_specs.PlanSpecs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[cpus](#cpus)** | list, tuple,  | tuple,  |  | [optional] 
**[drives](#drives)** | list, tuple,  | tuple,  |  | [optional] 
**[nics](#nics)** | list, tuple,  | tuple,  |  | [optional] 
**features** | [**PlanSpecsFeatures**](PlanSpecsFeatures.md) | [**PlanSpecsFeatures**](PlanSpecsFeatures.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cpus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlanSpecsCpusInner**](PlanSpecsCpusInner.md) | [**PlanSpecsCpusInner**](PlanSpecsCpusInner.md) | [**PlanSpecsCpusInner**](PlanSpecsCpusInner.md) |  | 

# drives

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlanSpecsDrivesInner**](PlanSpecsDrivesInner.md) | [**PlanSpecsDrivesInner**](PlanSpecsDrivesInner.md) | [**PlanSpecsDrivesInner**](PlanSpecsDrivesInner.md) |  | 

# nics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlanSpecsNicsInner**](PlanSpecsNicsInner.md) | [**PlanSpecsNicsInner**](PlanSpecsNicsInner.md) | [**PlanSpecsNicsInner**](PlanSpecsNicsInner.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

