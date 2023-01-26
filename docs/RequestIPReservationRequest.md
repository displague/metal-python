# RequestIPReservationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** |  | [optional] 
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**facility** | **str** |  | [optional] 
**fail_on_approval_required** | **bool** |  | [optional] 
**metro** | **str** | The code of the metro you are requesting the IP reservation in. | [optional] 
**quantity** | **int** |  | 
**tags** | **list[str]** |  | [optional] 
**type** | **str** | Must be set to &#39;vrf&#39; | 
**cidr** | **int** | The size of the VRF IP Reservation&#39;s subnet | 
**network** | **str** | The starting address for this VRF IP Reservation&#39;s subnet | 
**vrf_id** | **str** | The ID of the VRF in which this VRF IP Reservation is created. The VRF must have an existing IP Range that contains the requested subnet. This field may be aliased as just &#39;vrf&#39;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


