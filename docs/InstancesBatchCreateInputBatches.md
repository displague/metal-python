# InstancesBatchCreateInputBatches


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**hostnames** | **list[str]** |  | [optional] 
**facility** | **list[str]** | Array of facility codes the batch can use for provisioning. This param also takes a string if you want the batch to be fulfilled in only one facility. Cannot be set if the metro is already set. | [optional] 
**metro** | **str** | The metro ID or code the batch can use for provisioning. Cannot be set if the facility is already set. | [optional] 
**description** | **str** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**always_pxe** | **bool** |  | [optional] 
**userdata** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**termination_time** | **datetime** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**project_ssh_keys** | **list[str]** |  | [optional] 
**user_ssh_keys** | **list[str]** | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] 
**no_ssh_keys** | **bool** |  | [optional] 
**features** | **list[str]** |  | [optional] 
**customdata** | **object** |  | [optional] 
**ip_addresses** | [**list[InstancesBatchCreateInputIpAddresses]**](InstancesBatchCreateInputIpAddresses.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


