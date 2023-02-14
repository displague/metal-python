# metal.types.ip_reservation_metro.IPReservationMetro

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Metro](Metro.md) | [**Metro**](Metro.md) | [**Metro**](Metro.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The metro the IP reservation is in. As long as the IP reservation has a metro, it can be used on a metro level. Can be null if requesting an IP reservation in a facility that is not in a metro. | 

# all_of_1

The metro the IP reservation is in. As long as the IP reservation has a metro, it can be used on a metro level. Can be null if requesting an IP reservation in a facility that is not in a metro.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The metro the IP reservation is in. As long as the IP reservation has a metro, it can be used on a metro level. Can be null if requesting an IP reservation in a facility that is not in a metro. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

