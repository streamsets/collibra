"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import collibra_core
from collibra_core.model.data_quality_metric_request import DataQualityMetricRequest
from collibra_core.model.relation_trace_entry_request import RelationTraceEntryRequest
globals()['DataQualityMetricRequest'] = DataQualityMetricRequest
globals()['RelationTraceEntryRequest'] = RelationTraceEntryRequest
from collibra_core.model.add_data_quality_rule_request import AddDataQualityRuleRequest


class TestAddDataQualityRuleRequest(unittest.TestCase):
    """AddDataQualityRuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddDataQualityRuleRequest(self):
        """Test AddDataQualityRuleRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddDataQualityRuleRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
