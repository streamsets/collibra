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
from collibra_core.model.add_issue_request import AddIssueRequest
from collibra_core.model.asset_impl import AssetImpl
from collibra_core.model.asset_paged_response import AssetPagedResponse


class IssuesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_issue(
            self,
            **kwargs
        ):
            """Adds a new issue.  # noqa: E501

            Adds a new issue with the given parameters.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_issue(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                add_issue_request (AddIssueRequest): The properties of the issue to be added. [optional]
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
                AssetImpl
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

        self.add_issue = Endpoint(
            settings={
                'response_type': (AssetImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/issues',
                'operation_id': 'add_issue',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'add_issue_request',
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
                    'add_issue_request':
                        (AddIssueRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'add_issue_request': 'body',
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
            callable=__add_issue
        )

        def __find_issues(
            self,
            **kwargs
        ):
            """Returns issues matching the given search criteria.  # noqa: E501

            Returns issues matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned issues satisfy all constraints that are specified in this search criteria. By default a result containing 1000 issues is returned.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_issues(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                sort_order (str): The sorting order of the results.. [optional] if omitted the server will use the default value of "ASC"
                sort_field (str): The field on which the results are sorted. Default is NAME.. [optional] if omitted the server will use the default value of "NAME"
                only_open_issues (bool): Whether only open issues should be returned.. [optional] if omitted the server will use the default value of True
                user_relation (str): The relation of the user with the issues to be returned. By default all issues for the current user will be returned.. [optional] if omitted the server will use the default value of "ALL"
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
                AssetPagedResponse
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

        self.find_issues = Endpoint(
            settings={
                'response_type': (AssetPagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/issues',
                'operation_id': 'find_issues',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'sort_order',
                    'sort_field',
                    'only_open_issues',
                    'user_relation',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort_order',
                    'sort_field',
                    'user_relation',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('sort_order',): {

                        "ASC": "ASC",
                        "DESC": "DESC"
                    },
                    ('sort_field',): {

                        "NAME": "NAME",
                        "PRIORITY": "PRIORITY",
                        "RESOLUTION": "RESOLUTION",
                        "CREATED_BY": "CREATED_BY"
                    },
                    ('user_relation',): {

                        "ALL": "ALL",
                        "ASSIGNED": "ASSIGNED",
                        "CREATED": "CREATED"
                    },
                },
                'openapi_types': {
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'sort_order':
                        (str,),
                    'sort_field':
                        (str,),
                    'only_open_issues':
                        (bool,),
                    'user_relation':
                        (str,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'sort_order': 'sortOrder',
                    'sort_field': 'sortField',
                    'only_open_issues': 'onlyOpenIssues',
                    'user_relation': 'userRelation',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'sort_order': 'query',
                    'sort_field': 'query',
                    'only_open_issues': 'query',
                    'user_relation': 'query',
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
            callable=__find_issues
        )

        def __move_issue(
            self,
            issue_id,
            community_id,
            **kwargs
        ):
            """Moves an issue to another community.  # noqa: E501

            Moves an issue to another community.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.move_issue(issue_id, community_id, async_req=True)
            >>> result = thread.get()

            Args:
                issue_id (str): ID of the issue to be moved
                community_id (str): ID of the community to move the issue to

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
                AssetImpl
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
            kwargs['issue_id'] = \
                issue_id
            kwargs['community_id'] = \
                community_id
            return self.call_with_http_info(**kwargs)

        self.move_issue = Endpoint(
            settings={
                'response_type': (AssetImpl,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/issues/{issueId}/community/{communityId}',
                'operation_id': 'move_issue',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'issue_id',
                    'community_id',
                ],
                'required': [
                    'issue_id',
                    'community_id',
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
                    'issue_id':
                        (str,),
                    'community_id':
                        (str,),
                },
                'attribute_map': {
                    'issue_id': 'issueId',
                    'community_id': 'communityId',
                },
                'location_map': {
                    'issue_id': 'path',
                    'community_id': 'path',
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
            callable=__move_issue
        )