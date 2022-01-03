import requests
from bs4 import BeautifulSoup

cardname = ""

def scrape_for_card(cardname):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    cardname = '["' + cardname + '"]'
    link = "https://www.cardmarket.com/de/Magic/Products/Search?searchString=" + cardname
    print(link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    print(soup)

def get_Expansion_from_Soup(soup):
    pass

if __name__ == "__main__":
    scrape_for_card(cardname)