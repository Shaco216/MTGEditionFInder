import requests
from bs4 import BeautifulSoup

soup = ""
Expansionurls = []
cardname = ""
filteroption = 0
languageoption = 0
gradingoption = 0

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

def get_prices_from_all_editions(Expansionurls, cardname, filteroption, languageoption, gradingoption):
    #change cardname with space to urlversion with -
    if " " in cardname:
        cardname = cardname.replace(" ","-")

    #filteroptions sellerlocation
    if filteroption > 0 or languageoption > 0 or gradingoption > 0:
        zusatzinfo = "?"
    elif filteroption == 0 or languageoption == 0 or gradingoption == 0:
        zusatzinfo = ""
    #1 de
    #2 en
    if filteroption == 1:
        zusatzinfo = zusatzinfo + "sellerCountry=7"
    elif filteroption == 2:
        zusatzinfo = zusatzinfo + "sellerCountry=13"

    #linkverbindung via &
    if filteroption > 0 and languageoption > 0:
        zusatzinfo = zusatzinfo + "&"

    #languageoptions
    #1 de
    #2 en
    #3 de&en
    if languageoption == 1:
        zusatzinfo = zusatzinfo + "language=3"
    elif languageoption == 2:
        zusatzinfo = zusatzinfo + "language=1"
    elif languageoption == 3:
        zusatzinfo = zusatzinfo +"language=1,3"

    #linkverbindung via &
    if languageoption > 0 and gradingoption > 0:
        zusatzinfo = zusatzinfo + "&"

    #gradingoption
    #1 excellent or higher
    if gradingoption == 1:
        zusatzinfo = zusatzinfo + "minCondition=3"

    pricelist = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    for expURL in Expansionurls:
        fullURL = expURL + "/" + cardname + zusatzinfo
        req = requests.get(fullURL, headers=headers)
        soup = BeautifulSoup(req.content, "html.parser")
        price = soup.find(class_='font-weight-bold color-primary small text-right text-nowrap').text
        pricelist.append(price)
    return pricelist


if __name__ == "__main__":
    get_all_editionurls(soup)
    get_prices_from_all_editions(Expansionurls, cardname, filteroption, languageoption, gradingoption)