# metal.types.capacity_check_per_metro_info.CapacityCheckPerMetroInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**available** | bool,  | BoolClass,  | Returns true if there is enough capacity in the metro to fulfill the quantity set. Returns false if there is not enough. | [optional] 
**metro** | str,  | str,  | The metro ID or code sent to check capacity. | [optional] 
**plan** | str,  | str,  | The plan ID or slug sent to check capacity. | [optional] 
**quantity** | str,  | str,  | The number of servers sent to check capacity. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

