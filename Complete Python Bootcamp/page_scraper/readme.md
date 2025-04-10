# Final Capstone Project: <br> Web Scraper: Link Finder

This Python script extracts all the valid HTTP/HTTPS links from a given webpage. It uses the `requests` library to fetch the content of a webpage and `BeautifulSoup` from the `bs4` package to parse and extract the links.

## Requirements

To run this script, you'll need the following Python packages:

- `requests`
- `beautifulsoup4`

These dependencies can be installed using the `requirements.txt` file.


## Script Functionality

### link_finder(beautiful_soup)
This function accepts a BeautifulSoup object and finds all the valid links on the webpage. It filters out invalid links (those not starting with 'http' or 'https') and returns a formatted string with the valid links.

## Usage Flow

1. The script prompts the user to enter a URL.
2. It sends a GET request to that URL.
3. It parses the webpage using BeautifulSoup to extract the links.
4. It prints the valid links found on the page.