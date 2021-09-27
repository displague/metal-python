# HardwareReservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**short_id** | **str** | Short version of the ID. | [optional] 
**facility** | [**Facility**](Facility.md) |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**href** | **str** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**device** | [**Device**](Device.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**spare** | **bool** | Whether the Hardware Reservation is a spare. Spare Hardware Reservations are used when a Hardware Reservations requires service from Metal Equinix | [optional] 
**need_of_service** | **bool** | Whether this Device requires assistance from Metal Equinix. | [optional] 
**provisionable** | **bool** | Whether the reserved server is provisionable or not. Spare devices can&#39;t be provisioned unless they are activated first. | [optional] 
**custom_rate** | **float** | Amount that will be charged for every billing_cycle. | [optional] 
**switch_uuid** | **str** | Switch short id. This can be used to determine if two devices are connected to the same switch, for example. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


