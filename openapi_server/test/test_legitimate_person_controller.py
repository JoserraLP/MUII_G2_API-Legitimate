# coding: utf-8

from __future__ import absolute_import

from unittest import mock

from flask import json

from openapi_server.models.legitimate_person import LegitimatePerson  # noqa: E501
from openapi_server.models.update_legitimate_person import UpdateLegitimatePerson  # noqa: E501
from openapi_server.test import BaseTestCase


class TestLegitimatePersonController(BaseTestCase):
    """LegitimatePersonController integration test stubs"""

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.delete_legitimate_person")
    def test_delete_legitimate_person(self, mocked_delete_legitimate_person):
        """Test case for delete_legitimate_person

        Delete the legitimate person info.
        """
        mocked_delete_legitimate_person.assert_not_called()
        mocked_delete_legitimate_person.return_value = None
        response = self.client.open(
            '/legitimate_person/{device_mac}'.format(device_mac="ff:ff:ff:ff:ff"),
            method='DELETE')
        mocked_delete_legitimate_person.assert_called_once()

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_all_legitimate_person_info")
    def test_get_all_legitimate_person_info(self, mocked_get_all_legitimate_person_info):
        """Test case for get_all_legitimate_person_info

        Return all the information of each legitimate person
        """
        mocked_get_all_legitimate_person_info.assert_not_called()
        mocked_get_all_legitimate_person_info.return_value = [
            [1,
             "ff:ff:ff:ff:ff",
             "user",
             "123546789",
             True,
             "ASDKASD"]
        ]
        response = self.client.open(
            '/legitimate_person',
            method='GET')
        mocked_get_all_legitimate_person_info.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_legitimate_person_info")
    def test_get_legitimate_person_info(self, mocked_get_legitimate_person_info):
        """Test case for get_legitimate_person_info

        Return info of a legitimate person given a device MAC
        """
        mocked_get_legitimate_person_info.assert_not_called()
        mocked_get_legitimate_person_info.return_value = [
            [1,
             "ff:ff:ff:ff:ff",
             "user",
             "123546789",
             True,
             "ASDKASD"],
            [2,
             "00:00:00:ff:ff",
             "user1",
             "123546789",
             False,
             "ASDKAasdasdSD"],
            [3,
             "00:00:ff:00:00",
             "usee2",
             "123546789",
             False,
             "AS201D1K56A76S1D"]
        ]
        response = self.client.open(
            '/legitimate_person/{device_mac}'.format(device_mac="ff:ff:ff:ff:ff"),
            method='GET')
        mocked_get_legitimate_person_info.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.add_legitimate_person")
    def test_post_legitimate_person(self, mocked_add_legitimate_person):
        """Test case for post_legitimate_person

        Add a new legitimate person
        """
        mocked_add_legitimate_person.assert_not_called()
        mocked_add_legitimate_person.return_value = None
        legitimate_person = LegitimatePerson()
        response = self.client.open(
            '/legitimate_person',
            method='POST',
            data=json.dumps(legitimate_person),
            content_type='application/json')
        mocked_add_legitimate_person.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.update_legitimate_person")
    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_legitimate_person_info")
    def test_put_legitimate_person(self, mocked_get_legitimate_person_info, mocked_update_legitimate_person):
        """Test case for put_legitimate_person

        Update a device MAC
        """
        mocked_get_legitimate_person_info.assert_not_called()
        mocked_update_legitimate_person.assert_not_called()
        mocked_update_legitimate_person.return_value = None
        mocked_get_legitimate_person_info.return_value = [
            [1,
             "ff:ff:ff:ff:ff",
             "user",
             "123546789",
             True,
             "ASDKASD"]
        ]
        update_legitimate_person = UpdateLegitimatePerson()
        response = self.client.open(
            '/legitimate_person',
            method='PUT',
            data=json.dumps(update_legitimate_person),
            content_type='application/json')
        mocked_get_legitimate_person_info.assert_called_once()
        mocked_update_legitimate_person.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
