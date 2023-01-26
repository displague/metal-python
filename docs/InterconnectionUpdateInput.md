# InterconnectionUpdateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mode** | **str** | The mode of the interconnection (only relevant to Dedicated Ports). Shared connections won&#39;t have this field. Can be either &#39;standard&#39; or &#39;tunnel&#39;.   The default mode of an interconnection on a Dedicated Port is &#39;standard&#39;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] 
**name** | **str** |  | [optional] 
**redundancy** | **str** | Updating from &#39;redundant&#39; to &#39;primary&#39; will remove a secondary port, while updating from &#39;primary&#39; to &#39;redundant&#39; will add one. | [optional] 
**tags** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


