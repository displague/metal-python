# InterconnectionCreateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**facility** | **str** | A Facility ID or code. | 
**metro** | **str** | A Metro ID or code. Required for creating a connection, unless creating with facility. | [optional] 
**type** | **str** | Either &#39;shared&#39; or &#39;dedicated&#39;. | 
**redundancy** | **str** | Either &#39;primary&#39; or &#39;redundant&#39;. | 
**contact_email** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**speed** | **str** | A connection speed, in bps, mbps, or gbps. Ex: &#39;100000000&#39; or &#39;100 mbps&#39;. | [optional] 
**tags** | **list[str]** |  | [optional] 
**mode** | **str** | The mode of the connection (only relevant to dedicated connections). Shared connections won&#39;t have this field. Can be either &#39;standard&#39; or &#39;tunnel&#39;.   The default mode of a dedicated connection is &#39;standard&#39;. The mode can only be changed when there are no associated virtual circuits on the connection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


