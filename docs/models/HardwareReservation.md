# metal.types.hardware_reservation.HardwareReservation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**custom_rate** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount that will be charged for every billing_cycle. | [optional] value must be a 32 bit float
**device** | [**Device**](Device.md) | [**Device**](Device.md) |  | [optional] 
**facility** | [**Facility**](Facility.md) | [**Facility**](Facility.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**need_of_service** | bool,  | BoolClass,  | Whether this Device requires assistance from Equinix Metal. | [optional] 
**plan** | [**Plan**](Plan.md) | [**Plan**](Plan.md) |  | [optional] 
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**provisionable** | bool,  | BoolClass,  | Whether the reserved server is provisionable or not. Spare devices can&#x27;t be provisioned unless they are activated first. | [optional] 
**short_id** | str,  | str,  | Short version of the ID. | [optional] 
**spare** | bool,  | BoolClass,  | Whether the Hardware Reservation is a spare. Spare Hardware Reservations are used when a Hardware Reservations requires service from Equinix Metal | [optional] 
**switch_uuid** | str,  | str,  | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 
**termination_time** | str, datetime,  | str,  | Expiration date for the reservation. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

