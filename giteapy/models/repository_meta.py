# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.23.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class RepositoryMeta(object):
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
        'full_name': 'str',
        'id': 'int',
        'name': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'full_name': 'full_name',
        'id': 'id',
        'name': 'name',
        'owner': 'owner'
    }

    def __init__(self, full_name=None, id=None, name=None, owner=None, _configuration=None):  # noqa: E501
        """RepositoryMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._full_name = None
        self._id = None
        self._name = None
        self._owner = None
        self.discriminator = None

        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner

    @property
    def full_name(self):
        """Gets the full_name of this RepositoryMeta.  # noqa: E501


        :return: The full_name of this RepositoryMeta.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this RepositoryMeta.


        :param full_name: The full_name of this RepositoryMeta.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this RepositoryMeta.  # noqa: E501


        :return: The id of this RepositoryMeta.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepositoryMeta.


        :param id: The id of this RepositoryMeta.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RepositoryMeta.  # noqa: E501


        :return: The name of this RepositoryMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryMeta.


        :param name: The name of this RepositoryMeta.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this RepositoryMeta.  # noqa: E501


        :return: The owner of this RepositoryMeta.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this RepositoryMeta.


        :param owner: The owner of this RepositoryMeta.  # noqa: E501
        :type: str
        """

        self._owner = owner

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
        if issubclass(RepositoryMeta, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositoryMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryMeta):
            return True

        return self.to_dict() != other.to_dict()
