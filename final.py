# Your name: Bemnet, Sarah, Yeajee
# Group name: 404 error

from bs4 import BeautifulSoup
import re
import os
import csv
import unittest
import requests

def load_menu_items(soup): 
    """
    INPUT: A string containing the path of the html file
    RETURN: A list of tuples
    """

 
    product_title = []
    
    food_containers = soup.find_all("div", class_="c-product-card__info__container")
    
    for food in food_containers:
        title = food.find("span", class_="c-product-card__name")
            
        if title:
            product_title.append(title.text.strip())
        else:
            product_title.append("No Title Available")

    print(product_title)
    return product_title

def main():
    # Task 1: Create a BeautifulSoup object.
    url = "https://www.thecheesecakefactory.com/menu"
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else: 
        print("Failed to retrieve the web page.")
        return
    

class TestAllFunctions(unittest.TestCase):
    def setUp(self):
        soup = BeautifulSoup(requests.get("https://www.thecheesecakefactory.com/menu").text, 'html.parser')
        self.menu_items = load_menu_items(soup)

    def test_load_menu_items(self):
        
        self.assertEqual(type(self.menu_items), list)


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)