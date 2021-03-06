# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Organization(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'links': 'OrganizationLinks',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'status': 'status'
    }

    def __init__(self, links=None, id=None, name=None, description=None, created_at=None, updated_at=None, status='active'):  # noqa: E501
        """Organization - a model defined in OpenAPI"""  # noqa: E501

        self._links = None
        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status

    @property
    def links(self):
        """Gets the links of this Organization.  # noqa: E501


        :return: The links of this Organization.  # noqa: E501
        :rtype: OrganizationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Organization.


        :param links: The links of this Organization.  # noqa: E501
        :type: OrganizationLinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Organization.  # noqa: E501


        :return: The description of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organization.


        :param description: The description of this Organization.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Organization.  # noqa: E501


        :return: The created_at of this Organization.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Organization.


        :param created_at: The created_at of this Organization.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Organization.  # noqa: E501


        :return: The updated_at of this Organization.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Organization.


        :param updated_at: The updated_at of this Organization.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this Organization.  # noqa: E501

        If inactive the organization is inactive.  # noqa: E501

        :return: The status of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Organization.

        If inactive the organization is inactive.  # noqa: E501

        :param status: The status of this Organization.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
