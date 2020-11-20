# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LegitimatePerson(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, person_mac=None, person_name=None, person_phone_number=None, notification=None, dest_mac=None):  # noqa: E501
        """LegitimatePerson - a model defined in OpenAPI

        :param person_mac: The person_mac of this LegitimatePerson.  # noqa: E501
        :type person_mac: List[str]
        :param person_name: The person_name of this LegitimatePerson.  # noqa: E501
        :type person_name: str
        :param person_phone_number: The person_phone_number of this LegitimatePerson.  # noqa: E501
        :type person_phone_number: str
        :param notification: The notification of this LegitimatePerson.  # noqa: E501
        :type notification: bool
        :param dest_mac: The dest_mac of this LegitimatePerson.  # noqa: E501
        :type dest_mac: str
        """
        self.openapi_types = {
            'person_mac': List[str],
            'person_name': str,
            'person_phone_number': str,
            'notification': bool,
            'dest_mac': str
        }

        self.attribute_map = {
            'person_mac': 'person_MAC',
            'person_name': 'person_name',
            'person_phone_number': 'person_phone_number',
            'notification': 'notification',
            'dest_mac': 'dest_MAC'
        }

        self._person_mac = person_mac
        self._person_name = person_name
        self._person_phone_number = person_phone_number
        self._notification = notification
        self._dest_mac = dest_mac

    @classmethod
    def from_dict(cls, dikt) -> 'LegitimatePerson':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LegitimatePerson of this LegitimatePerson.  # noqa: E501
        :rtype: LegitimatePerson
        """
        return util.deserialize_model(dikt, cls)

    @property
    def person_mac(self):
        """Gets the person_mac of this LegitimatePerson.


        :return: The person_mac of this LegitimatePerson.
        :rtype: List[str]
        """
        return self._person_mac

    @person_mac.setter
    def person_mac(self, person_mac):
        """Sets the person_mac of this LegitimatePerson.


        :param person_mac: The person_mac of this LegitimatePerson.
        :type person_mac: List[str]
        """

        self._person_mac = person_mac

    @property
    def person_name(self):
        """Gets the person_name of this LegitimatePerson.


        :return: The person_name of this LegitimatePerson.
        :rtype: str
        """
        return self._person_name

    @person_name.setter
    def person_name(self, person_name):
        """Sets the person_name of this LegitimatePerson.


        :param person_name: The person_name of this LegitimatePerson.
        :type person_name: str
        """

        self._person_name = person_name

    @property
    def person_phone_number(self):
        """Gets the person_phone_number of this LegitimatePerson.


        :return: The person_phone_number of this LegitimatePerson.
        :rtype: str
        """
        return self._person_phone_number

    @person_phone_number.setter
    def person_phone_number(self, person_phone_number):
        """Sets the person_phone_number of this LegitimatePerson.


        :param person_phone_number: The person_phone_number of this LegitimatePerson.
        :type person_phone_number: str
        """

        self._person_phone_number = person_phone_number

    @property
    def notification(self):
        """Gets the notification of this LegitimatePerson.


        :return: The notification of this LegitimatePerson.
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this LegitimatePerson.


        :param notification: The notification of this LegitimatePerson.
        :type notification: bool
        """

        self._notification = notification

    @property
    def dest_mac(self):
        """Gets the dest_mac of this LegitimatePerson.


        :return: The dest_mac of this LegitimatePerson.
        :rtype: str
        """
        return self._dest_mac

    @dest_mac.setter
    def dest_mac(self, dest_mac):
        """Sets the dest_mac of this LegitimatePerson.


        :param dest_mac: The dest_mac of this LegitimatePerson.
        :type dest_mac: str
        """

        self._dest_mac = dest_mac
