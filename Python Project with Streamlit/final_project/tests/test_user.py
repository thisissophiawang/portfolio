"""
XINYI WANG
CS 5001, Fall 2023
Unitest for User class
"""
#python3 -m unittest tests.test_user


from unittest import TestCase
from unittest.mock import patch
from models.users import Users
import requests

class test_user(TestCase):
    '''
    Unit test for User class
    '''
    def test_user_fetch(self):
        user = Users()
        with patch('models.users.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = [
        {
        "address": {
            "geolocation": {"lat": "-37.3159", "long": "81.1496"}, 
            "city": "kilcoole",
            "street": "new road",
            "number": 7682, 
            "zipcode": "12926-3874"
            },
            "id": 1,
            "email": "sophia2013@gmail.com",
            "username": "sophiaaaa",
            "password": "van74nyc",
            "name": {"firstname": "Sophia", "lastname": "Wang"},
              "phone": "1-123-456-7899",
              "__v": 0
        },
            ]
            user.fetch_users()
            self.assertIsNotNone(user.users)    #checking if users are fectched
            self.assertEqual(len(user.users), 1)    #checking if the number of users are correct
            self.assertEqual(user.users[0]['name']['firstname'], 'Sophia')  #checking if user's first name is correct
            self.assertEqual(user.users[0]['name']['lastname'], 'Wang')    #checking if user's last name is correct


    # writing the serve down test
    def test_user_fetch_with_connection_error(self):
        user = Users()
        with patch('models.users.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError
            user.fetch_users()
            self.assertEqual(len(user.users), 0)    


    # writing the “non-200 status code” test
    def test_user_fetch_with_status_code_not_200(self):
        user = Users()
        with patch('models.users.requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            user.fetch_users()
            self.assertEqual(len(user.users), 0)


    # writing the “bad status message” test
    def test_user_fetch_bad_status(self):
        user = Users()
        with patch('models.users.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            user.fetch_users()
            self.assertEqual(len(user.users), 0)


            