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

from pynifi_client.models.port_entity import PortEntity  # noqa: F401,E501


class OutputPortsEntity(object):
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
        'output_ports': 'list[PortEntity]'
    }

    attribute_map = {
        'output_ports': 'outputPorts'
    }

    def __init__(self, output_ports=None):  # noqa: E501
        """OutputPortsEntity - a model defined in Swagger"""  # noqa: E501

        self._output_ports = None
        self.discriminator = None

        if output_ports is not None:
            self.output_ports = output_ports

    @property
    def output_ports(self):
        """Gets the output_ports of this OutputPortsEntity.  # noqa: E501


        :return: The output_ports of this OutputPortsEntity.  # noqa: E501
        :rtype: list[PortEntity]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """Sets the output_ports of this OutputPortsEntity.


        :param output_ports: The output_ports of this OutputPortsEntity.  # noqa: E501
        :type: list[PortEntity]
        """

        self._output_ports = output_ports

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
        if not isinstance(other, OutputPortsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
