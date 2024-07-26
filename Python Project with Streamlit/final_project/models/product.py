"""
XINYI WANG
CS 5001, Fall 2023
Class Product
"""
import requests

class Product:
    '''
    Product model
    '''
    def __init__(self):
        self.product = []
        self.categories = []
    
    def fetch_products(self):
        '''
        Fetch all product
        '''
        url = 'https://fakestoreapi.com/products'
        try:
            response =requests. get(url) #make an HTTP Get request
            data =response.json()  # Convert JSON string to dictionary
        except requests.exceptions.ConnectionError:
            return
        if response.status_code != 200:
            return
        self.products =data   # store the list of products
 

    def fetch_categories(self):
        '''
        Fetch all categories
        '''
        url = 'https://fakestoreapi.com/products/categories'
        try:
            response = requests.get(url) #make an HTTP Get request
            data = response.json()  # Convert JSON string to dictionary
        except requests.exceptions.ConnectionError:
            return
        if response.status_code != 200:
            return
        self.categories = data





