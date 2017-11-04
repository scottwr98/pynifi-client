# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.  # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.connection_dto import ConnectionDTO  # noqa: F401,E501
from swagger_client.models.controller_service_dto import ControllerServiceDTO  # noqa: F401,E501
from swagger_client.models.funnel_dto import FunnelDTO  # noqa: F401,E501
from swagger_client.models.label_dto import LabelDTO  # noqa: F401,E501
from swagger_client.models.port_dto import PortDTO  # noqa: F401,E501
from swagger_client.models.process_group_dto import ProcessGroupDTO  # noqa: F401,E501
from swagger_client.models.processor_dto import ProcessorDTO  # noqa: F401,E501
from swagger_client.models.remote_process_group_dto import RemoteProcessGroupDTO  # noqa: F401,E501


class FlowSnippetDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'process_groups': 'list[ProcessGroupDTO]',
        'remote_process_groups': 'list[RemoteProcessGroupDTO]',
        'processors': 'list[ProcessorDTO]',
        'input_ports': 'list[PortDTO]',
        'output_ports': 'list[PortDTO]',
        'connections': 'list[ConnectionDTO]',
        'labels': 'list[LabelDTO]',
        'funnels': 'list[FunnelDTO]',
        'controller_services': 'list[ControllerServiceDTO]'
    }

    attribute_map = {
        'process_groups': 'processGroups',
        'remote_process_groups': 'remoteProcessGroups',
        'processors': 'processors',
        'input_ports': 'inputPorts',
        'output_ports': 'outputPorts',
        'connections': 'connections',
        'labels': 'labels',
        'funnels': 'funnels',
        'controller_services': 'controllerServices'
    }

    def __init__(self, process_groups=None, remote_process_groups=None, processors=None, input_ports=None, output_ports=None, connections=None, labels=None, funnels=None, controller_services=None):  # noqa: E501
        """FlowSnippetDTO - a model defined in Swagger"""  # noqa: E501

        self._process_groups = None
        self._remote_process_groups = None
        self._processors = None
        self._input_ports = None
        self._output_ports = None
        self._connections = None
        self._labels = None
        self._funnels = None
        self._controller_services = None
        self.discriminator = None

        if process_groups is not None:
            self.process_groups = process_groups
        if remote_process_groups is not None:
            self.remote_process_groups = remote_process_groups
        if processors is not None:
            self.processors = processors
        if input_ports is not None:
            self.input_ports = input_ports
        if output_ports is not None:
            self.output_ports = output_ports
        if connections is not None:
            self.connections = connections
        if labels is not None:
            self.labels = labels
        if funnels is not None:
            self.funnels = funnels
        if controller_services is not None:
            self.controller_services = controller_services

    @property
    def process_groups(self):
        """Gets the process_groups of this FlowSnippetDTO.  # noqa: E501

        The process groups in this flow snippet.  # noqa: E501

        :return: The process_groups of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[ProcessGroupDTO]
        """
        return self._process_groups

    @process_groups.setter
    def process_groups(self, process_groups):
        """Sets the process_groups of this FlowSnippetDTO.

        The process groups in this flow snippet.  # noqa: E501

        :param process_groups: The process_groups of this FlowSnippetDTO.  # noqa: E501
        :type: list[ProcessGroupDTO]
        """

        self._process_groups = process_groups

    @property
    def remote_process_groups(self):
        """Gets the remote_process_groups of this FlowSnippetDTO.  # noqa: E501

        The remote process groups in this flow snippet.  # noqa: E501

        :return: The remote_process_groups of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[RemoteProcessGroupDTO]
        """
        return self._remote_process_groups

    @remote_process_groups.setter
    def remote_process_groups(self, remote_process_groups):
        """Sets the remote_process_groups of this FlowSnippetDTO.

        The remote process groups in this flow snippet.  # noqa: E501

        :param remote_process_groups: The remote_process_groups of this FlowSnippetDTO.  # noqa: E501
        :type: list[RemoteProcessGroupDTO]
        """

        self._remote_process_groups = remote_process_groups

    @property
    def processors(self):
        """Gets the processors of this FlowSnippetDTO.  # noqa: E501

        The processors in this flow snippet.  # noqa: E501

        :return: The processors of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[ProcessorDTO]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this FlowSnippetDTO.

        The processors in this flow snippet.  # noqa: E501

        :param processors: The processors of this FlowSnippetDTO.  # noqa: E501
        :type: list[ProcessorDTO]
        """

        self._processors = processors

    @property
    def input_ports(self):
        """Gets the input_ports of this FlowSnippetDTO.  # noqa: E501

        The input ports in this flow snippet.  # noqa: E501

        :return: The input_ports of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[PortDTO]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """Sets the input_ports of this FlowSnippetDTO.

        The input ports in this flow snippet.  # noqa: E501

        :param input_ports: The input_ports of this FlowSnippetDTO.  # noqa: E501
        :type: list[PortDTO]
        """

        self._input_ports = input_ports

    @property
    def output_ports(self):
        """Gets the output_ports of this FlowSnippetDTO.  # noqa: E501

        The output ports in this flow snippet.  # noqa: E501

        :return: The output_ports of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[PortDTO]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """Sets the output_ports of this FlowSnippetDTO.

        The output ports in this flow snippet.  # noqa: E501

        :param output_ports: The output_ports of this FlowSnippetDTO.  # noqa: E501
        :type: list[PortDTO]
        """

        self._output_ports = output_ports

    @property
    def connections(self):
        """Gets the connections of this FlowSnippetDTO.  # noqa: E501

        The connections in this flow snippet.  # noqa: E501

        :return: The connections of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[ConnectionDTO]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this FlowSnippetDTO.

        The connections in this flow snippet.  # noqa: E501

        :param connections: The connections of this FlowSnippetDTO.  # noqa: E501
        :type: list[ConnectionDTO]
        """

        self._connections = connections

    @property
    def labels(self):
        """Gets the labels of this FlowSnippetDTO.  # noqa: E501

        The labels in this flow snippet.  # noqa: E501

        :return: The labels of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[LabelDTO]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this FlowSnippetDTO.

        The labels in this flow snippet.  # noqa: E501

        :param labels: The labels of this FlowSnippetDTO.  # noqa: E501
        :type: list[LabelDTO]
        """

        self._labels = labels

    @property
    def funnels(self):
        """Gets the funnels of this FlowSnippetDTO.  # noqa: E501

        The funnels in this flow snippet.  # noqa: E501

        :return: The funnels of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[FunnelDTO]
        """
        return self._funnels

    @funnels.setter
    def funnels(self, funnels):
        """Sets the funnels of this FlowSnippetDTO.

        The funnels in this flow snippet.  # noqa: E501

        :param funnels: The funnels of this FlowSnippetDTO.  # noqa: E501
        :type: list[FunnelDTO]
        """

        self._funnels = funnels

    @property
    def controller_services(self):
        """Gets the controller_services of this FlowSnippetDTO.  # noqa: E501

        The controller services in this flow snippet.  # noqa: E501

        :return: The controller_services of this FlowSnippetDTO.  # noqa: E501
        :rtype: list[ControllerServiceDTO]
        """
        return self._controller_services

    @controller_services.setter
    def controller_services(self, controller_services):
        """Sets the controller_services of this FlowSnippetDTO.

        The controller services in this flow snippet.  # noqa: E501

        :param controller_services: The controller_services of this FlowSnippetDTO.  # noqa: E501
        :type: list[ControllerServiceDTO]
        """

        self._controller_services = controller_services

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FlowSnippetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
