import connexion
import six

from openapi_server.models.legitimate_person import LegitimatePerson  # noqa: E501
from openapi_server.models.update_legitimate_person import UpdateLegitimatePerson  # noqa: E501
from openapi_server import util


def delete_legitimate_person(device_mac):  # noqa: E501
    """Delete the legitimate person info.

    Delete the legitimate person given a device MAC. # noqa: E501

    :param device_mac: Legitimate person&#39;s Device MAC
    :type device_mac: str

    :rtype: str
    """
    return 'do some magic!'


def get_all_legitimate_person_info():  # noqa: E501
    """Return all the information of each legitimate person

    Return information of all the legitimate people # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def get_legitimate_person_info(device_mac):  # noqa: E501
    """Return info of a legitimate person given a device MAC

    Return information of a legitimate person given MAC device # noqa: E501

    :param device_mac: Legitimate person&#39;s Device MAC
    :type device_mac: str

    :rtype: str
    """
    return 'do some magic!'


def post_legitimate_person(legitimate_person):  # noqa: E501
    """Add a new legitimate person

    Addition of a new legitimate person # noqa: E501

    :param legitimate_person: 
    :type legitimate_person: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        legitimate_person = LegitimatePerson.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_legitimate_person(update_legitimate_person):  # noqa: E501
    """Update a device MAC

    Update a legitimate person # noqa: E501

    :param update_legitimate_person: 
    :type update_legitimate_person: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        update_legitimate_person = UpdateLegitimatePerson.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
