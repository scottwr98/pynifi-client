# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.  # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pynifi_client
from pynifi_client.models.history_entity import HistoryEntity  # noqa: E501
from pynifi_client.rest import ApiException


class TestHistoryEntity(unittest.TestCase):
    """HistoryEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHistoryEntity(self):
        """Test HistoryEntity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = pynifi_client.models.history_entity.HistoryEntity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
