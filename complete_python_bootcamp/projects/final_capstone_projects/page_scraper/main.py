from os import link

import requests
from bs4 import BeautifulSoup


def link_finder(beautiful_soup):
    """
    Extracts all valid HTTP/HTTPS links from the provided BeautifulSoup object.

    This function searches through the parsed HTML content for all anchor (<a>) tags that have an 'href'
    attribute. It collects links that start with "http" or "https" into a list. If no valid links are
    found or the webpage is inaccessible, the function returns a message indicating that no links were found.
    Otherwise, it returns a formatted string containing all the found links, with each link on a new line.

    Parameters:
        beautiful_soup (BeautifulSoup): A BeautifulSoup object representing the parsed HTML content of a webpage.

    Returns:
        str: A formatted string listing all valid HTTP/HTTPS links found, or a message stating that no links were found.
    """

    links: list = []
    for link in beautiful_soup.find_all(
        "a", href=True
    ):  # href=True ensures that we only get valid links
        l = link["href"]
        if l.startswith("http") or l.startswith("https"):
            links.append(l)

    if len(links) == 0:
        return "No links found or webpage is inaccessible."
    else:
        return f"Links found:' '\n' {'\n'.join(links)}"


# Send a GET request to the URL
response = requests.get(input("Enter URL: "))

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

print(link_finder(soup))
