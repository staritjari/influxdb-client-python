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


class VariableLinks(object):
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
        '_self': 'str',
        'org': 'str',
        'labels': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'org': 'org',
        'labels': 'labels'
    }

    def __init__(self, _self=None, org=None, labels=None):  # noqa: E501
        """VariableLinks - a model defined in OpenAPI"""  # noqa: E501

        self.__self = None
        self._org = None
        self._labels = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if org is not None:
            self.org = org
        if labels is not None:
            self.labels = labels

    @property
    def _self(self):
        """Gets the _self of this VariableLinks.  # noqa: E501


        :return: The _self of this VariableLinks.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this VariableLinks.


        :param _self: The _self of this VariableLinks.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def org(self):
        """Gets the org of this VariableLinks.  # noqa: E501


        :return: The org of this VariableLinks.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this VariableLinks.


        :param org: The org of this VariableLinks.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def labels(self):
        """Gets the labels of this VariableLinks.  # noqa: E501


        :return: The labels of this VariableLinks.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this VariableLinks.


        :param labels: The labels of this VariableLinks.  # noqa: E501
        :type: str
        """

        self._labels = labels

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
        if not isinstance(other, VariableLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other