"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.data_quality_rules_api import DataQualityRulesApi  # noqa: E501


class TestDataQualityRulesApi(unittest.TestCase):
    """DataQualityRulesApi unit test stubs"""

    def setUp(self):
        self.api = DataQualityRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_data_quality_rule(self):
        """Test case for add_data_quality_rule

        Adds a new data quality rule.  # noqa: E501
        """
        pass

    def test_change_data_quality_rule(self):
        """Test case for change_data_quality_rule

        Changes the data quality rule with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_find_data_quality_rules(self):
        """Test case for find_data_quality_rules

        Returns data quality rules matching the given search criteria.  # noqa: E501
        """
        pass

    def test_get_data_quality_rule(self):
        """Test case for get_data_quality_rule

        Returns the DataQualityRule identified by given id.  # noqa: E501
        """
        pass

    def test_remove_data_quality_rule(self):
        """Test case for remove_data_quality_rule

        Removes the DataQualityRule identified by the given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()