<h1 align="center">Final Capstone Project: <br> Web Scraper: Link Finder</h1>

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

## Example

```bash
Enter URL: https://commons.wikimedia.org/wiki/Main_Page
Links found:
https://aa.wikipedia.org/wiki/Main_Page
https://ab.wikipedia.org/wiki/%D0%98%D1%85%D0%B0%D0%B4%D0%BE%D1%83_%D0%B0%D0%B4%D0%B0%D2%9F%D1%8C%D0%B0
https://ace.wikipedia.org/wiki/%C3%94n_Keue
https://ady.wikipedia.org/wiki/%D0%9D%D1%8D%D0%BA%D3%80%D1%83%D0%B1%D0%B3%D1%8A%D0%BE_%D1%88%D1%8A%D1%85%D1%8C%D0%B0%D3%80
https://af.wikipedia.org/wiki/Tuisblad
https://als.wikipedia.org/wiki/Wikipedia:Houptsyte
https://alt.wikipedia.org/wiki/%D0%A2%D3%A7%D1%81_%D0%B1%D3%B1%D0%BA
https://am.wikipedia.org/wiki/%E1%8B%8B%E1%8A%93%E1%8B%8D_%E1%8C%88%E1%8C%BD
https://ami.wikipedia.org/wiki/Sa%E2%80%99ayayaw_pising_no_tyin-naw
https://an.wikipedia.org/wiki/Portalada
https://ang.wikipedia.org/wiki/Heafodtramet
https://ann.wikipedia.org/wiki/Uwu
https://anp.wikipedia.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A5%8D%E0%A4%AF_%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0
https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A9_%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D8%A9
https://arc.wikipedia.org/wiki/%DC%A6%DC%90%DC%AC%DC%90_%DC%AA%DC%9D%DC%AB%DC%9D%DC%AC%DC%90
https://ary.wikipedia.org/wiki/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A9_%D8%A7%D9%84%D9%84%D9%88%D9%84%D8%A7
https://arz.wikipedia.org/wiki/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D9%87_%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D9%87
https://as.wikipedia.org/wiki/%E0%A6%AC%E0%A7%87%E0%A6%9F%E0%A7%81%E0%A6%AA%E0%A6%BE%E0%A6%A4
https://ast.wikipedia.org/wiki/Portada
https://atj.wikipedia.org/wiki/Otitikowin
...
