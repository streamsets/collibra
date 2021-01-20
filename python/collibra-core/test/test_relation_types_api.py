"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.relation_types_api import RelationTypesApi  # noqa: E501


class TestRelationTypesApi(unittest.TestCase):
    """RelationTypesApi unit test stubs"""

    def setUp(self):
        self.api = RelationTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_relation_type(self):
        """Test case for add_relation_type

        Adds a new relation type.  # noqa: E501
        """
        pass

    def test_add_relation_types(self):
        """Test case for add_relation_types

        Adds multiple new relation type.  # noqa: E501
        """
        pass

    def test_change_relation_type(self):
        """Test case for change_relation_type

        Changes the relation type.  # noqa: E501
        """
        pass

    def test_change_relation_types(self):
        """Test case for change_relation_types

        Changes the relation types.  # noqa: E501
        """
        pass

    def test_find_relation_types(self):
        """Test case for find_relation_types

        Finds all the relation types matching the given criteria.  # noqa: E501
        """
        pass

    def test_get_relation_type(self):
        """Test case for get_relation_type

        Returns relation type identified by given UUID.  # noqa: E501
        """
        pass

    def test_remove_relation_type(self):
        """Test case for remove_relation_type

        Removes relation type identified by given UUID.  # noqa: E501
        """
        pass

    def test_remove_relation_types(self):
        """Test case for remove_relation_types

        Removes multiple relation types.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
