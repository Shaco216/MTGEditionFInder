from Cardsearcher import *
import tkinter as tk
from tkinter import *
from Pricesearcher import *

#variablen
Expansionlist = []
Expansions_till_14 = []

#Mainwindow
Mainwindow = Tk()
Mainwindow.title("MTGEditionFInder")

#Functions
def show_info(cardname, Expansionlist):
    #Expansions_till_14 = [] gehört zu lösung 1

    # variable
    cardnamevariable = StringVar()
    expansionsvariable = StringVar()
    #cardname wird als Stringvar für das label cardname gespeichert
    #Die Variablen, die in der GUI verwendet werden müssen zwingend in der selben datei sein
    soup = get_soup(cardname)
    Expansionlist = get_Expansion_from_Soup(soup)

    cardnamevariable.set(cardname)

    # Labels des Mainwindows
    LabelCardname_plaintext = Label(master=Mainwindow, text="cardname", width=30)
    LabelCardname_plaintext.pack()

    LabelCardname = Label(master=Mainwindow, textvariable=cardnamevariable, width=30)
    LabelCardname.pack()

    LabelExpansions_plaintext = Label(master=Mainwindow, text="Expansions", width=30)
    LabelExpansions_plaintext.pack()

    #search prices
    editionurls = get_all_editionurls(soup)
    print(editionurls)

    #expansions as a listbox
    Expansionlistbox = Listbox(Mainwindow)
    Expansionlistbox.pack()
    #fill list with items
    for item in Expansionlist:
        Expansionlistbox.insert(END,item)




#buttons and bars
Cardsearchbar = Text(master= Mainwindow, name="please enter cardname", height=1, width=50)
Cardsearchbar.pack()
Button_Submit = Button(master= Mainwindow, command= lambda: [scrape_for_card(Cardsearchbar.get("1.0", END)),show_info(Cardsearchbar.get("1.0", END), Expansionlist)], text="Find", height=1, width=5)
Button_Submit.pack()

mainloop()


