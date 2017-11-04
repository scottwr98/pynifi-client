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

import swagger_client
from swagger_client.api.snippets_api import SnippetsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSnippetsApi(unittest.TestCase):
    """SnippetsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.snippets_api.SnippetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_snippet(self):
        """Test case for create_snippet

        Creates a snippet. The snippet will be automatically discarded if not used in a subsequent request after 1 minute.  # noqa: E501
        """
        pass

    def test_delete_snippet(self):
        """Test case for delete_snippet

        Deletes the components in a snippet and discards the snippet  # noqa: E501
        """
        pass

    def test_update_snippet(self):
        """Test case for update_snippet

        Move's the components in this Snippet into a new Process Group and discards the snippet  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
