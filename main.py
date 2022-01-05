from Cardsearcher import *
import tkinter as tk
from tkinter import *

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
    Expansionlist = get_Expansion_from_Soup(get_soup(cardname))

    cardnamevariable.set(cardname)

    # Labels des Mainwindows
    LabelCardname_plaintext = Label(master=Mainwindow, text="cardname", width=30)
    LabelCardname_plaintext.pack()

    LabelCardname = Label(master=Mainwindow, textvariable=cardnamevariable, width=30)
    LabelCardname.pack()

    LabelExpansions_plaintext = Label(master=Mainwindow, text="Expansions", width=30)
    LabelExpansions_plaintext.pack()

    expansionsvariable.set(str(Expansionlist))
    LabelExpansions = Label(master=Mainwindow, textvariable=expansionsvariable)
    LabelExpansions.pack()

    #lösung 1 funktioniert nicht
    #for i in range(len(Expansionlist)):
    #    #only 14 items
    #    if i % 14 and not i == 0:
    #        if len(Expansions_till_14) > 0:
    #            expansionsvariable.set(Expansions_till_14)
    #            LabelExpansions = Label(master=Mainwindow, textvariable=expansionsvariable)
    #            LabelExpansions.pack()
    #        Expansions_till_14 = []
    #    else:
    #        Expansions_till_14.append(Expansionlist[i])




#buttons and bars
Cardsearchbar = Text(master= Mainwindow, name="please enter cardname", height=1, width=50)
Cardsearchbar.pack()
Button_Submit = Button(master= Mainwindow, command= lambda: [scrape_for_card(Cardsearchbar.get("1.0", END)),show_info(Cardsearchbar.get("1.0", END), Expansionlist)], text="Find", height=1, width=5)
Button_Submit.pack()

mainloop()


