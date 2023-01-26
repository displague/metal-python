# BgpSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**default_route** | **bool** |  | [optional] 
**device** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**learned_routes** | **list[str]** |  | [optional] 
**status** | **str** |  The status of the BGP Session. Multiple status values may be reported when the device is connected to multiple switches, one value per switch. Each status will start with \&quot;unknown\&quot; and progress to \&quot;up\&quot; or \&quot;down\&quot; depending on the connected device. Subsequent \&quot;unknown\&quot; values indicate a problem acquiring status from the switch.  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


