# metal.types.spot_market_request_create_input.SpotMarketRequestCreateInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**devices_max** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**devices_min** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**end_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[facilities](#facilities)** | list, tuple,  | tuple,  |  | [optional] 
**instance_attributes** | [**SpotMarketRequestCreateInputInstanceAttributes**](SpotMarketRequestCreateInputInstanceAttributes.md) | [**SpotMarketRequestCreateInputInstanceAttributes**](SpotMarketRequestCreateInputInstanceAttributes.md) |  | [optional] 
**max_bid_price** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**metro** | str,  | str,  | The metro ID or code the spot market request will be created in. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# facilities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

