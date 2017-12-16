__author__ = 'satyajit'

import requests


class UserProfile():

    def __init__(self):
        pass

    def update_user_profile(self):
        """
        This method used  for update user information like name, age , address etc
        """
        first_name = requests.get('First_Name', '')
        last_name = requests.get('Last_Name', '')
        age = requests.get('Age', '')