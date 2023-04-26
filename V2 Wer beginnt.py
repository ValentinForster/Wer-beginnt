import random
from tkinter import *

gleichstand = ["Falls Gleichstand: männlich\n",
               "Falls Gleichstand: weiblich\n"] # knopf falls gleichstand mit neuer Frage

akku = ["Wer hat am meisten Akku?\n",
        "Wer hat am wenigsten Akku?\n",
        "Wessen Akku ist am\nnähesten an 50%?\n"]

kleidung = ["Wer hat die hellste Hose?\n",
            "Wer hat die dunkelste Hose?\n",
            "Wer hat das hellste Oberteil?\n",
            "Wer hat das dunkelste Oberteil?\n",
            "Wer trägt heute am\nmeisten Schwarz?\n"]

aufstehen = ["Wer ist heute am\nfrühesten aufgestanden?\n",
             "Wer ist heute am\nspätesten aufgestanden?\n"]

zuletzt = ["Wer war zuletzt irgendwo einkaufen?\n",
           "Wer war zuletzt Haare schneiden?\n"]

himmelsrichtungen = ["Wer sitzt am nördlichsten?\n",
                     "Wer sitzt am östlichsten?\n",
                     "Wer sitzt am westlichsten?\n",
                     "Wer sitzt am südlichsten?\n"]

geburtstag = ["Wer hat als nächstes Geburtstag?\n",
              "Wer hatte als letztes Geburtstag?\n"]

glas = ["Wer hat am wenigsten\nin seinem Glas?\n",
        "Wer hat am meisten\nin seinem Glas?\n"]

fingernägel = ["Wer hat die längsten Fingernägel?\n",
               "Wer hat die kürzesten Fingernägel?\n"]

anfahrt = ["Der Gastgeber beginnt\n(falls mehrere: weiblich)\n",
           "Der Gastgeber beginnt\n(falls mehrere: männlich)\n",
           "Wer hatte den längsten Anfahrtsweg?\n"]

Alle_Ideen = [akku,
              kleidung,
              aufstehen,
              zuletzt,
              himmelsrichtungen,
              geburtstag,
              glas,
              fingernägel,
              anfahrt,
              "Wer hat als letztes\ndas Haus betreten?\n",
              "Ohne auf die Uhr zu schauen, wer\nschätzt die Uhrzeit am genauesten?\n",
              "Wer hat das Spiel bisher\nam seltensten gespielt?\n"]

button_counter = 0

def pick():
    the_pick = random.choice(Alle_Ideen)
    global tiebreak_contenders
    global button_counter
    tiebreak_contenders = Alle_Ideen.remove(the_pick)
    if type(the_pick) == list:
        the_pick = random.choice(the_pick)
    if button_counter == 0:
        l3 = Label(root, text=the_pick, bg=background_color, fg='white', font="Verdana 10 bold")
        l3.pack()
    elif button_counter == 1:
        l4 = Label(root, text=the_pick, bg=background_color, fg='white', font="Verdana 10 bold")
        l4.pack()
    elif button_counter == 2:
        l5 = Label(root, text=the_pick, bg=background_color, fg='white', font="Verdana 10 bold")
        l5.pack()
    elif button_counter == 3:
        l6 = Label(root, text=the_pick, bg=background_color, fg='white', font="Verdana 10 bold")
        l6.pack()
    elif button_counter == 4:
        l7 = Label(root, text=the_pick, bg=background_color, fg='white', font="Verdana 10 bold")
        l7.pack()
    elif button_counter == 5:
        l8 = Label(root, text=the_pick, bg=background_color, fg='white', font="Verdana 10 bold")
        l8.pack()
    else:
        go_button.pack_forget()
    button_counter += 1

def changeText():
    go_button['text'] = 'Go'

def tiebreak():
    global tiebreak_contenders
    tie_the_pick = random.choice(tiebreak_contenders)
    if type(tie_the_pick) == list:
        tie_the_pick = random.choice(tie_the_pick)
    print(the_pick)

# -----------------------------------------------------------------

background_color = '#212121'
button_color = "#f52222"
active_button_color = '#cf1d1d'
active_button_text = '#d4d2d2'

root = Tk()
root.title("Wer fängt an?")
root.configure(background=background_color)

l0 = Label(root, text='', bg=background_color)
l0.pack()
l1 = Label(root, text='Wer fängt an?', bg=background_color, fg='white', font = "Verdana 20 bold")
l1.pack()
l2 = Label(root, text='\n', bg=background_color)
l2.pack()

l_bottom = Label(root, text='\n', bg=background_color)
l_bottom.pack(side=BOTTOM)

l_bottom2 = Label(root, text='\n', bg=background_color)
l_bottom2.pack(side=BOTTOM)

go_button = Button(root, text="Go", command=lambda:[pick(), changeText()], fg='white', bg=button_color,
                   font = "Verdana 14 bold", height=2, width=8, activebackground=active_button_color,
                   activeforeground=active_button_text)
go_button.pack(side=BOTTOM)

l_over_button = Label(root, text='\n', bg=background_color)
l_over_button.pack(side=BOTTOM)

root.mainloop()

