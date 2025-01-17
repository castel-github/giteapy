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


class Reference(object):
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
        'object': 'GitObject',
        'ref': 'str',
        'url': 'str'
    }

    attribute_map = {
        'object': 'object',
        'ref': 'ref',
        'url': 'url'
    }

    def __init__(self, object=None, ref=None, url=None, _configuration=None):  # noqa: E501
        """Reference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._object = None
        self._ref = None
        self._url = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if ref is not None:
            self.ref = ref
        if url is not None:
            self.url = url

    @property
    def object(self):
        """Gets the object of this Reference.  # noqa: E501


        :return: The object of this Reference.  # noqa: E501
        :rtype: GitObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Reference.


        :param object: The object of this Reference.  # noqa: E501
        :type: GitObject
        """

        self._object = object

    @property
    def ref(self):
        """Gets the ref of this Reference.  # noqa: E501


        :return: The ref of this Reference.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this Reference.


        :param ref: The ref of this Reference.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def url(self):
        """Gets the url of this Reference.  # noqa: E501


        :return: The url of this Reference.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Reference.


        :param url: The url of this Reference.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Reference, dict):
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
        if not isinstance(other, Reference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Reference):
            return True

        return self.to_dict() != other.to_dict()
