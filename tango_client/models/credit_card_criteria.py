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


class CreditCardCriteria(object):
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
        'expiration': 'str',
        'number': 'str',
        'verification_number': 'str'
    }

    attribute_map = {
        'expiration': 'expiration',
        'number': 'number',
        'verification_number': 'verificationNumber'
    }

    def __init__(self, expiration=None, number=None, verification_number=None, _configuration=None):  # noqa: E501
        """CreditCardCriteria - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expiration = None
        self._number = None
        self._verification_number = None
        self.discriminator = None

        self.expiration = expiration
        self.number = number
        self.verification_number = verification_number

    @property
    def expiration(self):
        """Gets the expiration of this CreditCardCriteria.  # noqa: E501

        Expiration Date  # noqa: E501

        :return: The expiration of this CreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this CreditCardCriteria.

        Expiration Date  # noqa: E501

        :param expiration: The expiration of this CreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and expiration is None:
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    @property
    def number(self):
        """Gets the number of this CreditCardCriteria.  # noqa: E501

        Credit Card Number  # noqa: E501

        :return: The number of this CreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreditCardCriteria.

        Credit Card Number  # noqa: E501

        :param number: The number of this CreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def verification_number(self):
        """Gets the verification_number of this CreditCardCriteria.  # noqa: E501

        Verification Number  # noqa: E501

        :return: The verification_number of this CreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._verification_number

    @verification_number.setter
    def verification_number(self, verification_number):
        """Sets the verification_number of this CreditCardCriteria.

        Verification Number  # noqa: E501

        :param verification_number: The verification_number of this CreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and verification_number is None:
            raise ValueError("Invalid value for `verification_number`, must not be `None`")  # noqa: E501

        self._verification_number = verification_number

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
        if issubclass(CreditCardCriteria, dict):
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
        if not isinstance(other, CreditCardCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditCardCriteria):
            return True

        return self.to_dict() != other.to_dict()
