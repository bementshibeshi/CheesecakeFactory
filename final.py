# Your name: Bemnet, Sarah, Yeajee
# Group name: 404 error

from bs4 import BeautifulSoup
import re
import os
import csv
import unittest
import requests

def load_menu_items(html_file): 
    """
    INPUT: A string containing the path of the html file
    RETURN: A list of tuples
    """

    with open(html_file, "r", encoding="utf-8-sig") as file:
            content = file.read()
            soup = BeautifulSoup(content, "html.parser")

            product_title = []
            
            food_containers = soup.find_all("div", class_="c-product-card__info__container")
            
            for food in food_containers:
                title = None
                
                if food.find("span", class_="c-product-card__name"):
                    title = food.find("span", class_="c-product-card__name").text.strip()
                else:
                    title = "No Title Available"

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
