# Your name: Bemnet, Sarah, Yeajee
# Group name: 404 error

from bs4 import BeautifulSoup
import re
import os
import csv
import unittest

def load_listing_results(html_file): 
    """
    INPUT: A string containing the path of the html file
    RETURN: A list of tuples
    """

    with open(html_file, "r", encoding="utf-8-sig") as file:
            content = file.read()
            soup = BeautifulSoup(content, "html.parser")

            listings = []
            
            listing_containers = soup.find_all("div", class_="c1d4ry4s dir dir-ltr")
            
            for listing in listing_containers:
                title = None
                listing_id = None
                
                if listing.find("h2", class_="hnwb2pb dir dir-ltr"):
                    title = listing.find("h2", class_="hnwb2pb dir dir-ltr").text.strip()
                else:
                    title = "No Title Available"
                    
                if listing.get("data-id"):
                    listing_id = listing.get("data-id")
                else:
                    listing_id = "No ID Available"

                if title != "No Title Available" and listing_id != "No ID Available":
                    listings.append((title, listing_id))

    return listings
