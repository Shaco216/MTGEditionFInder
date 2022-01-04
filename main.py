from Cardsearcher import *
import tkinter as tk
from tkinter import *

#Mainwindow
Mainwindow = Tk()
Mainwindow.title("MTGEditionFInder")
Cardsearchbar = Text(master= Mainwindow, name="please enter cardname", height=1, width=50)
Cardsearchbar.pack()
Button_Submit = Button(master= Mainwindow, command= lambda: scrape_for_card(Cardsearchbar.get("1.0", END)), text="Find", height=1, width=5)
Button_Submit.pack()
mainloop()