# metal.types.spot_market_request.SpotMarketRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**devices_max** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**devices_min** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**end_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**facilities** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**instances** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**max_bid_price** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**metro** | [**SpotMarketRequestMetro**](SpotMarketRequestMetro.md) | [**SpotMarketRequestMetro**](SpotMarketRequestMetro.md) |  | [optional] 
**project** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

