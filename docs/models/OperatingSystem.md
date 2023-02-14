# metal.types.operating_system.OperatingSystem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**distro** | str,  | str,  |  | [optional] 
**distro_label** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**licensed** | bool,  | BoolClass,  | Licenced OS is priced according to pricing property | [optional] 
**name** | str,  | str,  |  | [optional] 
**preinstallable** | bool,  | BoolClass,  | Servers can be already preinstalled with OS in order to shorten provision time. | [optional] 
**[pricing](#pricing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores) | [optional] 
**[provisionable_on](#provisionable_on)** | list, tuple,  | tuple,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pricing

This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores) | 

# provisionable_on

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

