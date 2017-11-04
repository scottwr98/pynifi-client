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
from pynifi_client.api.output_ports_api import OutputPortsApi  # noqa: E501
from pynifi_client.rest import ApiException


class TestOutputPortsApi(unittest.TestCase):
    """OutputPortsApi unit test stubs"""

    def setUp(self):
        self.api = pynifi_client.api.output_ports_api.OutputPortsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_output_port(self):
        """Test case for get_output_port

        Gets an output port  # noqa: E501
        """
        pass

    def test_remove_output_port(self):
        """Test case for remove_output_port

        Deletes an output port  # noqa: E501
        """
        pass

    def test_update_output_port(self):
        """Test case for update_output_port

        Updates an output port  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()