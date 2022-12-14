# coding: utf-8

"""
    Tango Card RaaS API

    <5. Ordersp>Welcome to the RaaS&reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.<br /><br /> This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at <a href=\"mailto:devsupport@tangocard.com\">devsupport@tangocard.com</a>.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from tango_client.configuration import Configuration


class CredentialView(object):
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
        'credential_type': 'str',
        'label': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'credential_type': 'credentialType',
        'label': 'label',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, credential_type=None, label=None, type=None, value=None, _configuration=None):  # noqa: E501
        """CredentialView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential_type = None
        self._label = None
        self._type = None
        self._value = None
        self.discriminator = None

        if credential_type is not None:
            self.credential_type = credential_type
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def credential_type(self):
        """Gets the credential_type of this CredentialView.  # noqa: E501


        :return: The credential_type of this CredentialView.  # noqa: E501
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """Sets the credential_type of this CredentialView.


        :param credential_type: The credential_type of this CredentialView.  # noqa: E501
        :type: str
        """

        self._credential_type = credential_type

    @property
    def label(self):
        """Gets the label of this CredentialView.  # noqa: E501


        :return: The label of this CredentialView.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CredentialView.


        :param label: The label of this CredentialView.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this CredentialView.  # noqa: E501


        :return: The type of this CredentialView.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredentialView.


        :param type: The type of this CredentialView.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this CredentialView.  # noqa: E501


        :return: The value of this CredentialView.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CredentialView.


        :param value: The value of this CredentialView.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(CredentialView, dict):
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
        if not isinstance(other, CredentialView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CredentialView):
            return True

        return self.to_dict() != other.to_dict()
