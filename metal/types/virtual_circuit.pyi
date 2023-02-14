# coding: utf-8

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://metal.equinix.com/developers/api>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. The fields available for search differ by resource, as does the search strategy.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from metal import schemas  # noqa: F401


class VirtualCircuit(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "virtual_network",
            "nni_vlan",
            "vnid",
            "port",
            "name",
            "bill",
            "description",
            "project",
            "id",
            "status",
            "tags",
        }
        
        class properties:
            bill = schemas.BoolSchema
            description = schemas.StrSchema
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            nni_vlan = schemas.IntSchema
        
            @staticmethod
            def port() -> typing.Type['Href']:
                return Href
        
            @staticmethod
            def project() -> typing.Type['Href']:
                return Href
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def WAITING_ON_CUSTOMER_VLAN(cls):
                    return cls("waiting_on_customer_vlan")
                
                @schemas.classproperty
                def ACTIVATING(cls):
                    return cls("activating")
                
                @schemas.classproperty
                def CHANGING_VLAN(cls):
                    return cls("changing_vlan")
                
                @schemas.classproperty
                def DEACTIVATING(cls):
                    return cls("deactivating")
                
                @schemas.classproperty
                def DELETING(cls):
                    return cls("deleting")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("expired")
                
                @schemas.classproperty
                def ACTIVATION_FAILED(cls):
                    return cls("activation_failed")
                
                @schemas.classproperty
                def CHANGING_VLAN_FAILED(cls):
                    return cls("changing_vlan_failed")
                
                @schemas.classproperty
                def DEACTIVATION_FAILED(cls):
                    return cls("deactivation_failed")
                
                @schemas.classproperty
                def DELETE_FAILED(cls):
                    return cls("delete_failed")
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def virtual_network() -> typing.Type['Href']:
                return Href
            vnid = schemas.IntSchema
            speed = schemas.IntSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "bill": bill,
                "description": description,
                "id": id,
                "name": name,
                "nni_vlan": nni_vlan,
                "port": port,
                "project": project,
                "status": status,
                "tags": tags,
                "virtual_network": virtual_network,
                "vnid": vnid,
                "speed": speed,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    virtual_network: 'Href'
    nni_vlan: MetaOapg.properties.nni_vlan
    vnid: MetaOapg.properties.vnid
    port: 'Href'
    name: MetaOapg.properties.name
    bill: MetaOapg.properties.bill
    description: MetaOapg.properties.description
    project: 'Href'
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    tags: MetaOapg.properties.tags
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bill"]) -> MetaOapg.properties.bill: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nni_vlan"]) -> MetaOapg.properties.nni_vlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> 'Href': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> 'Href': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virtual_network"]) -> 'Href': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vnid"]) -> MetaOapg.properties.vnid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["speed"]) -> MetaOapg.properties.speed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bill", "description", "id", "name", "nni_vlan", "port", "project", "status", "tags", "virtual_network", "vnid", "speed", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bill"]) -> MetaOapg.properties.bill: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nni_vlan"]) -> MetaOapg.properties.nni_vlan: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> 'Href': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> 'Href': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virtual_network"]) -> 'Href': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vnid"]) -> MetaOapg.properties.vnid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["speed"]) -> typing.Union[MetaOapg.properties.speed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bill", "description", "id", "name", "nni_vlan", "port", "project", "status", "tags", "virtual_network", "vnid", "speed", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        virtual_network: 'Href',
        nni_vlan: typing.Union[MetaOapg.properties.nni_vlan, decimal.Decimal, int, ],
        vnid: typing.Union[MetaOapg.properties.vnid, decimal.Decimal, int, ],
        port: 'Href',
        name: typing.Union[MetaOapg.properties.name, str, ],
        bill: typing.Union[MetaOapg.properties.bill, bool, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        project: 'Href',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, ],
        speed: typing.Union[MetaOapg.properties.speed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VirtualCircuit':
        return super().__new__(
            cls,
            *_args,
            virtual_network=virtual_network,
            nni_vlan=nni_vlan,
            vnid=vnid,
            port=port,
            name=name,
            bill=bill,
            description=description,
            project=project,
            id=id,
            status=status,
            tags=tags,
            speed=speed,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from metal.types.href import Href
