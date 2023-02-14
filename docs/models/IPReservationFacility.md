# metal.types.ip_reservation_facility.IPReservationFacility

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Facility](Facility.md) | [**Facility**](Facility.md) | [**Facility**](Facility.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The facility the IP reservation is in. If the facility the IP reservation was requested in is in a metro, a metro value will also be set, and the subsequent IP reservation can be used on a metro level. Can be null if requesting an IP reservation in a metro. | 

# all_of_1

The facility the IP reservation is in. If the facility the IP reservation was requested in is in a metro, a metro value will also be set, and the subsequent IP reservation can be used on a metro level. Can be null if requesting an IP reservation in a metro.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The facility the IP reservation is in. If the facility the IP reservation was requested in is in a metro, a metro value will also be set, and the subsequent IP reservation can be used on a metro level. Can be null if requesting an IP reservation in a metro. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

