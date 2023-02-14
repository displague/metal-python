# metal.types.entitlement.Entitlement

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**weight** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**slug** | str,  | str,  |  | 
**description** | str,  | str,  |  | [optional] 
**[feature_access](#feature_access)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**[instance_quota](#instance_quota)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[ip_quota](#ip_quota)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**project_quota** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**[volume_limits](#volume_limits)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[volume_quota](#volume_quota)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# feature_access

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# instance_quota

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# ip_quota

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# volume_limits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# volume_quota

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

