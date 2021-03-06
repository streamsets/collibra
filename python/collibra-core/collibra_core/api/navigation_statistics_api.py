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
from collibra_core.model.navigation_statistics_entry_paged_response import NavigationStatisticsEntryPagedResponse


class NavigationStatisticsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __find_most_viewed_assets(
            self,
            **kwargs
        ):
            """Find most viewed assets.  # noqa: E501

            Returns the most viewed assets by all users, with navigation-related info.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_most_viewed_assets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                period (int): The time span for which most viewed assets should be found. This time span must be expressed in milliseconds.<br/>For instance, to get most viewed assets for last 24 hours, period would be <code>86400000</code>.<br/>If it's unset (period = 0) looks for all time most viewed assets.. [optional] if omitted the server will use the default value of 0
                is_guest_excluded (bool): Whether guest visits should be excluded from result.. [optional] if omitted the server will use the default value of False
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
                NavigationStatisticsEntryPagedResponse
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

        self.find_most_viewed_assets = Endpoint(
            settings={
                'response_type': (NavigationStatisticsEntryPagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/navigation/most_viewed',
                'operation_id': 'find_most_viewed_assets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'period',
                    'is_guest_excluded',
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
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'period':
                        (int,),
                    'is_guest_excluded':
                        (bool,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'period': 'period',
                    'is_guest_excluded': 'isGuestExcluded',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'period': 'query',
                    'is_guest_excluded': 'query',
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
            callable=__find_most_viewed_assets
        )

        def __find_recently_viewed_assets(
            self,
            **kwargs
        ):
            """Find recently viewed assets.  # noqa: E501

            Returns the assets that were recently viewed by the current user.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_recently_viewed_assets(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
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
                NavigationStatisticsEntryPagedResponse
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

        self.find_recently_viewed_assets = Endpoint(
            settings={
                'response_type': (NavigationStatisticsEntryPagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/navigation/recently_viewed',
                'operation_id': 'find_recently_viewed_assets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
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
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
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
            callable=__find_recently_viewed_assets
        )
