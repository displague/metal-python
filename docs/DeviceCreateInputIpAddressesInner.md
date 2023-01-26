# DeviceCreateInputIpAddressesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **float** | Address Family for IP Address | [optional] 
**cidr** | **float** | Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses) | [optional] 
**ip_reservations** | **list[str]** | UUIDs of any IP reservations to use when assigning IPs | [optional] 
**public** | **bool** | Address Type for IP Address | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


