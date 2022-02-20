import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

#global
global soup
#local variable
cardname = ""
soup = ""
tcg_option = 0

def replace_space_with_plus_cardname(cardname):
    # leerzeichen abfangen/ umwandeln in +
    space = " "
    if space in cardname:
        cardname = cardname.replace(" ", "+")
    return cardname

def get_soup(cardname, tcg_option):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # to find exactly that card you need to use ["name"] in the searchbar of the website
    # but the link will change [ to %5B and ] to %5D ""stay the same on addressbar but not in python ( see example )
    # space will be a +
    # example https://www.cardmarket.com/en/Magic/Products/Search?searchString=%5B%22sliverqueen%5B%22

    # cardname = '%5B"'+cardname+'"%5D'

    # probably the cardname is not correct because if i use a copyied link like this one https://www.cardmarket.com/de/Magic/Products/Search?searchString=sliverqueen it is working
    # as i thought the lenght of cardname is 1 character to long
    cardname = cardname[0:len(cardname) - 1]
    # problem solved with line 18
    cardname = replace_space_with_plus_cardname(cardname)
    if tcg_option == 1:
        link = "https://www.cardmarket.com/de/Magic/Products/Search?searchString=%5B" + str(cardname) + "%5D"
    elif tcg_option == 2:
        link = "https://www.cardmarket.com/de/YuGiOh/Products/Search?searchString=%5B" + str(cardname) + "%5D"
    print(link)
    link = str(link)
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")

    return soup

def scrape_for_card(cardname, tcg_option):
    global Expansionlist

    cardname = replace_space_with_plus_cardname(cardname)

    soup = get_soup(cardname, tcg_option)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # to find exactly that card you need to use ["name"] in the searchbar of the website
    # but the link will change [ to %5B and ] to %5D ""stay the same on addressbar but not in python ( see example )
    # space will be a +
    # example https://www.cardmarket.com/en/Magic/Products/Search?searchString=%5B%22sliverqueen%5B%22

    # cardname = '%5B"'+cardname+'"%5D'

    # probably the cardname is not correct because if i use a copyied link like this one https://www.cardmarket.com/de/Magic/Products/Search?searchString=sliverqueen it is working
    # as i thought the lenght of cardname is 1 character to long
    cardname = cardname[0:len(cardname) - 1]
    # problem solved with line 18
    if tcg_option == 1:
        link = "https://www.cardmarket.com/de/Magic/Products/Search?searchString=" + str(cardname)
    elif tcg_option == 2:
        link = "https://www.cardmarket.com/de/YuGiOh/Products/Search?searchString=" + str(cardname)

    link = str(link)
    #req = requests.get(link, headers=headers)
    #soup = BeautifulSoup(req.content, "html.parser")

    Expansionlist = get_Expansion_from_Soup(soup, tcg_option)

    print("Cardname: " + cardname + "\nExpansionlist")
    print(Expansionlist)

def get_Expansion_from_Soup(soup, tcg_option):
    links = []
    Substring = "Expansions"

    for link in soup.findAll('a'):
        links.append(link.get('href'))

    #checking if list(links) contains a Substring
    Expansionlist = [link for link in links if Substring in str(link)]
    #https://www.kite.com/python/answers/how-to-check-if-a-list-contains-a-substring-in-python#:~:text=Use%20any()%20to%20check,the%20list%20contains%20the%20substring.&text=Alternatively%2C%20use%20a%20list%20comprehension,element%20that%20contains%20the%20substring.
    #WICHTIG: in dem link www.kite.com/... wird nicht erwähnt, dass (in diesem fall) link kein string ist und deshalb nicht mit einem substring
    #verglichen werden kann! deshalb str(link) (s. https://stackoverflow.com/questions/47464211/what-does-the-x-for-x-in-syntax-mean )

    Expansions = []
    for Expansion in Expansionlist:
        if tcg_option == 1:
            Expansion = str(Expansion).replace("/de/Magic/Expansions/","")
        elif tcg_option == 2:
            Expansion = str(Expansion).replace("/de/YuGiOh/Expansions/", "")
        Expansions.append(Expansion)

    return Expansions

if __name__ == "__main__":
    get_soup(cardname, tcg_option)
    scrape_for_card(cardname, tcg_option)
    get_Expansion_from_Soup(soup, tcg_option)
    replace_space_with_plus_cardname(cardname)