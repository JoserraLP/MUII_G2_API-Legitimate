import connexion
import six

from openapi_server.models.legitimate_person import LegitimatePerson  # noqa: E501
from openapi_server.models.update_legitimate_person import UpdateLegitimatePerson  # noqa: E501
from openapi_server import util

import os
import psycopg2

DATABASE_PWD = os.environ['DATABASE_PWD']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_DB = os.environ['DATABASE_DB']
DATABASE_HOST = os.environ['DATABASE_HOST']

def delete_legitimate_person(device_mac):  # noqa: E501
    """Delete the legitimate person info.

    Delete the legitimate person given a device MAC. # noqa: E501

    :param device_mac: Legitimate person&#39;s Device MAC
    :type device_mac: str

    :rtype: str
    """
    conn = psycopg2.connect(user=DATABASE_USER,
                            password=DATABASE_PWD,
                            host=DATABASE_HOST,
                            database=DATABASE_DB, sslmode='require')
    cursor = conn.cursor()
    
    try:
        
        query = "DELETE FROM legitimate WHERE %s = ANY(person_mac)"

        print("Deleting rows from legitimate table")
        cursor.execute(query, (device_mac, ))

        conn.commit()
        
        return "Record deleted successfully"

    except (Exception, psycopg2.Error) as error :
        return "Error while deleting data from PostgreSQL. Error => {}".format(error)

    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def get_all_legitimate_person_info():  # noqa: E501
    """Return all the information of each legitimate person

    Return information of all the legitimate people # noqa: E501


    :rtype: str
    """
    conn = psycopg2.connect(user=DATABASE_USER,
                            password=DATABASE_PWD,
                            host=DATABASE_HOST,
                            database=DATABASE_DB, sslmode='require')
    cursor = conn.cursor()
    
    try:

        
        query = "SELECT * FROM legitimate"

        cursor.execute(query)
        print("Selecting rows from legitimate table using cursor.fetchall")
        legitimate_records = cursor.fetchall() 
        
        data = {"legitimate" : []}
        for row in legitimate_records:
            data['legitimate'].append(
                {
                    "id": row[0],
                    "person_MAC": row[1],
                    "person_name": row[2],
                    "person_phone_number": row[3],
                    "notification": row[4],
                    "dest_MAC": row[5]
                }
            )
            

        return data

    except (Exception, psycopg2.Error) as error :
        return "Error while fetching data from PostgreSQL. Error => {}".format(error)

    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def get_legitimate_person_info(device_mac):  # noqa: E501
    """Return info of a legitimate person given a device MAC

    Return information of a legitimate person given MAC device # noqa: E501

    :param device_mac: Legitimate person&#39;s Device MAC
    :type device_mac: str

    :rtype: str
    """
    conn = psycopg2.connect(user=DATABASE_USER,
                            password=DATABASE_PWD,
                            host=DATABASE_HOST,
                            database=DATABASE_DB, sslmode='require')
    cursor = conn.cursor()
    
    try:

        query = "SELECT * FROM legitimate WHERE %s = ANY(person_mac)"

        cursor.execute(query, (device_mac, ))
        print("Selecting rows from legitimate table using cursor.fetchall")
        legitimate_records = cursor.fetchall() 
        
        data = {"legitimate" : []}
        for row in legitimate_records:
            data['legitimate'].append(
                {
                    "id": row[0],
                    "person_MAC": row[1],
                    "person_name": row[2],
                    "person_phone_number": row[3],
                    "notification": row[4],
                    "dest_MAC": row[5]
                }
            )
            
        return data

    except (Exception, psycopg2.Error) as error :
        return "Error while fetching data from PostgreSQL. Error => {}".format(error)

    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def post_legitimate_person(legitimate_person):  # noqa: E501
    """Add a new legitimate person

    Addition of a new legitimate person # noqa: E501

    :param legitimate_person: 
    :type legitimate_person: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        legitimate_person = LegitimatePerson.from_dict(connexion.request.get_json())  # noqa: E501

    conn = psycopg2.connect(user=DATABASE_USER,
                            password=DATABASE_PWD,
                            host=DATABASE_HOST,
                            database=DATABASE_DB, sslmode='require')
    cursor = conn.cursor()

    try:

        query = """ INSERT INTO legitimate (person_mac, person_name, person_phone_number, notification, dest_mac) VALUES (%s,%s,%s,%s,%s)"""
        legitimate_data = (legitimate_person.person_mac, legitimate_person.person_name, legitimate_person.person_phone_number, legitimate_person.notification, legitimate_person.dest_mac)
        cursor.execute(query, legitimate_data)

        conn.commit()
        count = cursor.rowcount
        return "Record inserted successfully into legitimate table"

    except (Exception, psycopg2.Error) as error :
        if conn:
            return "Failed to insert record into legitimate table. Error =>  {}".format(error)
    
    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def put_legitimate_person(update_legitimate_person):  # noqa: E501
    """Update a device MAC

    Update a legitimate person # noqa: E501

    :param update_legitimate_person: 
    :type update_legitimate_person: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        update_legitimate_person = UpdateLegitimatePerson.from_dict(connexion.request.get_json())  # noqa: E501

    conn = psycopg2.connect(user=DATABASE_USER,
                            password=DATABASE_PWD,
                            host=DATABASE_HOST,
                            database=DATABASE_DB, sslmode='require')
    cursor = conn.cursor()

    try:

        query = "SELECT * FROM legitimate WHERE %s = ANY(person_mac)"

        cursor.execute(query, (update_legitimate_person.old_mac, ))
        legitimate_records = cursor.fetchone()

        # Delete previous MAC
        prev_mac = legitimate_records[1]
        
        print("#")
        print(prev_mac)
        
        prev_mac.remove(update_legitimate_person.old_mac)
        print("##")
        print(prev_mac)

        # Add new MAC
        prev_mac.append(update_legitimate_person.new_mac)

        print("###")
        print(prev_mac)

        query = """ UPDATE legitimate set person_mac = %s WHERE %s = ANY(person_mac)"""
        legitimate_data = (prev_mac, update_legitimate_person.old_mac)
        cursor.execute(query, legitimate_data)

        conn.commit()
        count = cursor.rowcount
        return "Record updated successfully into legitimate table"

    except (Exception, psycopg2.Error) as error :
        if conn:
            return "Failed to update record into legitimate table. Error =>  {}".format(error)
    
    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
