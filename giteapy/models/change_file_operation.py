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


class ChangeFileOperation(object):
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
        'content': 'str',
        'from_path': 'str',
        'operation': 'str',
        'path': 'str',
        'sha': 'str'
    }

    attribute_map = {
        'content': 'content',
        'from_path': 'from_path',
        'operation': 'operation',
        'path': 'path',
        'sha': 'sha'
    }

    def __init__(self, content=None, from_path=None, operation=None, path=None, sha=None, _configuration=None):  # noqa: E501
        """ChangeFileOperation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._from_path = None
        self._operation = None
        self._path = None
        self._sha = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if from_path is not None:
            self.from_path = from_path
        self.operation = operation
        self.path = path
        if sha is not None:
            self.sha = sha

    @property
    def content(self):
        """Gets the content of this ChangeFileOperation.  # noqa: E501

        new or updated file content, must be base64 encoded  # noqa: E501

        :return: The content of this ChangeFileOperation.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ChangeFileOperation.

        new or updated file content, must be base64 encoded  # noqa: E501

        :param content: The content of this ChangeFileOperation.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def from_path(self):
        """Gets the from_path of this ChangeFileOperation.  # noqa: E501

        old path of the file to move  # noqa: E501

        :return: The from_path of this ChangeFileOperation.  # noqa: E501
        :rtype: str
        """
        return self._from_path

    @from_path.setter
    def from_path(self, from_path):
        """Sets the from_path of this ChangeFileOperation.

        old path of the file to move  # noqa: E501

        :param from_path: The from_path of this ChangeFileOperation.  # noqa: E501
        :type: str
        """

        self._from_path = from_path

    @property
    def operation(self):
        """Gets the operation of this ChangeFileOperation.  # noqa: E501

        indicates what to do with the file  # noqa: E501

        :return: The operation of this ChangeFileOperation.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ChangeFileOperation.

        indicates what to do with the file  # noqa: E501

        :param operation: The operation of this ChangeFileOperation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["create", "update", "delete"]  # noqa: E501
        if (self._configuration.client_side_validation and
                operation not in allowed_values):
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def path(self):
        """Gets the path of this ChangeFileOperation.  # noqa: E501

        path to the existing or new file  # noqa: E501

        :return: The path of this ChangeFileOperation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ChangeFileOperation.

        path to the existing or new file  # noqa: E501

        :param path: The path of this ChangeFileOperation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def sha(self):
        """Gets the sha of this ChangeFileOperation.  # noqa: E501

        sha is the SHA for the file that already exists, required for update or delete  # noqa: E501

        :return: The sha of this ChangeFileOperation.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ChangeFileOperation.

        sha is the SHA for the file that already exists, required for update or delete  # noqa: E501

        :param sha: The sha of this ChangeFileOperation.  # noqa: E501
        :type: str
        """

        self._sha = sha

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
        if issubclass(ChangeFileOperation, dict):
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
        if not isinstance(other, ChangeFileOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeFileOperation):
            return True

        return self.to_dict() != other.to_dict()
