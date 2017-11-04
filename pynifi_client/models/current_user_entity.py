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

from pynifi_client.models.permissions_dto import PermissionsDTO  # noqa: F401,E501


class CurrentUserEntity(object):
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
        'identity': 'str',
        'anonymous': 'bool',
        'provenance_permissions': 'PermissionsDTO',
        'counters_permissions': 'PermissionsDTO',
        'tenants_permissions': 'PermissionsDTO',
        'controller_permissions': 'PermissionsDTO',
        'policies_permissions': 'PermissionsDTO',
        'system_permissions': 'PermissionsDTO',
        'restricted_components_permissions': 'PermissionsDTO'
    }

    attribute_map = {
        'identity': 'identity',
        'anonymous': 'anonymous',
        'provenance_permissions': 'provenancePermissions',
        'counters_permissions': 'countersPermissions',
        'tenants_permissions': 'tenantsPermissions',
        'controller_permissions': 'controllerPermissions',
        'policies_permissions': 'policiesPermissions',
        'system_permissions': 'systemPermissions',
        'restricted_components_permissions': 'restrictedComponentsPermissions'
    }

    def __init__(self, identity=None, anonymous=False, provenance_permissions=None, counters_permissions=None, tenants_permissions=None, controller_permissions=None, policies_permissions=None, system_permissions=None, restricted_components_permissions=None):  # noqa: E501
        """CurrentUserEntity - a model defined in Swagger"""  # noqa: E501

        self._identity = None
        self._anonymous = None
        self._provenance_permissions = None
        self._counters_permissions = None
        self._tenants_permissions = None
        self._controller_permissions = None
        self._policies_permissions = None
        self._system_permissions = None
        self._restricted_components_permissions = None
        self.discriminator = None

        if identity is not None:
            self.identity = identity
        if anonymous is not None:
            self.anonymous = anonymous
        if provenance_permissions is not None:
            self.provenance_permissions = provenance_permissions
        if counters_permissions is not None:
            self.counters_permissions = counters_permissions
        if tenants_permissions is not None:
            self.tenants_permissions = tenants_permissions
        if controller_permissions is not None:
            self.controller_permissions = controller_permissions
        if policies_permissions is not None:
            self.policies_permissions = policies_permissions
        if system_permissions is not None:
            self.system_permissions = system_permissions
        if restricted_components_permissions is not None:
            self.restricted_components_permissions = restricted_components_permissions

    @property
    def identity(self):
        """Gets the identity of this CurrentUserEntity.  # noqa: E501

        The user identity being serialized.  # noqa: E501

        :return: The identity of this CurrentUserEntity.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this CurrentUserEntity.

        The user identity being serialized.  # noqa: E501

        :param identity: The identity of this CurrentUserEntity.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def anonymous(self):
        """Gets the anonymous of this CurrentUserEntity.  # noqa: E501

        Whether the current user is anonymous.  # noqa: E501

        :return: The anonymous of this CurrentUserEntity.  # noqa: E501
        :rtype: bool
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous):
        """Sets the anonymous of this CurrentUserEntity.

        Whether the current user is anonymous.  # noqa: E501

        :param anonymous: The anonymous of this CurrentUserEntity.  # noqa: E501
        :type: bool
        """

        self._anonymous = anonymous

    @property
    def provenance_permissions(self):
        """Gets the provenance_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for querying provenance.  # noqa: E501

        :return: The provenance_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._provenance_permissions

    @provenance_permissions.setter
    def provenance_permissions(self, provenance_permissions):
        """Sets the provenance_permissions of this CurrentUserEntity.

        Permissions for querying provenance.  # noqa: E501

        :param provenance_permissions: The provenance_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._provenance_permissions = provenance_permissions

    @property
    def counters_permissions(self):
        """Gets the counters_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for accessing counters.  # noqa: E501

        :return: The counters_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._counters_permissions

    @counters_permissions.setter
    def counters_permissions(self, counters_permissions):
        """Sets the counters_permissions of this CurrentUserEntity.

        Permissions for accessing counters.  # noqa: E501

        :param counters_permissions: The counters_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._counters_permissions = counters_permissions

    @property
    def tenants_permissions(self):
        """Gets the tenants_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for accessing tenants.  # noqa: E501

        :return: The tenants_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._tenants_permissions

    @tenants_permissions.setter
    def tenants_permissions(self, tenants_permissions):
        """Sets the tenants_permissions of this CurrentUserEntity.

        Permissions for accessing tenants.  # noqa: E501

        :param tenants_permissions: The tenants_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._tenants_permissions = tenants_permissions

    @property
    def controller_permissions(self):
        """Gets the controller_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for accessing the controller.  # noqa: E501

        :return: The controller_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._controller_permissions

    @controller_permissions.setter
    def controller_permissions(self, controller_permissions):
        """Sets the controller_permissions of this CurrentUserEntity.

        Permissions for accessing the controller.  # noqa: E501

        :param controller_permissions: The controller_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._controller_permissions = controller_permissions

    @property
    def policies_permissions(self):
        """Gets the policies_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for accessing the policies.  # noqa: E501

        :return: The policies_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._policies_permissions

    @policies_permissions.setter
    def policies_permissions(self, policies_permissions):
        """Sets the policies_permissions of this CurrentUserEntity.

        Permissions for accessing the policies.  # noqa: E501

        :param policies_permissions: The policies_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._policies_permissions = policies_permissions

    @property
    def system_permissions(self):
        """Gets the system_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for accessing system.  # noqa: E501

        :return: The system_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._system_permissions

    @system_permissions.setter
    def system_permissions(self, system_permissions):
        """Sets the system_permissions of this CurrentUserEntity.

        Permissions for accessing system.  # noqa: E501

        :param system_permissions: The system_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._system_permissions = system_permissions

    @property
    def restricted_components_permissions(self):
        """Gets the restricted_components_permissions of this CurrentUserEntity.  # noqa: E501

        Permissions for accessing restricted components. Note: the read permission are not used and will always be false.  # noqa: E501

        :return: The restricted_components_permissions of this CurrentUserEntity.  # noqa: E501
        :rtype: PermissionsDTO
        """
        return self._restricted_components_permissions

    @restricted_components_permissions.setter
    def restricted_components_permissions(self, restricted_components_permissions):
        """Sets the restricted_components_permissions of this CurrentUserEntity.

        Permissions for accessing restricted components. Note: the read permission are not used and will always be false.  # noqa: E501

        :param restricted_components_permissions: The restricted_components_permissions of this CurrentUserEntity.  # noqa: E501
        :type: PermissionsDTO
        """

        self._restricted_components_permissions = restricted_components_permissions

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
        if not isinstance(other, CurrentUserEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other