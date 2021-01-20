"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from collibra_core.api_client import ApiClient, Endpoint
from collibra_core.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from collibra_core.model.add_user_group_request import AddUserGroupRequest
from collibra_core.model.add_users_to_user_group_request import AddUsersToUserGroupRequest
from collibra_core.model.change_user_group_request import ChangeUserGroupRequest
from collibra_core.model.remove_users_from_user_group_request import RemoveUsersFromUserGroupRequest
from collibra_core.model.user import User
from collibra_core.model.user_group_impl import UserGroupImpl
from collibra_core.model.user_group_paged_response import UserGroupPagedResponse


class UserGroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_user_group(
            self,
            **kwargs
        ):
            """Add new user group  # noqa: E501

            Adds a new user group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_user_group(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                add_user_group_request (AddUserGroupRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserGroupImpl
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.add_user_group = Endpoint(
            settings={
                'response_type': (UserGroupImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups',
                'operation_id': 'add_user_group',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'add_user_group_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'add_user_group_request':
                        (AddUserGroupRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'add_user_group_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__add_user_group
        )

        def __add_users_to_user_group(
            self,
            user_group_id,
            **kwargs
        ):
            """Add users to user group  # noqa: E501

            Adds users to an existing user group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_users_to_user_group(user_group_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_group_id (str): The ID of the user group

            Keyword Args:
                add_users_to_user_group_request (AddUsersToUserGroupRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [User]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_group_id'] = \
                user_group_id
            return self.call_with_http_info(**kwargs)

        self.add_users_to_user_group = Endpoint(
            settings={
                'response_type': ([User],),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups/{userGroupId}/users',
                'operation_id': 'add_users_to_user_group',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_group_id',
                    'add_users_to_user_group_request',
                ],
                'required': [
                    'user_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_group_id':
                        (str,),
                    'add_users_to_user_group_request':
                        (AddUsersToUserGroupRequest,),
                },
                'attribute_map': {
                    'user_group_id': 'userGroupId',
                },
                'location_map': {
                    'user_group_id': 'path',
                    'add_users_to_user_group_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__add_users_to_user_group
        )

        def __change_user_group(
            self,
            user_group_id,
            **kwargs
        ):
            """Change user group  # noqa: E501

            Changes the user group with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.change_user_group(user_group_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_group_id (str): The ID of the user group

            Keyword Args:
                change_user_group_request (ChangeUserGroupRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserGroupImpl
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_group_id'] = \
                user_group_id
            return self.call_with_http_info(**kwargs)

        self.change_user_group = Endpoint(
            settings={
                'response_type': (UserGroupImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups/{userGroupId}',
                'operation_id': 'change_user_group',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_group_id',
                    'change_user_group_request',
                ],
                'required': [
                    'user_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_group_id':
                        (str,),
                    'change_user_group_request':
                        (ChangeUserGroupRequest,),
                },
                'attribute_map': {
                    'user_group_id': 'userGroupId',
                },
                'location_map': {
                    'user_group_id': 'path',
                    'change_user_group_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__change_user_group
        )

        def __find_user_groups(
            self,
            **kwargs
        ):
            """Find user groups  # noqa: E501

            Returns user groups matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 user groups is returned.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_user_groups(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                name (str): The name of the user group.. [optional]
                name_match_mode (str): The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive.. [optional] if omitted the server will use the default value of "ANYWHERE"
                user_id (str): The ID of the user who should belong to searched user groups.. [optional]
                include_everyone (bool): Indicates if we should include the everyone group or not.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserGroupPagedResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.find_user_groups = Endpoint(
            settings={
                'response_type': (UserGroupPagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups',
                'operation_id': 'find_user_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'name',
                    'name_match_mode',
                    'user_id',
                    'include_everyone',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'name_match_mode',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('name_match_mode',): {

                        "START": "START",
                        "END": "END",
                        "ANYWHERE": "ANYWHERE",
                        "EXACT": "EXACT"
                    },
                },
                'openapi_types': {
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'name':
                        (str,),
                    'name_match_mode':
                        (str,),
                    'user_id':
                        (str,),
                    'include_everyone':
                        (bool,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'name': 'name',
                    'name_match_mode': 'nameMatchMode',
                    'user_id': 'userId',
                    'include_everyone': 'includeEveryone',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'name': 'query',
                    'name_match_mode': 'query',
                    'user_id': 'query',
                    'include_everyone': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__find_user_groups
        )

        def __get_user_group(
            self,
            user_group_id,
            **kwargs
        ):
            """Get user group  # noqa: E501

            Returns the user group with the given ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_user_group(user_group_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_group_id (str): The ID of the user group

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserGroupImpl
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_group_id'] = \
                user_group_id
            return self.call_with_http_info(**kwargs)

        self.get_user_group = Endpoint(
            settings={
                'response_type': (UserGroupImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups/{userGroupId}',
                'operation_id': 'get_user_group',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_group_id',
                ],
                'required': [
                    'user_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_group_id':
                        (str,),
                },
                'attribute_map': {
                    'user_group_id': 'userGroupId',
                },
                'location_map': {
                    'user_group_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_user_group
        )

        def __remove_user_group(
            self,
            user_group_id,
            **kwargs
        ):
            """Remove user group  # noqa: E501

            Removes the user group with the given ID  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.remove_user_group(user_group_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_group_id (str): The ID of the user group

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_group_id'] = \
                user_group_id
            return self.call_with_http_info(**kwargs)

        self.remove_user_group = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups/{userGroupId}',
                'operation_id': 'remove_user_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_group_id',
                ],
                'required': [
                    'user_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_group_id':
                        (str,),
                },
                'attribute_map': {
                    'user_group_id': 'userGroupId',
                },
                'location_map': {
                    'user_group_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__remove_user_group
        )

        def __remove_users_from_user_group(
            self,
            user_group_id,
            **kwargs
        ):
            """Remove users from user group  # noqa: E501

            Removes users from the user group with the given ID  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.remove_users_from_user_group(user_group_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_group_id (str): The ID of the user group

            Keyword Args:
                remove_users_from_user_group_request (RemoveUsersFromUserGroupRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_group_id'] = \
                user_group_id
            return self.call_with_http_info(**kwargs)

        self.remove_users_from_user_group = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/userGroups/{userGroupId}/users',
                'operation_id': 'remove_users_from_user_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_group_id',
                    'remove_users_from_user_group_request',
                ],
                'required': [
                    'user_group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_group_id':
                        (str,),
                    'remove_users_from_user_group_request':
                        (RemoveUsersFromUserGroupRequest,),
                },
                'attribute_map': {
                    'user_group_id': 'userGroupId',
                },
                'location_map': {
                    'user_group_id': 'path',
                    'remove_users_from_user_group_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__remove_users_from_user_group
        )
