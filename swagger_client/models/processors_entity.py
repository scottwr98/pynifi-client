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

from swagger_client.models.processor_entity import ProcessorEntity  # noqa: F401,E501


class ProcessorsEntity(object):
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
        'processors': 'list[ProcessorEntity]'
    }

    attribute_map = {
        'processors': 'processors'
    }

    def __init__(self, processors=None):  # noqa: E501
        """ProcessorsEntity - a model defined in Swagger"""  # noqa: E501

        self._processors = None
        self.discriminator = None

        if processors is not None:
            self.processors = processors

    @property
    def processors(self):
        """Gets the processors of this ProcessorsEntity.  # noqa: E501


        :return: The processors of this ProcessorsEntity.  # noqa: E501
        :rtype: list[ProcessorEntity]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this ProcessorsEntity.


        :param processors: The processors of this ProcessorsEntity.  # noqa: E501
        :type: list[ProcessorEntity]
        """

        self._processors = processors

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
        if not isinstance(other, ProcessorsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
