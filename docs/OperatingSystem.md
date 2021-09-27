# OperatingSystem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**distro** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**preinstallable** | **bool** | Servers can be already preinstalled with OS in order to shorten provision time. | [optional] 
**provisionable_on** | **list[str]** |  | [optional] 
**pricing** | **object** | This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores) | [optional] 
**licensed** | **bool** | Licenced OS is priced according to pricing property | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


