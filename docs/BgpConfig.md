# BgpConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** | Status of the BGP Config. Status \&quot;requested\&quot; is valid only with the \&quot;global\&quot; deployment_type. | [optional] 
**deployment_type** | **str** | In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space.  | [optional] 
**asn** | **int** | Autonomous System Number. ASN is required with Global BGP. With Local BGP the private ASN, 65000, is assigned. | [optional] 
**route_object** | **str** | Specifies AS-MACRO (aka AS-SET) to use when building client route filters | [optional] 
**md5** | **str** | (Optional) Password for BGP session in plaintext (not a checksum) | [optional] 
**max_prefix** | **int** | The maximum number of route filters allowed per server | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**requested_at** | **datetime** |  | [optional] 
**sessions** | [**list[BgpSession]**](BgpSession.md) | The direct connections between neighboring routers that want to exchange routing information. | [optional] 
**ranges** | [**list[GlobalBgpRange]**](GlobalBgpRange.md) | The IP block ranges associated to the ASN (Populated in Global BGP only) | [optional] 
**href** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


