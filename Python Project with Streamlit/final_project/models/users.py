"""
XINYI WANG
CS 5001, Fall 2023
Class Users
"""
import requests

class Users:
    '''
    User model
    '''
    def __init__(self):
        self.users = []
        self.categories = []
    
    def fetch_users(self):
        '''
        Fetch all users from the API
        '''
        url = 'https://fakestoreapi.com/users'
        try:
            response =requests. get(url) #make an HTTP Get request
            data =response.json()  # Convert JSON string to dictionary
        except requests.exceptions.ConnectionError:
            return
        if response.status_code != 200:
            return
        self.users =data


    def filter_users_by_geolocation(self, target_latitude, target_longitude):
        """
        filters the users based on their geolocation.
        It returns a list of users whose geolocation matches the given latitude and longitude.

        Parameters:
        target_latitude (str): The latitude to filter users by.
        target_longitude (str): The longitude to filter users by.

        Returns:
        list: A list of users who are located at the given latitude and longitude.
        """

        # Initialize an empty list to store users 
        matching_users = []

        # For Loop through each user 
        for user in self.users:
            # get the latitude and longitude of the current user
            user_latitude = user['address']['geolocation']['lat']
            user_longitude = user['address']['geolocation']['long']

            # Check if the user's latitude and longitude could match 
            if user_latitude == target_latitude and user_longitude == target_longitude:
               # If so, add the user to the list of matching users
                matching_users.append(user)

        # Return the list of matching users
        return matching_users
