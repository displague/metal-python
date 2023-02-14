# metal.types.self_service_reservation_response.SelfServiceReservationResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[item](#item)** | list, tuple,  | tuple,  |  | [optional] 
**notes** | str,  | str,  |  | [optional] 
**organization** | str,  | str,  |  | [optional] 
**organization_id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**period** | [**CreateSelfServiceReservationRequestPeriod**](CreateSelfServiceReservationRequestPeriod.md) | [**CreateSelfServiceReservationRequestPeriod**](CreateSelfServiceReservationRequestPeriod.md) |  | [optional] 
**project** | str,  | str,  |  | [optional] 
**project_id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**start_date** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | [optional] 
**total_cost** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SelfServiceReservationItemResponse**](SelfServiceReservationItemResponse.md) | [**SelfServiceReservationItemResponse**](SelfServiceReservationItemResponse.md) | [**SelfServiceReservationItemResponse**](SelfServiceReservationItemResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

