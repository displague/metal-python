# metal.types.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**avatar_thumb_url** | str,  | str,  |  | [optional] 
**avatar_url** | str,  | str,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**[emails](#emails)** | list, tuple,  | tuple,  |  | [optional] 
**first_name** | str,  | str,  |  | [optional] 
**fraud_score** | str,  | str,  |  | [optional] 
**full_name** | str,  | str,  |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**last_login_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**last_name** | str,  | str,  |  | [optional] 
**max_organizations** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**max_projects** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**phone_number** | str,  | str,  |  | [optional] 
**short_id** | str,  | str,  |  | [optional] 
**timezone** | str,  | str,  |  | [optional] 
**two_factor_auth** | str,  | str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# emails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

