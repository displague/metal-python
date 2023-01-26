# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal. The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account.  The official API docs are hosted at <https://metal.equinix.com/developers/api>.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from metal.api_client import ApiClient
from metal.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MembershipsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_membership(self, id, **kwargs):  # noqa: E501
        """Delete the membership  # noqa: E501

        Deletes the membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_membership(id, async_req=True)
        >>> result = thread.get()

        :param id: Membership UUID (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_membership_with_http_info(id, **kwargs)  # noqa: E501

    def delete_membership_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete the membership  # noqa: E501

        Deletes the membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_membership_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: Membership UUID (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_membership" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and local_var_params.get('id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_membership`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x_auth_token']  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            '/memberships/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def find_membership_by_id(self, id, **kwargs):  # noqa: E501
        """Retrieve a membership  # noqa: E501

        Returns a single membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_membership_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: Membership UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: list[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Membership
        """
        kwargs['_return_http_data_only'] = True
        return self.find_membership_by_id_with_http_info(id, **kwargs)  # noqa: E501

    def find_membership_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a membership  # noqa: E501

        Returns a single membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_membership_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: Membership UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: list[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Membership, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id',
            'include',
            'exclude'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_membership_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and local_var_params.get('id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `find_membership_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if local_var_params.get('include') is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
            collection_formats['include'] = 'csv'  # noqa: E501
        if local_var_params.get('exclude') is not None:  # noqa: E501
            query_params.append(('exclude', local_var_params['exclude']))  # noqa: E501
            collection_formats['exclude'] = 'csv'  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x_auth_token']  # noqa: E501

        response_types_map = {
            200: "Membership",
            401: "Error",
            403: "Error",
            404: "Error",
        }

        return self.api_client.call_api(
            '/memberships/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def find_project_memberships(self, project_id, **kwargs):  # noqa: E501
        """Retrieve project memberships  # noqa: E501

        Returns all memberships in a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_project_memberships(project_id, async_req=True)
        >>> result = thread.get()

        :param project_id: Project UUID (required)
        :type project_id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: list[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: list[str]
        :param page: Page to return
        :type page: int
        :param per_page: Items returned per page
        :type per_page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MembershipList
        """
        kwargs['_return_http_data_only'] = True
        return self.find_project_memberships_with_http_info(project_id, **kwargs)  # noqa: E501

    def find_project_memberships_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Retrieve project memberships  # noqa: E501

        Returns all memberships in a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_project_memberships_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param project_id: Project UUID (required)
        :type project_id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: list[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: list[str]
        :param page: Page to return
        :type page: int
        :param per_page: Items returned per page
        :type per_page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MembershipList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'include',
            'exclude',
            'page',
            'per_page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_project_memberships" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and local_var_params.get('project_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `find_project_memberships`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > 100000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `find_project_memberships`, must be a value less than or equal to `100000`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `find_project_memberships`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `find_project_memberships`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `find_project_memberships`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']  # noqa: E501

        query_params = []
        if local_var_params.get('include') is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
            collection_formats['include'] = 'csv'  # noqa: E501
        if local_var_params.get('exclude') is not None:  # noqa: E501
            query_params.append(('exclude', local_var_params['exclude']))  # noqa: E501
            collection_formats['exclude'] = 'csv'  # noqa: E501
        if local_var_params.get('page') is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if local_var_params.get('per_page') is not None:  # noqa: E501
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x_auth_token']  # noqa: E501

        response_types_map = {
            200: "MembershipList",
            401: "Error",
            403: "Error",
            404: "Error",
        }

        return self.api_client.call_api(
            '/projects/{project_id}/memberships', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_membership(self, id, membership, **kwargs):  # noqa: E501
        """Update the membership  # noqa: E501

        Updates the membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_membership(id, membership, async_req=True)
        >>> result = thread.get()

        :param id: Membership UUID (required)
        :type id: str
        :param membership: Membership to update (required)
        :type membership: MembershipInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Membership
        """
        kwargs['_return_http_data_only'] = True
        return self.update_membership_with_http_info(id, membership, **kwargs)  # noqa: E501

    def update_membership_with_http_info(self, id, membership, **kwargs):  # noqa: E501
        """Update the membership  # noqa: E501

        Updates the membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_membership_with_http_info(id, membership, async_req=True)
        >>> result = thread.get()

        :param id: Membership UUID (required)
        :type id: str
        :param membership: Membership to update (required)
        :type membership: MembershipInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Membership, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id',
            'membership'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_membership" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and local_var_params.get('id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_membership`")  # noqa: E501
        # verify the required parameter 'membership' is set
        if self.api_client.client_side_validation and local_var_params.get('membership') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `membership` when calling `update_membership`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'membership' in local_var_params:
            body_params = local_var_params['membership']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'PUT', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['x_auth_token']  # noqa: E501

        response_types_map = {
            200: "Membership",
            401: "Error",
            403: "Error",
            404: "Error",
            422: "Error",
        }

        return self.api_client.call_api(
            '/memberships/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
