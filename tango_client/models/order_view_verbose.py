# coding: utf-8

"""
    Tango Card RaaS API

    <p>Welcome to the RaaS&reg; API – with this RESTful API you can integrate a global reward or incentive program into your app or platform.<br /><br /> This console works in our Sandbox environment. To receive your own credentials or to ask questions, please contact us at <a href=\"mailto:devsupport@tangocard.com\">devsupport@tangocard.com</a>.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from tango_client.configuration import Configuration


class OrderViewVerbose(object):
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
        'account_number': 'str',
        'amount_charged': 'MoneyView',
        'campaign': 'str',
        'created_at': 'str',
        'customer_identifier': 'str',
        'denomination': 'MoneyView',
        'email_subject': 'str',
        'etid': 'str',
        'external_ref_id': 'str',
        'message': 'str',
        'notes': 'str',
        'recipient': 'RecipientInfoView',
        'reference_order_id': 'str',
        'reward': 'RewardView',
        'reward_name': 'str',
        'send_email': 'bool',
        'sender': 'SenderInfoView',
        'status': 'str',
        'utid': 'str'
    }

    attribute_map = {
        'account_identifier': 'accountIdentifier',
        'account_number': 'accountNumber',
        'amount_charged': 'amountCharged',
        'campaign': 'campaign',
        'created_at': 'createdAt',
        'customer_identifier': 'customerIdentifier',
        'denomination': 'denomination',
        'email_subject': 'emailSubject',
        'etid': 'etid',
        'external_ref_id': 'externalRefID',
        'message': 'message',
        'notes': 'notes',
        'recipient': 'recipient',
        'reference_order_id': 'referenceOrderID',
        'reward': 'reward',
        'reward_name': 'rewardName',
        'send_email': 'sendEmail',
        'sender': 'sender',
        'status': 'status',
        'utid': 'utid'
    }

    def __init__(self, account_identifier=None, account_number=None, amount_charged=None, campaign=None, created_at=None, customer_identifier=None, denomination=None, email_subject=None, etid=None, external_ref_id=None, message=None, notes=None, recipient=None, reference_order_id=None, reward=None, reward_name=None, send_email=None, sender=None, status=None, utid=None, _configuration=None):  # noqa: E501
        """OrderViewVerbose - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_identifier = None
        self._account_number = None
        self._amount_charged = None
        self._campaign = None
        self._created_at = None
        self._customer_identifier = None
        self._denomination = None
        self._email_subject = None
        self._etid = None
        self._external_ref_id = None
        self._message = None
        self._notes = None
        self._recipient = None
        self._reference_order_id = None
        self._reward = None
        self._reward_name = None
        self._send_email = None
        self._sender = None
        self._status = None
        self._utid = None
        self.discriminator = None

        self.account_identifier = account_identifier
        self.account_number = account_number
        self.amount_charged = amount_charged
        self.campaign = campaign
        self.created_at = created_at
        self.customer_identifier = customer_identifier
        if denomination is not None:
            self.denomination = denomination
        self.email_subject = email_subject
        self.etid = etid
        if external_ref_id is not None:
            self.external_ref_id = external_ref_id
        self.message = message
        if notes is not None:
            self.notes = notes
        if recipient is not None:
            self.recipient = recipient
        self.reference_order_id = reference_order_id
        self.reward = reward
        self.reward_name = reward_name
        self.send_email = send_email
        if sender is not None:
            self.sender = sender
        self.status = status
        self.utid = utid

    @property
    def account_identifier(self):
        """Gets the account_identifier of this OrderViewVerbose.  # noqa: E501

        Account Identifier  # noqa: E501

        :return: The account_identifier of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this OrderViewVerbose.

        Account Identifier  # noqa: E501

        :param account_identifier: The account_identifier of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_identifier is None:
            raise ValueError("Invalid value for `account_identifier`, must not be `None`")  # noqa: E501

        self._account_identifier = account_identifier

    @property
    def account_number(self):
        """Gets the account_number of this OrderViewVerbose.  # noqa: E501

        Account Number  # noqa: E501

        :return: The account_number of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this OrderViewVerbose.

        Account Number  # noqa: E501

        :param account_number: The account_number of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def amount_charged(self):
        """Gets the amount_charged of this OrderViewVerbose.  # noqa: E501

        Amount Charged  # noqa: E501

        :return: The amount_charged of this OrderViewVerbose.  # noqa: E501
        :rtype: MoneyView
        """
        return self._amount_charged

    @amount_charged.setter
    def amount_charged(self, amount_charged):
        """Sets the amount_charged of this OrderViewVerbose.

        Amount Charged  # noqa: E501

        :param amount_charged: The amount_charged of this OrderViewVerbose.  # noqa: E501
        :type: MoneyView
        """
        if self._configuration.client_side_validation and amount_charged is None:
            raise ValueError("Invalid value for `amount_charged`, must not be `None`")  # noqa: E501

        self._amount_charged = amount_charged

    @property
    def campaign(self):
        """Gets the campaign of this OrderViewVerbose.  # noqa: E501

        Reward Campaign  # noqa: E501

        :return: The campaign of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this OrderViewVerbose.

        Reward Campaign  # noqa: E501

        :param campaign: The campaign of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and campaign is None:
            raise ValueError("Invalid value for `campaign`, must not be `None`")  # noqa: E501

        self._campaign = campaign

    @property
    def created_at(self):
        """Gets the created_at of this OrderViewVerbose.  # noqa: E501

        Created Date  # noqa: E501

        :return: The created_at of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrderViewVerbose.

        Created Date  # noqa: E501

        :param created_at: The created_at of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def customer_identifier(self):
        """Gets the customer_identifier of this OrderViewVerbose.  # noqa: E501

        Customer Identifier  # noqa: E501

        :return: The customer_identifier of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._customer_identifier

    @customer_identifier.setter
    def customer_identifier(self, customer_identifier):
        """Sets the customer_identifier of this OrderViewVerbose.

        Customer Identifier  # noqa: E501

        :param customer_identifier: The customer_identifier of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_identifier is None:
            raise ValueError("Invalid value for `customer_identifier`, must not be `None`")  # noqa: E501

        self._customer_identifier = customer_identifier

    @property
    def denomination(self):
        """Gets the denomination of this OrderViewVerbose.  # noqa: E501

        Denomination  # noqa: E501

        :return: The denomination of this OrderViewVerbose.  # noqa: E501
        :rtype: MoneyView
        """
        return self._denomination

    @denomination.setter
    def denomination(self, denomination):
        """Sets the denomination of this OrderViewVerbose.

        Denomination  # noqa: E501

        :param denomination: The denomination of this OrderViewVerbose.  # noqa: E501
        :type: MoneyView
        """

        self._denomination = denomination

    @property
    def email_subject(self):
        """Gets the email_subject of this OrderViewVerbose.  # noqa: E501

        Email Subject  # noqa: E501

        :return: The email_subject of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this OrderViewVerbose.

        Email Subject  # noqa: E501

        :param email_subject: The email_subject of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email_subject is None:
            raise ValueError("Invalid value for `email_subject`, must not be `None`")  # noqa: E501

        self._email_subject = email_subject

    @property
    def etid(self):
        """Gets the etid of this OrderViewVerbose.  # noqa: E501

        Reward Email Template  # noqa: E501

        :return: The etid of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._etid

    @etid.setter
    def etid(self, etid):
        """Sets the etid of this OrderViewVerbose.

        Reward Email Template  # noqa: E501

        :param etid: The etid of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and etid is None:
            raise ValueError("Invalid value for `etid`, must not be `None`")  # noqa: E501

        self._etid = etid

    @property
    def external_ref_id(self):
        """Gets the external_ref_id of this OrderViewVerbose.  # noqa: E501

        External Reference ID  # noqa: E501

        :return: The external_ref_id of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._external_ref_id

    @external_ref_id.setter
    def external_ref_id(self, external_ref_id):
        """Sets the external_ref_id of this OrderViewVerbose.

        External Reference ID  # noqa: E501

        :param external_ref_id: The external_ref_id of this OrderViewVerbose.  # noqa: E501
        :type: str
        """

        self._external_ref_id = external_ref_id

    @property
    def message(self):
        """Gets the message of this OrderViewVerbose.  # noqa: E501

        Email Message  # noqa: E501

        :return: The message of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OrderViewVerbose.

        Email Message  # noqa: E501

        :param message: The message of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def notes(self):
        """Gets the notes of this OrderViewVerbose.  # noqa: E501

        Notes  # noqa: E501

        :return: The notes of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this OrderViewVerbose.

        Notes  # noqa: E501

        :param notes: The notes of this OrderViewVerbose.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def recipient(self):
        """Gets the recipient of this OrderViewVerbose.  # noqa: E501

        Recipient Details  # noqa: E501

        :return: The recipient of this OrderViewVerbose.  # noqa: E501
        :rtype: RecipientInfoView
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this OrderViewVerbose.

        Recipient Details  # noqa: E501

        :param recipient: The recipient of this OrderViewVerbose.  # noqa: E501
        :type: RecipientInfoView
        """

        self._recipient = recipient

    @property
    def reference_order_id(self):
        """Gets the reference_order_id of this OrderViewVerbose.  # noqa: E501

        Reference Order ID  # noqa: E501

        :return: The reference_order_id of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, reference_order_id):
        """Sets the reference_order_id of this OrderViewVerbose.

        Reference Order ID  # noqa: E501

        :param reference_order_id: The reference_order_id of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reference_order_id is None:
            raise ValueError("Invalid value for `reference_order_id`, must not be `None`")  # noqa: E501

        self._reference_order_id = reference_order_id

    @property
    def reward(self):
        """Gets the reward of this OrderViewVerbose.  # noqa: E501

        The Reward  # noqa: E501

        :return: The reward of this OrderViewVerbose.  # noqa: E501
        :rtype: RewardView
        """
        return self._reward

    @reward.setter
    def reward(self, reward):
        """Sets the reward of this OrderViewVerbose.

        The Reward  # noqa: E501

        :param reward: The reward of this OrderViewVerbose.  # noqa: E501
        :type: RewardView
        """
        if self._configuration.client_side_validation and reward is None:
            raise ValueError("Invalid value for `reward`, must not be `None`")  # noqa: E501

        self._reward = reward

    @property
    def reward_name(self):
        """Gets the reward_name of this OrderViewVerbose.  # noqa: E501

        Reward Name  # noqa: E501

        :return: The reward_name of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._reward_name

    @reward_name.setter
    def reward_name(self, reward_name):
        """Sets the reward_name of this OrderViewVerbose.

        Reward Name  # noqa: E501

        :param reward_name: The reward_name of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reward_name is None:
            raise ValueError("Invalid value for `reward_name`, must not be `None`")  # noqa: E501

        self._reward_name = reward_name

    @property
    def send_email(self):
        """Gets the send_email of this OrderViewVerbose.  # noqa: E501

        Send Email?  # noqa: E501

        :return: The send_email of this OrderViewVerbose.  # noqa: E501
        :rtype: bool
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        """Sets the send_email of this OrderViewVerbose.

        Send Email?  # noqa: E501

        :param send_email: The send_email of this OrderViewVerbose.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and send_email is None:
            raise ValueError("Invalid value for `send_email`, must not be `None`")  # noqa: E501

        self._send_email = send_email

    @property
    def sender(self):
        """Gets the sender of this OrderViewVerbose.  # noqa: E501

        Sender Details  # noqa: E501

        :return: The sender of this OrderViewVerbose.  # noqa: E501
        :rtype: SenderInfoView
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this OrderViewVerbose.

        Sender Details  # noqa: E501

        :param sender: The sender of this OrderViewVerbose.  # noqa: E501
        :type: SenderInfoView
        """

        self._sender = sender

    @property
    def status(self):
        """Gets the status of this OrderViewVerbose.  # noqa: E501

        Reward Status  # noqa: E501

        :return: The status of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderViewVerbose.

        Reward Status  # noqa: E501

        :param status: The status of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def utid(self):
        """Gets the utid of this OrderViewVerbose.  # noqa: E501

        Utid - Unique Tango Card ID.  # noqa: E501

        :return: The utid of this OrderViewVerbose.  # noqa: E501
        :rtype: str
        """
        return self._utid

    @utid.setter
    def utid(self, utid):
        """Sets the utid of this OrderViewVerbose.

        Utid - Unique Tango Card ID.  # noqa: E501

        :param utid: The utid of this OrderViewVerbose.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and utid is None:
            raise ValueError("Invalid value for `utid`, must not be `None`")  # noqa: E501

        self._utid = utid

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
        if issubclass(OrderViewVerbose, dict):
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
        if not isinstance(other, OrderViewVerbose):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderViewVerbose):
            return True

        return self.to_dict() != other.to_dict()
