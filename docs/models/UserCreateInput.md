# metal.types.user_create_input.UserCreateInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[emails](#emails)** | list, tuple,  | tuple,  |  | 
**last_name** | str,  | str,  |  | 
**first_name** | str,  | str,  |  | 
**avatar** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**company_name** | str,  | str,  |  | [optional] 
**company_url** | str,  | str,  |  | [optional] 
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**level** | str,  | str,  |  | [optional] 
**locked** | bool,  | BoolClass,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**phone_number** | str,  | str,  |  | [optional] 
**[social_accounts](#social_accounts)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**timezone** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**two_factor_auth** | str,  | str,  |  | [optional] 
**verified_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**invitation_id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**nonce** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# emails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EmailInput**](EmailInput.md) | [**EmailInput**](EmailInput.md) | [**EmailInput**](EmailInput.md) |  | 

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# social_accounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

