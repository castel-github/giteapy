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


class PackageFile(object):
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
        'size': 'int',
        'id': 'int',
        'md5': 'str',
        'name': 'str',
        'sha1': 'str',
        'sha256': 'str',
        'sha512': 'str'
    }

    attribute_map = {
        'size': 'Size',
        'id': 'id',
        'md5': 'md5',
        'name': 'name',
        'sha1': 'sha1',
        'sha256': 'sha256',
        'sha512': 'sha512'
    }

    def __init__(self, size=None, id=None, md5=None, name=None, sha1=None, sha256=None, sha512=None, _configuration=None):  # noqa: E501
        """PackageFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._size = None
        self._id = None
        self._md5 = None
        self._name = None
        self._sha1 = None
        self._sha256 = None
        self._sha512 = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if id is not None:
            self.id = id
        if md5 is not None:
            self.md5 = md5
        if name is not None:
            self.name = name
        if sha1 is not None:
            self.sha1 = sha1
        if sha256 is not None:
            self.sha256 = sha256
        if sha512 is not None:
            self.sha512 = sha512

    @property
    def size(self):
        """Gets the size of this PackageFile.  # noqa: E501


        :return: The size of this PackageFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PackageFile.


        :param size: The size of this PackageFile.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def id(self):
        """Gets the id of this PackageFile.  # noqa: E501


        :return: The id of this PackageFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageFile.


        :param id: The id of this PackageFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def md5(self):
        """Gets the md5 of this PackageFile.  # noqa: E501


        :return: The md5 of this PackageFile.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this PackageFile.


        :param md5: The md5 of this PackageFile.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def name(self):
        """Gets the name of this PackageFile.  # noqa: E501


        :return: The name of this PackageFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageFile.


        :param name: The name of this PackageFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sha1(self):
        """Gets the sha1 of this PackageFile.  # noqa: E501


        :return: The sha1 of this PackageFile.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this PackageFile.


        :param sha1: The sha1 of this PackageFile.  # noqa: E501
        :type: str
        """

        self._sha1 = sha1

    @property
    def sha256(self):
        """Gets the sha256 of this PackageFile.  # noqa: E501


        :return: The sha256 of this PackageFile.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this PackageFile.


        :param sha256: The sha256 of this PackageFile.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def sha512(self):
        """Gets the sha512 of this PackageFile.  # noqa: E501


        :return: The sha512 of this PackageFile.  # noqa: E501
        :rtype: str
        """
        return self._sha512

    @sha512.setter
    def sha512(self, sha512):
        """Sets the sha512 of this PackageFile.


        :param sha512: The sha512 of this PackageFile.  # noqa: E501
        :type: str
        """

        self._sha512 = sha512

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
        if issubclass(PackageFile, dict):
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
        if not isinstance(other, PackageFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageFile):
            return True

        return self.to_dict() != other.to_dict()
