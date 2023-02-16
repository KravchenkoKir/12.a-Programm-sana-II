from tkinter import *

#class consisting template for art models
class Part:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

#Class that will handle reading the file and extracting the information from it.
class FileHandler():
    def __init__(self):
        self.Parts = []

    #method for reading the data
    def Disassembler(self):
        file1 = open("./store_prototype_txt_ver/Supplies.txt","r")
        #making list for data
        existingParts = []
        #reading the file with the data, returning it as a list of lines
        returnedText = file1.readlines() 
        # Splitting the list into parts consisting 3 pieces each
        for y in range(0, len(returnedText)-1,3):  
            list_type = returnedText[y].strip()
            list_model = returnedText[y+1].strip()
            list_price = float(returnedText[y+2].strip())
            #adding the piece of the read data into the list made for it
            existingParts.append(Part(list_type, list_model, list_price))
        file1.close()
        return existingParts


    #method for writing a piece of data    
    def Assembler(self, existingParts):
        file1 = open("./store_prototype_txt_ver/Supplies.txt","w")
        b = ""
        for x in existingParts:
            # b = b + "string" is the same thing as b += "string" (b + the next thing after it)
            b += x.type + "\n" + x.model + "\n" + str(x.price) + "\n"
        file1.write(b)
    
    #method for exporting data into an outside file
    def Export(self, existingPart):
        cheque = open("./store_prototype_txt_ver/Cheque.txt", "w")
        text = "- ArtStore - \n Information: " + existingPart.type + "\n Item: " + existingPart.model + "\n Price:" + str(existingPart.price) + " EUR"
        cheque.write(text)

fileHandler = FileHandler()

existingParts = fileHandler.Disassembler()


m = Tk()
m.title('Art Store Storage')


Label1 = Label(m, text="Choose an object or make a new one to work with.")

Listbox = Listbox(m)

#method for entering the names of parts into the listbox
def namesofParts():
    Listbox.delete(0, END)
    for curPart in range(len(existingParts)):
        Listbox.insert (curPart, existingParts[curPart].model)

namesofParts()

#creating objects

typeLabel = Label(m, text="Additional Information:", justify=LEFT)
modelLabel = Label(m, text="Item:", justify=LEFT)
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
    fileHandler.Export(existingParts[Listbox.curselection()[0]])

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