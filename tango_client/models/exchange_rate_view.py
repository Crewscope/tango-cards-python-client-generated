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


class ExchangeRateView(object):
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
        'base_currency': 'str',
        'base_fx': 'float',
        'last_modified_date': 'str',
        'reward_currency': 'str'
    }

    attribute_map = {
        'base_currency': 'baseCurrency',
        'base_fx': 'baseFx',
        'last_modified_date': 'lastModifiedDate',
        'reward_currency': 'rewardCurrency'
    }

    def __init__(self, base_currency=None, base_fx=None, last_modified_date=None, reward_currency=None, _configuration=None):  # noqa: E501
        """ExchangeRateView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_currency = None
        self._base_fx = None
        self._last_modified_date = None
        self._reward_currency = None
        self.discriminator = None

        self.base_currency = base_currency
        self.base_fx = base_fx
        self.last_modified_date = last_modified_date
        self.reward_currency = reward_currency

    @property
    def base_currency(self):
        """Gets the base_currency of this ExchangeRateView.  # noqa: E501

        Base Currency  # noqa: E501

        :return: The base_currency of this ExchangeRateView.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this ExchangeRateView.

        Base Currency  # noqa: E501

        :param base_currency: The base_currency of this ExchangeRateView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and base_currency is None:
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501

        self._base_currency = base_currency

    @property
    def base_fx(self):
        """Gets the base_fx of this ExchangeRateView.  # noqa: E501

        Base Fixed Exchange Rate  # noqa: E501

        :return: The base_fx of this ExchangeRateView.  # noqa: E501
        :rtype: float
        """
        return self._base_fx

    @base_fx.setter
    def base_fx(self, base_fx):
        """Sets the base_fx of this ExchangeRateView.

        Base Fixed Exchange Rate  # noqa: E501

        :param base_fx: The base_fx of this ExchangeRateView.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and base_fx is None:
            raise ValueError("Invalid value for `base_fx`, must not be `None`")  # noqa: E501

        self._base_fx = base_fx

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this ExchangeRateView.  # noqa: E501

        Last Modified Timestamp  # noqa: E501

        :return: The last_modified_date of this ExchangeRateView.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this ExchangeRateView.

        Last Modified Timestamp  # noqa: E501

        :param last_modified_date: The last_modified_date of this ExchangeRateView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_modified_date is None:
            raise ValueError("Invalid value for `last_modified_date`, must not be `None`")  # noqa: E501

        self._last_modified_date = last_modified_date

    @property
    def reward_currency(self):
        """Gets the reward_currency of this ExchangeRateView.  # noqa: E501

        Reward Currency  # noqa: E501

        :return: The reward_currency of this ExchangeRateView.  # noqa: E501
        :rtype: str
        """
        return self._reward_currency

    @reward_currency.setter
    def reward_currency(self, reward_currency):
        """Sets the reward_currency of this ExchangeRateView.

        Reward Currency  # noqa: E501

        :param reward_currency: The reward_currency of this ExchangeRateView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reward_currency is None:
            raise ValueError("Invalid value for `reward_currency`, must not be `None`")  # noqa: E501

        self._reward_currency = reward_currency

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
        if issubclass(ExchangeRateView, dict):
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
        if not isinstance(other, ExchangeRateView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExchangeRateView):
            return True

        return self.to_dict() != other.to_dict()
