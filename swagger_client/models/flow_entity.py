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

from swagger_client.models.flow_dto import FlowDTO  # noqa: F401,E501


class FlowEntity(object):
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
        'flow': 'FlowDTO'
    }

    attribute_map = {
        'flow': 'flow'
    }

    def __init__(self, flow=None):  # noqa: E501
        """FlowEntity - a model defined in Swagger"""  # noqa: E501

        self._flow = None
        self.discriminator = None

        if flow is not None:
            self.flow = flow

    @property
    def flow(self):
        """Gets the flow of this FlowEntity.  # noqa: E501


        :return: The flow of this FlowEntity.  # noqa: E501
        :rtype: FlowDTO
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this FlowEntity.


        :param flow: The flow of this FlowEntity.  # noqa: E501
        :type: FlowDTO
        """

        self._flow = flow

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
        if not isinstance(other, FlowEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
