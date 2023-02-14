# metal.types.vrf_metal_gateway.VrfMetalGateway

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**created_by** | [**Href**](Href.md) | [**Href**](Href.md) |  | [optional] 
**href** | str,  | str,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**ip_reservation** | [**VrfIpReservation**](VrfIpReservation.md) | [**VrfIpReservation**](VrfIpReservation.md) |  | [optional] 
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**state** | str,  | str,  | The current state of the Metal Gateway. &#x27;Ready&#x27; indicates the gateway record has been configured, but is currently not active on the network. &#x27;Active&#x27; indicates the gateway has been configured on the network. &#x27;Deleting&#x27; is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted. | [optional] must be one of ["ready", "active", "deleting", ] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) | [**Vrf**](Vrf.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

