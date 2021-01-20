"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from collibra_core.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class AssetReferenceImpl(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('resource_type',): {
            'VIEW': "View",
            'ASSET': "Asset",
            'COMMUNITY': "Community",
            'DOMAIN': "Domain",
            'ASSETTYPE': "AssetType",
            'DOMAINTYPE': "DomainType",
            'STATUS': "Status",
            'USER': "User",
            'CLASSIFICATIONMATCH': "ClassificationMatch",
            'USERGROUP': "UserGroup",
            'ATTRIBUTE': "Attribute",
            'STRINGATTRIBUTE': "StringAttribute",
            'SCRIPTATTRIBUTE': "ScriptAttribute",
            'BOOLEANATTRIBUTE': "BooleanAttribute",
            'DATEATTRIBUTE': "DateAttribute",
            'NUMERICATTRIBUTE': "NumericAttribute",
            'SINGLEVALUELISTATTRIBUTE': "SingleValueListAttribute",
            'MULTIVALUELISTATTRIBUTE': "MultiValueListAttribute",
            'COMMENT': "Comment",
            'ATTACHMENT': "Attachment",
            'RESPONSIBILITY': "Responsibility",
            'WORKFLOW': "Workflow",
            'JOB': "Job",
            'RELATION': "Relation",
            'RELATIONTYPE': "RelationType",
            'COMPLEXRELATION': "ComplexRelation",
            'COMPLEXRELATIONTYPE': "ComplexRelationType",
            'ARTICULATIONRULE': "ArticulationRule",
            'ASSIGNMENT': "Assignment",
            'SCOPE': "Scope",
            'RELATIONTRACE': "RelationTrace",
            'VALIDATIONRULE': "ValidationRule",
            'DATAQUALITYRULE': "DataQualityRule",
            'DATAQUALITYMETRIC': "DataQualityMetric",
            'ADDRESS': "Address",
            'INSTANTMESSAGINGACCOUNT': "InstantMessagingAccount",
            'EMAIL': "Email",
            'PHONENUMBER': "PhoneNumber",
            'WEBSITE': "Website",
            'ACTIVITY': "Activity",
            'FORMPROPERTY': "FormProperty",
            'WORKFLOWTASK': "WorkflowTask",
            'ACTIVITYCHANGE': "ActivityChange",
            'WORKFLOWINSTANCE': "WorkflowInstance",
            'ROLE': "Role",
            'ATTRIBUTETYPE': "AttributeType",
            'BOOLEANATTRIBUTETYPE': "BooleanAttributeType",
            'DATEATTRIBUTETYPE': "DateAttributeType",
            'DATETIMEATTRIBUTETYPE': "DateTimeAttributeType",
            'MULTIVALUELISTATTRIBUTETYPE': "MultiValueListAttributeType",
            'NUMERICATTRIBUTETYPE': "NumericAttributeType",
            'SCRIPTATTRIBUTETYPE': "ScriptAttributeType",
            'SINGLEVALUELISTATTRIBUTETYPE': "SingleValueListAttributeType",
            'STRINGATTRIBUTETYPE': "StringAttributeType",
            'VIEWSHARINGRULE': "ViewSharingRule",
            'VIEWASSIGNMENTRULE': "ViewAssignmentRule",
            'JDBCDRIVERFILE': "JdbcDriverFile",
            'JDBCDRIVER': "JdbcDriver",
            'JDBCINGESTIONPROPERTIES': "JdbcIngestionProperties",
            'CSVINGESTIONPROPERTIES': "CsvIngestionProperties",
            'EXCELINGESTIONPROPERTIES': "ExcelIngestionProperties",
            'CONNECTIONSTRINGPARAMETER': "ConnectionStringParameter",
            'ASSIGNEDCHARACTERISTICTYPE': "AssignedCharacteristicType",
            'NOTIFICATION': "Notification",
            'TAG': "Tag",
            'COMPLEXRELATIONLEGTYPE': "ComplexRelationLegType",
            'COMPLEXRELATIONATTRIBUTETYPE': "ComplexRelationAttributeType",
            'COMPLEXRELATIONLEG': "ComplexRelationLeg",
            'BASEDATATYPE': "BaseDataType",
            'ADVANCEDDATATYPE': "AdvancedDataType",
            'DIAGRAMPICTURE': "DiagramPicture",
            'DIAGRAMPICTURESHARINGRULE': "DiagramPictureSharingRule",
            'DIAGRAMPICTUREASSIGNMENTRULE': "DiagramPictureAssignmentRule",
            'RATING': "Rating",
            'CLASSIFICATION': "Classification",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (str,),  # noqa: E501
            'resource_type': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'resource_type': 'resourceType',  # noqa: E501
        'name': 'name',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, resource_type, *args, **kwargs):  # noqa: E501
        """AssetReferenceImpl - a model defined in OpenAPI

        Args:
            id (str): The id of the referenced resource.
            resource_type (str): The type of the resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): The name of the referenced resource.. [optional]  # noqa: E501
            display_name (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.resource_type = resource_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
