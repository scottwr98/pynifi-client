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


class FlowConfigurationDTO(object):
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
        'supports_managed_authorizer': 'bool',
        'supports_configurable_authorizer': 'bool',
        'supports_configurable_users_and_groups': 'bool',
        'auto_refresh_interval_seconds': 'int',
        'current_time': 'str',
        'time_offset': 'int'
    }

    attribute_map = {
        'supports_managed_authorizer': 'supportsManagedAuthorizer',
        'supports_configurable_authorizer': 'supportsConfigurableAuthorizer',
        'supports_configurable_users_and_groups': 'supportsConfigurableUsersAndGroups',
        'auto_refresh_interval_seconds': 'autoRefreshIntervalSeconds',
        'current_time': 'currentTime',
        'time_offset': 'timeOffset'
    }

    def __init__(self, supports_managed_authorizer=False, supports_configurable_authorizer=False, supports_configurable_users_and_groups=False, auto_refresh_interval_seconds=None, current_time=None, time_offset=None):  # noqa: E501
        """FlowConfigurationDTO - a model defined in Swagger"""  # noqa: E501

        self._supports_managed_authorizer = None
        self._supports_configurable_authorizer = None
        self._supports_configurable_users_and_groups = None
        self._auto_refresh_interval_seconds = None
        self._current_time = None
        self._time_offset = None
        self.discriminator = None

        if supports_managed_authorizer is not None:
            self.supports_managed_authorizer = supports_managed_authorizer
        if supports_configurable_authorizer is not None:
            self.supports_configurable_authorizer = supports_configurable_authorizer
        if supports_configurable_users_and_groups is not None:
            self.supports_configurable_users_and_groups = supports_configurable_users_and_groups
        if auto_refresh_interval_seconds is not None:
            self.auto_refresh_interval_seconds = auto_refresh_interval_seconds
        if current_time is not None:
            self.current_time = current_time
        if time_offset is not None:
            self.time_offset = time_offset

    @property
    def supports_managed_authorizer(self):
        """Gets the supports_managed_authorizer of this FlowConfigurationDTO.  # noqa: E501

        Whether this NiFi supports a managed authorizer. Managed authorizers can visualize users, groups, and policies in the UI.  # noqa: E501

        :return: The supports_managed_authorizer of this FlowConfigurationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._supports_managed_authorizer

    @supports_managed_authorizer.setter
    def supports_managed_authorizer(self, supports_managed_authorizer):
        """Sets the supports_managed_authorizer of this FlowConfigurationDTO.

        Whether this NiFi supports a managed authorizer. Managed authorizers can visualize users, groups, and policies in the UI.  # noqa: E501

        :param supports_managed_authorizer: The supports_managed_authorizer of this FlowConfigurationDTO.  # noqa: E501
        :type: bool
        """

        self._supports_managed_authorizer = supports_managed_authorizer

    @property
    def supports_configurable_authorizer(self):
        """Gets the supports_configurable_authorizer of this FlowConfigurationDTO.  # noqa: E501

        Whether this NiFi supports a configurable authorizer.  # noqa: E501

        :return: The supports_configurable_authorizer of this FlowConfigurationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._supports_configurable_authorizer

    @supports_configurable_authorizer.setter
    def supports_configurable_authorizer(self, supports_configurable_authorizer):
        """Sets the supports_configurable_authorizer of this FlowConfigurationDTO.

        Whether this NiFi supports a configurable authorizer.  # noqa: E501

        :param supports_configurable_authorizer: The supports_configurable_authorizer of this FlowConfigurationDTO.  # noqa: E501
        :type: bool
        """

        self._supports_configurable_authorizer = supports_configurable_authorizer

    @property
    def supports_configurable_users_and_groups(self):
        """Gets the supports_configurable_users_and_groups of this FlowConfigurationDTO.  # noqa: E501

        Whether this NiFi supports configurable users and groups.  # noqa: E501

        :return: The supports_configurable_users_and_groups of this FlowConfigurationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._supports_configurable_users_and_groups

    @supports_configurable_users_and_groups.setter
    def supports_configurable_users_and_groups(self, supports_configurable_users_and_groups):
        """Sets the supports_configurable_users_and_groups of this FlowConfigurationDTO.

        Whether this NiFi supports configurable users and groups.  # noqa: E501

        :param supports_configurable_users_and_groups: The supports_configurable_users_and_groups of this FlowConfigurationDTO.  # noqa: E501
        :type: bool
        """

        self._supports_configurable_users_and_groups = supports_configurable_users_and_groups

    @property
    def auto_refresh_interval_seconds(self):
        """Gets the auto_refresh_interval_seconds of this FlowConfigurationDTO.  # noqa: E501

        The interval in seconds between the automatic NiFi refresh requests.  # noqa: E501

        :return: The auto_refresh_interval_seconds of this FlowConfigurationDTO.  # noqa: E501
        :rtype: int
        """
        return self._auto_refresh_interval_seconds

    @auto_refresh_interval_seconds.setter
    def auto_refresh_interval_seconds(self, auto_refresh_interval_seconds):
        """Sets the auto_refresh_interval_seconds of this FlowConfigurationDTO.

        The interval in seconds between the automatic NiFi refresh requests.  # noqa: E501

        :param auto_refresh_interval_seconds: The auto_refresh_interval_seconds of this FlowConfigurationDTO.  # noqa: E501
        :type: int
        """

        self._auto_refresh_interval_seconds = auto_refresh_interval_seconds

    @property
    def current_time(self):
        """Gets the current_time of this FlowConfigurationDTO.  # noqa: E501

        The current time on the system.  # noqa: E501

        :return: The current_time of this FlowConfigurationDTO.  # noqa: E501
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """Sets the current_time of this FlowConfigurationDTO.

        The current time on the system.  # noqa: E501

        :param current_time: The current_time of this FlowConfigurationDTO.  # noqa: E501
        :type: str
        """

        self._current_time = current_time

    @property
    def time_offset(self):
        """Gets the time_offset of this FlowConfigurationDTO.  # noqa: E501

        The time offset of the system.  # noqa: E501

        :return: The time_offset of this FlowConfigurationDTO.  # noqa: E501
        :rtype: int
        """
        return self._time_offset

    @time_offset.setter
    def time_offset(self, time_offset):
        """Sets the time_offset of this FlowConfigurationDTO.

        The time offset of the system.  # noqa: E501

        :param time_offset: The time_offset of this FlowConfigurationDTO.  # noqa: E501
        :type: int
        """

        self._time_offset = time_offset

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
        if not isinstance(other, FlowConfigurationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
