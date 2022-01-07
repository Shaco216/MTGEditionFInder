import requests
from bs4 import BeautifulSoup

soup = ""

def get_all_editionurls(soup):
    urls = []
    Expansionurls = []
    Substring = "Expansions"
    for link in soup.findAll('a'):
        urls.append(link.get('href'))
    Expansions = [link for link in urls if Substring in str(link)]
    for item in Expansions:
        item = "https://www.cardmarket.com" + str(item)
        Expansionurls.append(item)
    return Expansionurls

if __name__ == "__main__":
    get_all_editionurls(soup)