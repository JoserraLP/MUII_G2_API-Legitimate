# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.legitimate_person import LegitimatePerson  # noqa: E501
from openapi_server.models.update_legitimate_person import UpdateLegitimatePerson  # noqa: E501
from openapi_server.test import BaseTestCase


class TestLegitimatePersonController(BaseTestCase):
    """LegitimatePersonController integration test stubs"""

    def test_delete_legitimate_person(self):
        """Test case for delete_legitimate_person

        Delete the legitimate person info.
        """
        response = self.client.open(
            '/legitimate_person/{device_mac}'.format(device_mac=ff:ff:ff:ff:ff),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_legitimate_person_info(self):
        """Test case for get_all_legitimate_person_info

        Return all the information of each legitimate person
        """
        response = self.client.open(
            '/legitimate_person',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_legitimate_person_info(self):
        """Test case for get_legitimate_person_info

        Return info of a legitimate person given a device MAC
        """
        response = self.client.open(
            '/legitimate_person/{device_mac}'.format(device_mac=ff:ff:ff:ff:ff),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_legitimate_person(self):
        """Test case for post_legitimate_person

        Add a new legitimate person
        """
        legitimate_person = LegitimatePerson()
        response = self.client.open(
            '/legitimate_person',
            method='POST',
            data=json.dumps(legitimate_person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_legitimate_person(self):
        """Test case for put_legitimate_person

        Update a device MAC
        """
        update_legitimate_person = UpdateLegitimatePerson()
        response = self.client.open(
            '/legitimate_person',
            method='PUT',
            data=json.dumps(update_legitimate_person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
