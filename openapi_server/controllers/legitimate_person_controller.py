import connexion
from muii_g2_family_lock_database.Database import PostgresDB

from openapi_server.models.legitimate_person import LegitimatePerson  # noqa: E501
from openapi_server.models.update_legitimate_person import UpdateLegitimatePerson  # noqa: E501

def delete_legitimate_person(device_mac):  # noqa: E501
    """Delete the legitimate person info.

    Delete the legitimate person given a device MAC. # noqa: E501

    :param device_mac: Legitimate person&#39;s Device MAC
    :type device_mac: str

    :rtype: str
    """
    db = PostgresDB()
    error = db.delete_legitimate_person(device_mac)
    if error:
        return error
    return "Record deleted successfully"


def get_all_legitimate_person_info():  # noqa: E501
    """Return all the information of each legitimate person

    Return information of all the legitimate people # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    legitimate_records = db.get_all_legitimate_person_info()
    if "Error" in legitimate_records:
        return legitimate_records
    data = {"legitimate": []}
    for row in legitimate_records:
        data['legitimate'].append(
            {
                "id": row[0],
                "person_MAC": row[1],
                "person_name": row[2],
                "person_phone_number": row[3],
                "notification": row[4],
                "relation": row[5]
            }
        )

    return data


def get_legitimate_person_info(device_mac):  # noqa: E501
    """Return info of a legitimate person given a device MAC

    Return information of a legitimate person given MAC device # noqa: E501

    :param device_mac: Legitimate person&#39;s Device MAC
    :type device_mac: str

    :rtype: str
    """
    db = PostgresDB()
    legitimate_person_info = db.get_legitimate_person_info(device_mac)
    if "Error" in legitimate_person_info:
        return legitimate_person_info
    data = {"legitimate": []}
    for row in legitimate_person_info:
        data['legitimate'].append(
            {
                "id": row[0],
                "person_MAC": row[1],
                "person_name": row[2],
                "person_phone_number": row[3],
                "notification": row[4],
                "relation": row[5]
            }
        )

    return data


def post_legitimate_person(legitimate_person):  # noqa: E501
    """Add a new legitimate person

    Addition of a new legitimate person # noqa: E501

    :param legitimate_person: 
    :type legitimate_person: dict | bytes

    :rtype: str
    """

    if connexion.request.is_json:
        legitimate_person = LegitimatePerson.from_dict(connexion.request.get_json())  # noqa: E501

    db = PostgresDB()
    error = db.add_legitimate_person(legitimate_person.person_mac, legitimate_person.person_name,
                                     legitimate_person.person_phone_number,
                                     legitimate_person.notification, legitimate_person.relation)
    if error:
        return error
    return "Record inserted successfully into legitimate table"


def put_legitimate_person(update_legitimate_person):  # noqa: E501
    """Update a device MAC

    Update a legitimate person # noqa: E501

    :param update_legitimate_person: 
    :type update_legitimate_person: dict | bytes

    :rtype: str
    """
    db = PostgresDB()

    if connexion.request.is_json:
        update_legitimate_person = UpdateLegitimatePerson.from_dict(connexion.request.get_json())  # noqa: E501

    legitimate_person = db.get_legitimate_person_info(update_legitimate_person.old_mac)
    if "Error" in legitimate_person:
        return legitimate_person

    # Delete previous MAC
    prev_mac = legitimate_person[0][1]
    prev_mac.remove(update_legitimate_person.old_mac)

    # Add new MAC
    prev_mac.append(update_legitimate_person.new_mac)
    error = db.update_legitimate_person(prev_mac, update_legitimate_person.old_mac)
    if error:
        return error
    return "Record updated successfully into legitimate table"
