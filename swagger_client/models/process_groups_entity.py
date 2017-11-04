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

from swagger_client.models.process_group_entity import ProcessGroupEntity  # noqa: F401,E501


class ProcessGroupsEntity(object):
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
        'process_groups': 'list[ProcessGroupEntity]'
    }

    attribute_map = {
        'process_groups': 'processGroups'
    }

    def __init__(self, process_groups=None):  # noqa: E501
        """ProcessGroupsEntity - a model defined in Swagger"""  # noqa: E501

        self._process_groups = None
        self.discriminator = None

        if process_groups is not None:
            self.process_groups = process_groups

    @property
    def process_groups(self):
        """Gets the process_groups of this ProcessGroupsEntity.  # noqa: E501


        :return: The process_groups of this ProcessGroupsEntity.  # noqa: E501
        :rtype: list[ProcessGroupEntity]
        """
        return self._process_groups

    @process_groups.setter
    def process_groups(self, process_groups):
        """Sets the process_groups of this ProcessGroupsEntity.


        :param process_groups: The process_groups of this ProcessGroupsEntity.  # noqa: E501
        :type: list[ProcessGroupEntity]
        """

        self._process_groups = process_groups

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
        if not isinstance(other, ProcessGroupsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
