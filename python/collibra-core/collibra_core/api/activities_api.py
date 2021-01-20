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
from collibra_core.model.activity_paged_response import ActivityPagedResponse


class ActivitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_activities(
            self,
            **kwargs
        ):
            """Returns activities matching the given search criteria.  # noqa: E501

            Returns activities matching the given search criteria.Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.All other parameters are ignored.The returned activities satisfy all constraints that are specified in this search criteria.By default a result containing 100 activities is returned.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_activities(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.. [optional] if omitted the server will use the default value of 0
                limit (int): The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.. [optional] if omitted the server will use the default value of 0
                task_id (str): The ID of the task which contains the basic find activities request.. [optional]
                context_id (str): The ID of the context which the activities should be searched for.. [optional]
                involved_people_ids ([str]): The list of IDs of the people that should be involved in searched activities.. [optional]
                involved_role_ids ([str]): The list of IDs of the roles that should be involved in searched activities.. [optional]
                performed_by_user_id (str): The ID of the user who performed searched activities.. [optional]
                performed_by_role_ids ([str]): The list of IDs of the roles assigned to users who performed searched activities.. [optional]
                activity_type (str): The type of the activity.. [optional]
                call_id (str): The ID of the call.. [optional]
                categories ([str]): The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT,<br/>STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS].. [optional]
                resource_types ([str]): The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute,<br/>Relation, WorkflowInstance].. [optional]
                start_date (int): TThe start date of the searched activities. It is the timestamp (in UTC time standard).. [optional]
                end_date (int): The end date of the searched activities. It is the timestamp (in UTC time standard).. [optional]
                call_count_enabled (bool): Flag to indicate if the number of calls standing behind the activity should be returned or not.<br/>Note that by default that count will be not calculated as it brings an important performance penalty.. [optional] if omitted the server will use the default value of False
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
                ActivityPagedResponse
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

        self.get_activities = Endpoint(
            settings={
                'response_type': (ActivityPagedResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/activities',
                'operation_id': 'get_activities',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'offset',
                    'limit',
                    'task_id',
                    'context_id',
                    'involved_people_ids',
                    'involved_role_ids',
                    'performed_by_user_id',
                    'performed_by_role_ids',
                    'activity_type',
                    'call_id',
                    'categories',
                    'resource_types',
                    'start_date',
                    'end_date',
                    'call_count_enabled',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'activity_type',
                    'categories',
                    'resource_types',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('activity_type',): {

                        "ADD": "ADD",
                        "UPDATE": "UPDATE",
                        "DELETE": "DELETE"
                    },
                    ('categories',): {

                        "ATTRIBUTE": "ATTRIBUTE",
                        "ATTACHMENT": "ATTACHMENT",
                        "RELATION": "RELATION",
                        "COMMENT": "COMMENT",
                        "STATUS": "STATUS",
                        "WORKFLOW": "WORKFLOW",
                        "RESPONSIBILITY": "RESPONSIBILITY",
                        "USER": "USER",
                        "USER_GROUP": "USER_GROUP",
                        "ROLE": "ROLE",
                        "TAGS": "TAGS",
                        "OTHERS": "OTHERS",
                        "USER_PASSWORD": "USER_PASSWORD"
                    },
                    ('resource_types',): {

                        "VIEW": "View",
                        "ASSET": "Asset",
                        "COMMUNITY": "Community",
                        "DOMAIN": "Domain",
                        "ASSETTYPE": "AssetType",
                        "DOMAINTYPE": "DomainType",
                        "STATUS": "Status",
                        "USER": "User",
                        "CLASSIFICATIONMATCH": "ClassificationMatch",
                        "USERGROUP": "UserGroup",
                        "ATTRIBUTE": "Attribute",
                        "STRINGATTRIBUTE": "StringAttribute",
                        "SCRIPTATTRIBUTE": "ScriptAttribute",
                        "BOOLEANATTRIBUTE": "BooleanAttribute",
                        "DATEATTRIBUTE": "DateAttribute",
                        "NUMERICATTRIBUTE": "NumericAttribute",
                        "SINGLEVALUELISTATTRIBUTE": "SingleValueListAttribute",
                        "MULTIVALUELISTATTRIBUTE": "MultiValueListAttribute",
                        "COMMENT": "Comment",
                        "ATTACHMENT": "Attachment",
                        "RESPONSIBILITY": "Responsibility",
                        "WORKFLOW": "Workflow",
                        "JOB": "Job",
                        "RELATION": "Relation",
                        "RELATIONTYPE": "RelationType",
                        "COMPLEXRELATION": "ComplexRelation",
                        "COMPLEXRELATIONTYPE": "ComplexRelationType",
                        "ARTICULATIONRULE": "ArticulationRule",
                        "ASSIGNMENT": "Assignment",
                        "SCOPE": "Scope",
                        "RELATIONTRACE": "RelationTrace",
                        "VALIDATIONRULE": "ValidationRule",
                        "DATAQUALITYRULE": "DataQualityRule",
                        "DATAQUALITYMETRIC": "DataQualityMetric",
                        "ADDRESS": "Address",
                        "INSTANTMESSAGINGACCOUNT": "InstantMessagingAccount",
                        "EMAIL": "Email",
                        "PHONENUMBER": "PhoneNumber",
                        "WEBSITE": "Website",
                        "ACTIVITY": "Activity",
                        "FORMPROPERTY": "FormProperty",
                        "WORKFLOWTASK": "WorkflowTask",
                        "ACTIVITYCHANGE": "ActivityChange",
                        "WORKFLOWINSTANCE": "WorkflowInstance",
                        "ROLE": "Role",
                        "ATTRIBUTETYPE": "AttributeType",
                        "BOOLEANATTRIBUTETYPE": "BooleanAttributeType",
                        "DATEATTRIBUTETYPE": "DateAttributeType",
                        "DATETIMEATTRIBUTETYPE": "DateTimeAttributeType",
                        "MULTIVALUELISTATTRIBUTETYPE": "MultiValueListAttributeType",
                        "NUMERICATTRIBUTETYPE": "NumericAttributeType",
                        "SCRIPTATTRIBUTETYPE": "ScriptAttributeType",
                        "SINGLEVALUELISTATTRIBUTETYPE": "SingleValueListAttributeType",
                        "STRINGATTRIBUTETYPE": "StringAttributeType",
                        "VIEWSHARINGRULE": "ViewSharingRule",
                        "VIEWASSIGNMENTRULE": "ViewAssignmentRule",
                        "JDBCDRIVERFILE": "JdbcDriverFile",
                        "JDBCDRIVER": "JdbcDriver",
                        "JDBCINGESTIONPROPERTIES": "JdbcIngestionProperties",
                        "CSVINGESTIONPROPERTIES": "CsvIngestionProperties",
                        "EXCELINGESTIONPROPERTIES": "ExcelIngestionProperties",
                        "CONNECTIONSTRINGPARAMETER": "ConnectionStringParameter",
                        "ASSIGNEDCHARACTERISTICTYPE": "AssignedCharacteristicType",
                        "NOTIFICATION": "Notification",
                        "TAG": "Tag",
                        "COMPLEXRELATIONLEGTYPE": "ComplexRelationLegType",
                        "COMPLEXRELATIONATTRIBUTETYPE": "ComplexRelationAttributeType",
                        "COMPLEXRELATIONLEG": "ComplexRelationLeg",
                        "BASEDATATYPE": "BaseDataType",
                        "ADVANCEDDATATYPE": "AdvancedDataType",
                        "DIAGRAMPICTURE": "DiagramPicture",
                        "DIAGRAMPICTURESHARINGRULE": "DiagramPictureSharingRule",
                        "DIAGRAMPICTUREASSIGNMENTRULE": "DiagramPictureAssignmentRule",
                        "RATING": "Rating",
                        "CLASSIFICATION": "Classification"
                    },
                },
                'openapi_types': {
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'task_id':
                        (str,),
                    'context_id':
                        (str,),
                    'involved_people_ids':
                        ([str],),
                    'involved_role_ids':
                        ([str],),
                    'performed_by_user_id':
                        (str,),
                    'performed_by_role_ids':
                        ([str],),
                    'activity_type':
                        (str,),
                    'call_id':
                        (str,),
                    'categories':
                        ([str],),
                    'resource_types':
                        ([str],),
                    'start_date':
                        (int,),
                    'end_date':
                        (int,),
                    'call_count_enabled':
                        (bool,),
                },
                'attribute_map': {
                    'offset': 'offset',
                    'limit': 'limit',
                    'task_id': 'taskId',
                    'context_id': 'contextId',
                    'involved_people_ids': 'involvedPeopleIds',
                    'involved_role_ids': 'involvedRoleIds',
                    'performed_by_user_id': 'performedByUserId',
                    'performed_by_role_ids': 'performedByRoleIds',
                    'activity_type': 'activityType',
                    'call_id': 'callId',
                    'categories': 'categories',
                    'resource_types': 'resourceTypes',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'call_count_enabled': 'callCountEnabled',
                },
                'location_map': {
                    'offset': 'query',
                    'limit': 'query',
                    'task_id': 'query',
                    'context_id': 'query',
                    'involved_people_ids': 'query',
                    'involved_role_ids': 'query',
                    'performed_by_user_id': 'query',
                    'performed_by_role_ids': 'query',
                    'activity_type': 'query',
                    'call_id': 'query',
                    'categories': 'query',
                    'resource_types': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'call_count_enabled': 'query',
                },
                'collection_format_map': {
                    'involved_people_ids': 'multi',
                    'involved_role_ids': 'multi',
                    'performed_by_role_ids': 'multi',
                    'categories': 'multi',
                    'resource_types': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_activities
        )
