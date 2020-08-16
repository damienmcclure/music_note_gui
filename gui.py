from tkinter import *
from sounds import *
import time

root = Tk()

notesPlayed = []


def aClicked():
    notesPlayed.append("a2()")
def bClicked():
    notesPlayed.append("b2()")
def cClicked():
    notesPlayed.append("c3()")
def dClicked():
    notesPlayed.append("d3()")
def eClicked():
    notesPlayed.append("e3()")
def fClicked():
    notesPlayed.append("f3()")
def gClicked():
    notesPlayed.append("g3()")



def paste():
    print(notesPlayed)

def save():
    f = open("songfile.py", "w")
    f.write("import winsound\n")
    f.write("from sounds import *\n")
    f.write("import time\n")
    f.write("\n")
    for element in notesPlayed:
        f.write(element)
        f.write("\n")
    f.close()

exitButton = Button(root, text=" X ", padx=50, pady=50, command=lambda:[root.quit(), paste()], fg="white", bg="red")
exitButton.pack()

aButton = Button(root, text="A2", padx=50, pady=50, command=lambda:[a2(), aClicked()], bg="red")
aButton.pack()

bButton = Button(root, text="B2", padx=50, pady=50, command=lambda:[b2(), bClicked()], bg="orange")
bButton.pack()

cButton = Button(root, text="C3", padx=50, pady=50, command=lambda:[c3(), cClicked()], bg="yellow")
cButton.pack()

dButton = Button(root, text="D3", padx=50, pady=50, command=lambda:[d3(), dClicked()], bg="green")
dButton.pack()

eButton = Button(root, text="E3", padx=50, pady=50, command=lambda:[e3(), eClicked()], bg="blue")
eButton.pack()

fButton = Button(root, text="F3", padx=50, pady=50, command=lambda:[f3(), fClicked()], bg="#4B0082")
fButton.pack()

gButton = (Button(root, text="G3", padx=50, pady=50, command=lambda:[g3(), gClicked()], bg="#8F00FF"))
gButton.pack()

saveButton = (Button(root, text="Save", padx=50, pady=50, command=save))
saveButton.pack()

root.mainloop()
