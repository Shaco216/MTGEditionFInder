import requests
from bs4 import BeautifulSoup

cardname = ""

def scrape_for_card(cardname):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    #to find exactly that card you need to use ["name"] in the searchbar of the website
    #but the link will change [ to %5B and ] to %5D ""stay the same on addressbar but not in python ( see example )
    #space will be a +
    #example https://www.cardmarket.com/en/Magic/Products/Search?searchString=%5B%22sliverqueen%5B%22

    #cardname = '%5B"'+cardname+'"%5D'

    #probably the cardname is not correct because if i use a copyied link like this one https://www.cardmarket.com/de/Magic/Products/Search?searchString=sliverqueen it is working
    #as i thought the lenght of cardname is 1 character to long
    cardname = cardname[0:len(cardname)-1]
    #problem solved with line 18

    link = "https://www.cardmarket.com/de/Magic/Products/Search?searchString="+str(cardname)
    print(link)
    link = str(link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    print(soup)

def get_Expansion_from_Soup(soup):
    pass

if __name__ == "__main__":
    scrape_for_card(cardname)