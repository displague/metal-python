# InterconnectionPort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**role** | **str** | Either &#39;primary&#39; or &#39;secondary&#39;. | [optional] 
**status** | **str** | For both Fabric VCs and Dedicated Ports, this will be &#39;requested&#39; on creation and &#39;deleting&#39; on deletion. Once the Fabric VC has found its corresponding Fabric connection, this will turn to &#39;active&#39;. For Dedicated Ports, once the dedicated port is associated, this will also turn to &#39;active&#39;. For Fabric VCs, this can turn into an &#39;expired&#39; state if the service token associated is expired. | [optional] 
**switch_id** | **str** | A switch &#39;short ID&#39; | [optional] 
**virtual_circuits** | [**VirtualCircuitList**](VirtualCircuitList.md) |  | [optional] 
**name** | **str** |  | [optional] 
**speed** | **int** |  | [optional] 
**link_status** | **str** |  | [optional] 
**href** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


