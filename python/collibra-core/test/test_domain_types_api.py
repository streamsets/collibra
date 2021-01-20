"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.domain_types_api import DomainTypesApi  # noqa: E501


class TestDomainTypesApi(unittest.TestCase):
    """DomainTypesApi unit test stubs"""

    def setUp(self):
        self.api = DomainTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_domain_type(self):
        """Test case for add_domain_type

        Adds a new domain type.  # noqa: E501
        """
        pass

    def test_add_domain_types(self):
        """Test case for add_domain_types

        Adds multiple new domain types.  # noqa: E501
        """
        pass

    def test_change_domain_type(self):
        """Test case for change_domain_type

        Changes the domain type.  # noqa: E501
        """
        pass

    def test_change_domain_types(self):
        """Test case for change_domain_types

        Changes the domain types.  # noqa: E501
        """
        pass

    def test_find_domain_types(self):
        """Test case for find_domain_types

        Returns domain types matching the given search criteria.  # noqa: E501
        """
        pass

    def test_find_sub_domain_types(self):
        """Test case for find_sub_domain_types

        Returns sub domain types matching the given search criteria.  # noqa: E501
        """
        pass

    def test_get_domain_type(self):
        """Test case for get_domain_type

        Returns domain type identified by given UUID.  # noqa: E501
        """
        pass

    def test_remove_domain_type(self):
        """Test case for remove_domain_type

        Removes domain type identified by given UUID.  # noqa: E501
        """
        pass

    def test_remove_domain_types(self):
        """Test case for remove_domain_types

        Removes multiple domain types.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
