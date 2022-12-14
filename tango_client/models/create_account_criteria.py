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


class CreateAccountCriteria(object):
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
        'account_identifier': 'str',
        'contact_email': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'contact_email': 'contactEmail',
        'display_name': 'displayName'
    }

    def __init__(self, account_identifier=None, contact_email=None, display_name=None, _configuration=None):  # noqa: E501
        """CreateAccountCriteria - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_identifier = None
        self._contact_email = None
        self._display_name = None
        self.discriminator = None

        self.account_identifier = account_identifier
        self.contact_email = contact_email
        self.display_name = display_name

    @property
    def account_identifier(self):
        """Gets the account_identifier of this CreateAccountCriteria.  # noqa: E501

        Account Identifier  # noqa: E501

        :return: The account_identifier of this CreateAccountCriteria.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this CreateAccountCriteria.

        Account Identifier  # noqa: E501

        :param account_identifier: The account_identifier of this CreateAccountCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def contact_email(self):
        """Gets the contact_email of this CreateAccountCriteria.  # noqa: E501

        Email  # noqa: E501

        :return: The contact_email of this CreateAccountCriteria.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this CreateAccountCriteria.

        Email  # noqa: E501

        :param contact_email: The contact_email of this CreateAccountCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def display_name(self):
        """Gets the display_name of this CreateAccountCriteria.  # noqa: E501

        Display Name  # noqa: E501

        :return: The display_name of this CreateAccountCriteria.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateAccountCriteria.

        Display Name  # noqa: E501

        :param display_name: The display_name of this CreateAccountCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

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
        if issubclass(CreateAccountCriteria, dict):
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
        if not isinstance(other, CreateAccountCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAccountCriteria):
            return True

        return self.to_dict() != other.to_dict()
