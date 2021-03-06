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


class ReportingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_insights_zip(
            self,
            **kwargs
        ):
            """Reporting insights download  # noqa: E501

            Returns a Reporting Data archive (zip) file that contains Apache Parquet files with table content for each of the six concepts (community, domain, asset, attribute, relation and responsibility) for one day (=snapshot date). Each morning, at 00:01 in the timezone of the Collibra platform, the reporting data of that platform is captured. The reporting data is retained for one rolling month and each month’s end before that. The tables structure (DDL) for this content is published [here](https://marketplace.collibra.com/listings/reporting-data-layer).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_insights_zip(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                snapshot_date (str): Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14). [optional]
                format (str): Archive format. Currently only ZIP format is accepted. [optional] if omitted the server will use the default value of "zip"
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
                file_type
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

        self.get_insights_zip = Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/reporting/insights/download',
                'operation_id': 'get_insights_zip',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'snapshot_date',
                    'format',
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
                    'snapshot_date':
                        (str,),
                    'format':
                        (str,),
                },
                'attribute_map': {
                    'snapshot_date': 'snapshotDate',
                    'format': 'format',
                },
                'location_map': {
                    'snapshot_date': 'query',
                    'format': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_insights_zip
        )
