# coding: utf-8

"""
    Registry of Open Community Challenge API

    The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from roccclient.api_client import ApiClient
from roccclient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OrganizationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_organization(self, organization_id, **kwargs):  # noqa: E501
        """Create an organization  # noqa: E501

        Create an organization with the specified name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_organization(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: The ID of the organization that is being created (required)
        :type organization_id: str
        :param organization:
        :type organization: Organization
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
        :rtype: Organization
        """
        kwargs['_return_http_data_only'] = True
        return self.create_organization_with_http_info(organization_id, **kwargs)  # noqa: E501

    def create_organization_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Create an organization  # noqa: E501

        Create an organization with the specified name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_organization_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: The ID of the organization that is being created (required)
        :type organization_id: str
        :param organization:
        :type organization: Organization
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
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Organization, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'organization_id',
            'organization'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_organization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `create_organization`")  # noqa: E501

        if self.api_client.client_side_validation and ('organization_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['organization_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `create_organization`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('organization_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['organization_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `create_organization`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'organization_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['organization_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `create_organization`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in local_var_params and local_var_params['organization_id'] is not None:  # noqa: E501
            query_params.append(('organizationId', local_var_params['organization_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'organization' in local_var_params:
            body_params = local_var_params['organization']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/organizations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_organization(self, organization_id, **kwargs):  # noqa: E501
        """Delete an organization  # noqa: E501

        Deletes the organization specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_organization(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: The ID of the organization (required)
        :type organization_id: str
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
        :rtype: Organization
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_organization_with_http_info(organization_id, **kwargs)  # noqa: E501

    def delete_organization_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Delete an organization  # noqa: E501

        Deletes the organization specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_organization_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: The ID of the organization (required)
        :type organization_id: str
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
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Organization, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'organization_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_organization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `delete_organization`")  # noqa: E501

        if self.api_client.client_side_validation and ('organization_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['organization_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `delete_organization`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('organization_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['organization_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `delete_organization`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'organization_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['organization_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `delete_organization`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organizationId'] = local_var_params['organization_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organizationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_organization(self, organization_id, **kwargs):  # noqa: E501
        """Get an organization  # noqa: E501

        Returns the organization specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_organization(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: The ID of the organization (required)
        :type organization_id: str
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
        :rtype: Organization
        """
        kwargs['_return_http_data_only'] = True
        return self.get_organization_with_http_info(organization_id, **kwargs)  # noqa: E501

    def get_organization_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Get an organization  # noqa: E501

        Returns the organization specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_organization_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: The ID of the organization (required)
        :type organization_id: str
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
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Organization, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'organization_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `get_organization`")  # noqa: E501

        if self.api_client.client_side_validation and ('organization_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['organization_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `get_organization`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('organization_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['organization_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `get_organization`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'organization_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['organization_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `organization_id` when calling `get_organization`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organizationId'] = local_var_params['organization_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organizationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_organizations(self, **kwargs):  # noqa: E501
        """Get all organizations  # noqa: E501

        Returns the organizations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_organizations(async_req=True)
        >>> result = thread.get()

        :param limit: Maximum number of results returned
        :type limit: int
        :param offset: Index of the first result that must be returned
        :type offset: int
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
        :rtype: PageOfOrganizations
        """
        kwargs['_return_http_data_only'] = True
        return self.list_organizations_with_http_info(**kwargs)  # noqa: E501

    def list_organizations_with_http_info(self, **kwargs):  # noqa: E501
        """Get all organizations  # noqa: E501

        Returns the organizations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_organizations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: Maximum number of results returned
        :type limit: int
        :param offset: Index of the first result that must be returned
        :type offset: int
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
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PageOfOrganizations, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_organizations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_organizations`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_organizations`, must be a value greater than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `list_organizations`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/organizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfOrganizations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
