# metal.types.payment_method.PaymentMethod

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**billing_address** | [**PaymentMethodBillingAddress**](PaymentMethodBillingAddress.md) | [**PaymentMethodBillingAddress**](PaymentMethodBillingAddress.md) |  | [optional] 
**card_type** | str,  | str,  |  | [optional] 
**cardholder_name** | str,  | str,  |  | [optional] 
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**created_by_user** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**default** | bool,  | BoolClass,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**expiration_month** | str,  | str,  |  | [optional] 
**expiration_year** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**name** | str,  | str,  |  | [optional] 
**organization** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**[projects](#projects)** | list, tuple,  | tuple,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

