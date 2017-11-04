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
from pynifi_client.api.flow_api import FlowApi  # noqa: E501
from pynifi_client.rest import ApiException


class TestFlowApi(unittest.TestCase):
    """FlowApi unit test stubs"""

    def setUp(self):
        self.api = pynifi_client.api.flow_api.FlowApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_controller_services(self):
        """Test case for activate_controller_services

        Enable or disable Controller Services in the specified Process Group.  # noqa: E501
        """
        pass

    def test_generate_client_id(self):
        """Test case for generate_client_id

        Generates a client id.  # noqa: E501
        """
        pass

    def test_get_about_info(self):
        """Test case for get_about_info

        Retrieves details about this NiFi to put in the About dialog  # noqa: E501
        """
        pass

    def test_get_action(self):
        """Test case for get_action

        Gets an action  # noqa: E501
        """
        pass

    def test_get_banners(self):
        """Test case for get_banners

        Retrieves the banners for this NiFi  # noqa: E501
        """
        pass

    def test_get_bulletin_board(self):
        """Test case for get_bulletin_board

        Gets current bulletins  # noqa: E501
        """
        pass

    def test_get_bulletins(self):
        """Test case for get_bulletins

        Retrieves Controller level bulletins  # noqa: E501
        """
        pass

    def test_get_cluster_summary(self):
        """Test case for get_cluster_summary

        The cluster summary for this NiFi  # noqa: E501
        """
        pass

    def test_get_component_history(self):
        """Test case for get_component_history

        Gets configuration history for a component  # noqa: E501
        """
        pass

    def test_get_connection_status(self):
        """Test case for get_connection_status

        Gets status for a connection  # noqa: E501
        """
        pass

    def test_get_connection_status_history(self):
        """Test case for get_connection_status_history

        Gets the status history for a connection  # noqa: E501
        """
        pass

    def test_get_controller_service_types(self):
        """Test case for get_controller_service_types

        Retrieves the types of controller services that this NiFi supports  # noqa: E501
        """
        pass

    def test_get_controller_services_from_controller(self):
        """Test case for get_controller_services_from_controller

        Gets all controller services  # noqa: E501
        """
        pass

    def test_get_controller_services_from_group(self):
        """Test case for get_controller_services_from_group

        Gets all controller services  # noqa: E501
        """
        pass

    def test_get_controller_status(self):
        """Test case for get_controller_status

        Gets the current status of this NiFi  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Retrieves the user identity of the user making the request  # noqa: E501
        """
        pass

    def test_get_flow(self):
        """Test case for get_flow

        Gets a process group  # noqa: E501
        """
        pass

    def test_get_flow_config(self):
        """Test case for get_flow_config

        Retrieves the configuration for this NiFi flow  # noqa: E501
        """
        pass

    def test_get_input_port_status(self):
        """Test case for get_input_port_status

        Gets status for an input port  # noqa: E501
        """
        pass

    def test_get_output_port_status(self):
        """Test case for get_output_port_status

        Gets status for an output port  # noqa: E501
        """
        pass

    def test_get_prioritizers(self):
        """Test case for get_prioritizers

        Retrieves the types of prioritizers that this NiFi supports  # noqa: E501
        """
        pass

    def test_get_process_group_status(self):
        """Test case for get_process_group_status

        Gets the status for a process group  # noqa: E501
        """
        pass

    def test_get_process_group_status_history(self):
        """Test case for get_process_group_status_history

        Gets status history for a remote process group  # noqa: E501
        """
        pass

    def test_get_processor_status(self):
        """Test case for get_processor_status

        Gets status for a processor  # noqa: E501
        """
        pass

    def test_get_processor_status_history(self):
        """Test case for get_processor_status_history

        Gets status history for a processor  # noqa: E501
        """
        pass

    def test_get_processor_types(self):
        """Test case for get_processor_types

        Retrieves the types of processors that this NiFi supports  # noqa: E501
        """
        pass

    def test_get_remote_process_group_status(self):
        """Test case for get_remote_process_group_status

        Gets status for a remote process group  # noqa: E501
        """
        pass

    def test_get_remote_process_group_status_history(self):
        """Test case for get_remote_process_group_status_history

        Gets the status history  # noqa: E501
        """
        pass

    def test_get_reporting_task_types(self):
        """Test case for get_reporting_task_types

        Retrieves the types of reporting tasks that this NiFi supports  # noqa: E501
        """
        pass

    def test_get_reporting_tasks(self):
        """Test case for get_reporting_tasks

        Gets all reporting tasks  # noqa: E501
        """
        pass

    def test_get_templates(self):
        """Test case for get_templates

        Gets all templates  # noqa: E501
        """
        pass

    def test_query_history(self):
        """Test case for query_history

        Gets configuration history  # noqa: E501
        """
        pass

    def test_schedule_components(self):
        """Test case for schedule_components

        Schedule or unschedule components in the specified Process Group.  # noqa: E501
        """
        pass

    def test_search_cluster(self):
        """Test case for search_cluster

        Searches the cluster for a node with the specified address  # noqa: E501
        """
        pass

    def test_search_flow(self):
        """Test case for search_flow

        Performs a search against this NiFi using the specified search term  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
