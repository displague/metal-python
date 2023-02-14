# metal.types.create_self_service_reservation_request.CreateSelfServiceReservationRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[item](#item)** | list, tuple,  | tuple,  |  | [optional] 
**notes** | str,  | str,  |  | [optional] 
**period** | [**CreateSelfServiceReservationRequestPeriod**](CreateSelfServiceReservationRequestPeriod.md) | [**CreateSelfServiceReservationRequestPeriod**](CreateSelfServiceReservationRequestPeriod.md) |  | [optional] 
**start_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SelfServiceReservationItemRequest**](SelfServiceReservationItemRequest.md) | [**SelfServiceReservationItemRequest**](SelfServiceReservationItemRequest.md) | [**SelfServiceReservationItemRequest**](SelfServiceReservationItemRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

