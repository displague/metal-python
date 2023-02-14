# metal.types.facility.Facility

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) | [**Address**](Address.md) |  | [optional] 
**code** | str,  | str,  |  | [optional] 
**[features](#features)** | list, tuple,  | tuple,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**[ip_ranges](#ip_ranges)** | list, tuple,  | tuple,  | IP ranges registered in facility. Can be used for GeoIP location | [optional] 
**metro** | [**DeviceMetro**](DeviceMetro.md) | [**DeviceMetro**](DeviceMetro.md) |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# features

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["baremetal", "backend_transfer", "layer_2", "global_ipv4", "ibx", ] 

# ip_ranges

IP ranges registered in facility. Can be used for GeoIP location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | IP ranges registered in facility. Can be used for GeoIP location | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

