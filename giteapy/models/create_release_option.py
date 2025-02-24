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


class CreateReleaseOption(object):
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
        'body': 'str',
        'draft': 'bool',
        'name': 'str',
        'prerelease': 'bool',
        'tag_name': 'str',
        'target_commitish': 'str'
    }

    attribute_map = {
        'body': 'body',
        'draft': 'draft',
        'name': 'name',
        'prerelease': 'prerelease',
        'tag_name': 'tag_name',
        'target_commitish': 'target_commitish'
    }

    def __init__(self, body=None, draft=None, name=None, prerelease=None, tag_name=None, target_commitish=None, _configuration=None):  # noqa: E501
        """CreateReleaseOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._draft = None
        self._name = None
        self._prerelease = None
        self._tag_name = None
        self._target_commitish = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if draft is not None:
            self.draft = draft
        if name is not None:
            self.name = name
        if prerelease is not None:
            self.prerelease = prerelease
        self.tag_name = tag_name
        if target_commitish is not None:
            self.target_commitish = target_commitish

    @property
    def body(self):
        """Gets the body of this CreateReleaseOption.  # noqa: E501


        :return: The body of this CreateReleaseOption.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateReleaseOption.


        :param body: The body of this CreateReleaseOption.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def draft(self):
        """Gets the draft of this CreateReleaseOption.  # noqa: E501


        :return: The draft of this CreateReleaseOption.  # noqa: E501
        :rtype: bool
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this CreateReleaseOption.


        :param draft: The draft of this CreateReleaseOption.  # noqa: E501
        :type: bool
        """

        self._draft = draft

    @property
    def name(self):
        """Gets the name of this CreateReleaseOption.  # noqa: E501


        :return: The name of this CreateReleaseOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateReleaseOption.


        :param name: The name of this CreateReleaseOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prerelease(self):
        """Gets the prerelease of this CreateReleaseOption.  # noqa: E501


        :return: The prerelease of this CreateReleaseOption.  # noqa: E501
        :rtype: bool
        """
        return self._prerelease

    @prerelease.setter
    def prerelease(self, prerelease):
        """Sets the prerelease of this CreateReleaseOption.


        :param prerelease: The prerelease of this CreateReleaseOption.  # noqa: E501
        :type: bool
        """

        self._prerelease = prerelease

    @property
    def tag_name(self):
        """Gets the tag_name of this CreateReleaseOption.  # noqa: E501


        :return: The tag_name of this CreateReleaseOption.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this CreateReleaseOption.


        :param tag_name: The tag_name of this CreateReleaseOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and tag_name is None:
            raise ValueError("Invalid value for `tag_name`, must not be `None`")  # noqa: E501

        self._tag_name = tag_name

    @property
    def target_commitish(self):
        """Gets the target_commitish of this CreateReleaseOption.  # noqa: E501


        :return: The target_commitish of this CreateReleaseOption.  # noqa: E501
        :rtype: str
        """
        return self._target_commitish

    @target_commitish.setter
    def target_commitish(self, target_commitish):
        """Sets the target_commitish of this CreateReleaseOption.


        :param target_commitish: The target_commitish of this CreateReleaseOption.  # noqa: E501
        :type: str
        """

        self._target_commitish = target_commitish

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
        if issubclass(CreateReleaseOption, dict):
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
        if not isinstance(other, CreateReleaseOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateReleaseOption):
            return True

        return self.to_dict() != other.to_dict()
