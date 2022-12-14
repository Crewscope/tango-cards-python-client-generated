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


class CreateCreditCardCriteria(object):
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
        'billing_address': 'BillingAddressCriteria',
        'contact_information': 'list[ContactInformationCriteria]',
        'credit_card': 'CreditCardCriteria',
        'customer_identifier': 'str',
        'ip_address': 'str',
        'label': 'str'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'billing_address': 'billingAddress',
        'contact_information': 'contactInformation',
        'credit_card': 'creditCard',
        'customer_identifier': 'customerIdentifier',
        'ip_address': 'ipAddress',
        'label': 'label'
    }

    def __init__(self, account_identifier=None, billing_address=None, contact_information=None, credit_card=None, customer_identifier=None, ip_address=None, label=None, _configuration=None):  # noqa: E501
        """CreateCreditCardCriteria - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_identifier = None
        self._billing_address = None
        self._contact_information = None
        self._credit_card = None
        self._customer_identifier = None
        self._ip_address = None
        self._label = None
        self.discriminator = None

        self.account_identifier = account_identifier
        self.billing_address = billing_address
        if contact_information is not None:
            self.contact_information = contact_information
        self.credit_card = credit_card
        self.customer_identifier = customer_identifier
        self.ip_address = ip_address
        self.label = label

    @property
    def account_identifier(self):
        """Gets the account_identifier of this CreateCreditCardCriteria.  # noqa: E501

        Account Identifier  # noqa: E501

        :return: The account_identifier of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this CreateCreditCardCriteria.

        Account Identifier  # noqa: E501

        :param account_identifier: The account_identifier of this CreateCreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def billing_address(self):
        """Gets the billing_address of this CreateCreditCardCriteria.  # noqa: E501

        Billing Address  # noqa: E501

        :return: The billing_address of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: BillingAddressCriteria
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this CreateCreditCardCriteria.

        Billing Address  # noqa: E501

        :param billing_address: The billing_address of this CreateCreditCardCriteria.  # noqa: E501
        :type: BillingAddressCriteria
        """
        if self._configuration.client_side_validation and billing_address is None:
            raise ValueError("Invalid value for `billing_address`, must not be `None`")  # noqa: E501

        self._billing_address = billing_address

    @property
    def contact_information(self):
        """Gets the contact_information of this CreateCreditCardCriteria.  # noqa: E501

        Contact Information  # noqa: E501

        :return: The contact_information of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: list[ContactInformationCriteria]
        """
        return self._contact_information

    @contact_information.setter
    def contact_information(self, contact_information):
        """Sets the contact_information of this CreateCreditCardCriteria.

        Contact Information  # noqa: E501

        :param contact_information: The contact_information of this CreateCreditCardCriteria.  # noqa: E501
        :type: list[ContactInformationCriteria]
        """

        self._contact_information = contact_information

    @property
    def credit_card(self):
        """Gets the credit_card of this CreateCreditCardCriteria.  # noqa: E501

        Credit Card Information  # noqa: E501

        :return: The credit_card of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: CreditCardCriteria
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """Sets the credit_card of this CreateCreditCardCriteria.

        Credit Card Information  # noqa: E501

        :param credit_card: The credit_card of this CreateCreditCardCriteria.  # noqa: E501
        :type: CreditCardCriteria
        """
        if self._configuration.client_side_validation and credit_card is None:
            raise ValueError("Invalid value for `credit_card`, must not be `None`")  # noqa: E501

        self._credit_card = credit_card

    @property
    def customer_identifier(self):
        """Gets the customer_identifier of this CreateCreditCardCriteria.  # noqa: E501

        Customer Identifier  # noqa: E501

        :return: The customer_identifier of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._customer_identifier

    @customer_identifier.setter
    def customer_identifier(self, customer_identifier):
        """Sets the customer_identifier of this CreateCreditCardCriteria.

        Customer Identifier  # noqa: E501

        :param customer_identifier: The customer_identifier of this CreateCreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_identifier is None:
            raise ValueError("Invalid value for `customer_identifier`, must not be `None`")  # noqa: E501

        self._customer_identifier = customer_identifier

    @property
    def ip_address(self):
        """Gets the ip_address of this CreateCreditCardCriteria.  # noqa: E501

        IP Address  # noqa: E501

        :return: The ip_address of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this CreateCreditCardCriteria.

        IP Address  # noqa: E501

        :param ip_address: The ip_address of this CreateCreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def label(self):
        """Gets the label of this CreateCreditCardCriteria.  # noqa: E501

        Credit Card Label  # noqa: E501

        :return: The label of this CreateCreditCardCriteria.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CreateCreditCardCriteria.

        Credit Card Label  # noqa: E501

        :param label: The label of this CreateCreditCardCriteria.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

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
        if issubclass(CreateCreditCardCriteria, dict):
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
        if not isinstance(other, CreateCreditCardCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCreditCardCriteria):
            return True

        return self.to_dict() != other.to_dict()
