from os import link

import requests
from bs4 import BeautifulSoup

def link_finder(beautiful_soup):
    """"
    This function finds all the links in the given webpage.
    """
    links = []

    for link in beautiful_soup.find_all('a', href=True):  # href=True ensures that we only get valid links
        if link['href'].startswith('http') or link['href'].startswith('https'):
            links.append(link['href'])

    return f"Links found:' '\n' {'\n'.join(links)}"

# Send a GET request to the URL
response = requests.get(input('Enter URL: '))
response.raise_for_status()  # Raise an exception for 4xx/5xx responses

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

print(link_finder(soup))