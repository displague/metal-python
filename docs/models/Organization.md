# metal.types.organization.Organization

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) | [**Address**](Address.md) |  | [optional] 
**billing_address** | [**Address**](Address.md) | [**Address**](Address.md) |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**credit_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**[customdata](#customdata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**enforce_2fa_at** | str, datetime,  | str,  | Force to all members to have enabled the two factor authentication after that date, unless the value is null | [optional] value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**logo** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**[members](#members)** | list, tuple,  | tuple,  |  | [optional] 
**[memberships](#memberships)** | list, tuple,  | tuple,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**[projects](#projects)** | list, tuple,  | tuple,  |  | [optional] 
**terms** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**twitter** | str,  | str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**website** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customdata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# members

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

# memberships

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

# projects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Href**](Href.md) | [**Href**](Href.md) | [**Href**](Href.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

