# Interconnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**redundancy** | **str** |  | [optional] 
**speed** | **int** | The connection&#39;s speed in bps. | [optional] 
**tags** | **list[str]** |  | [optional] 
**ports** | [**list[InterconnectionPort]**](InterconnectionPort.md) |  | [optional] 
**facility** | [**Href**](Href.md) |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**metro** | [**InterconnectionMetro**](InterconnectionMetro.md) |  | [optional] 
**mode** | **str** | The mode of the connection (only relevant to dedicated connections). Shared connections won&#39;t have this field. Can be either &#39;standard&#39; or &#39;tunnel&#39;.   The default mode of a dedicated connection is &#39;standard&#39;. The mode can only be changed when there are no associated virtual circuits on the connection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


