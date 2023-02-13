from tkinter import *
from FileHandler import *
from Part import *

a = FileHandler()

existingParts = a.Disassembler()


m = Tk()
m.title('Store')


Label1 = Label(m, text="Choose an object or make a new one to work with.")

Listbox = Listbox(m)

#method for entering the names of parts into the listbox
def namesofParts():
    Listbox.delete(0, END)
    for curPart in range(len(existingParts)):
        Listbox.insert (curPart, existingParts[curPart].model)

namesofParts()

#creating objects

typeLabel = Label(m, text="Type:", justify=LEFT)
modelLabel = Label(m, text="Model:", justify=LEFT)
priceLabel = Label(m, text="Price (EUR):", justify=LEFT)


typeEntry = Entry(m)
modelEntry = Entry(m)
priceEntry = Entry(m)

def DataExtraction():
    dataIndex = Listbox.curselection()[0]
    curPart = existingParts[dataIndex]
    typeEntry.delete(first=0, last=len(typeEntry.get()))
    modelEntry.delete(first=0, last=len(modelEntry.get()))
    priceEntry.delete(first=0, last=len(priceEntry.get()))
    typeEntry.insert(0, curPart.type)
    modelEntry.insert(0, curPart.model)
    priceEntry.insert(0, curPart.price)

yes_no = IntVar()
addItem = Checkbutton(m, text="Add as new part", variable = yes_no)

#Commands for buttons responsible for either updating or adding new items
def DataUpdate():
    if yes_no.get() == 0 :
        dataIndex = Listbox.curselection()[0]
        existingParts[dataIndex].type = typeEntry.get()
        existingParts[dataIndex].model = modelEntry.get()
        existingParts[dataIndex].price = priceEntry.get()
        a.Assembler(existingParts)
        namesofParts()
    elif yes_no.get() == 1:
        newPart = Part(typeEntry.get(), modelEntry.get(), priceEntry.get())
        existingParts.append(newPart)
        a.Assembler(existingParts)
        namesofParts()

#Method for exporting
def CreateCheque():
    a.Export(existingParts[Listbox.curselection()[0]])

showButton = Button(m, text = "Show", command=DataExtraction)
updateButton = Button(m, text="Update", command=DataUpdate)
exportButton = Button(m,text="Export", command=CreateCheque)


#Gridding
Label1.grid(row=0, column=0)
Listbox.grid(row = 1, column = 0, ipadx = 30)

typeLabel.grid(row=2, column=0)
typeEntry.grid(row=3, column=0, ipadx=50)

modelLabel.grid(row=4, column=0)
modelEntry.grid(row=5, column=0, ipadx=50)

priceLabel.grid(row=6, column=0)
priceEntry.grid(row=7, column=0, ipadx=50)

addItem.grid(row=8, column=0)

showButton.grid(row=9, column=0, ipadx=20)
updateButton.grid(row=10, column=0, ipadx=15)
exportButton.grid(row=11, column=0, ipadx=17)


m.mainloop()