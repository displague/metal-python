# metal.types.user_lite.UserLite

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | ID of the User | value must be a uuid
**short_id** | str,  | str,  | Short ID of the User | 
**avatar_thumb_url** | str,  | str,  | Avatar thumbnail URL of the User | [optional] 
**created_at** | str, datetime,  | str,  | When the user was created | [optional] value must conform to RFC-3339 date-time
**email** | str,  | str,  | Primary email address of the User | [optional] 
**first_name** | str,  | str,  | First name of the User | [optional] 
**full_name** | str,  | str,  | Full name of the User | [optional] 
**href** | str,  | str,  | API URL uniquely representing the User | [optional] 
**last_name** | str,  | str,  | Last name of the User | [optional] 
**updated_at** | str, datetime,  | str,  | When the user details were last updated | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

