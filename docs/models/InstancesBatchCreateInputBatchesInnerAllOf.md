# metal.types.instances_batch_create_input_batches_inner_all_of.InstancesBatchCreateInputBatchesInnerAllOf

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[hostnames](#hostnames)** | list, tuple,  | tuple,  |  | [optional] 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | The number of devices to create in this batch. The hostname may contain an &#x60;{{index}}&#x60; placeholder, which will be replaced with the index of the device in the batch. For example, if the hostname is &#x60;device-{{index}}&#x60;, the first device in the batch will have the hostname &#x60;device-01&#x60;, the second device will have the hostname &#x60;device-02&#x60;, and so on. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hostnames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

