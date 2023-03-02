from tkinter import *
from tkinter import messagebox

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
        file1 = open("./art_store/Supplies.txt","r")
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
        file1 = open("./art_store/Supplies.txt","w")
        b = ""
        for x in existingParts:
            # b = b + "string" is the same thing as b += "string" (b + the next thing after it)
            b += x.type + "\n" + x.model + "\n" + str(x.price) + "\n"
        file1.write(b)
    
    #method for exporting data into an outside file
    def Export(self, existingPart):
        cheque = open("./art_store/Cheque.txt", "w")
        text = "- ArtStore - \n Information: " + existingPart.type + "\n Item: " + existingPart.model + "\n Price:" + str(existingPart.price) + " EUR"
        cheque.write(text)

fileHandler = FileHandler()

existingParts = fileHandler.Disassembler()


m = Tk()
m.title('Art Store Storage')


Label1 = Label(m, text="Choose an object or make a new one to work with.")

itemListbox = Listbox(m)

#method for entering the names of parts into the listbox
def namesofParts():
    itemListbox.delete(0, END)
    for curPart in range(len(existingParts)):
        itemListbox.insert (curPart, existingParts[curPart].model)

namesofParts()

#Error popup if nothing is chosen
def error():
   messagebox.showerror('Python Error', 'Error: Please select an item!')

#creating objects

typeLabel = Label(m, text="Additional Information:", justify=LEFT)
modelLabel = Label(m, text="Item:", justify=LEFT)
priceLabel = Label(m, text="Price (EUR):", justify=LEFT)

typeEntry = Entry(m)
modelEntry = Entry(m)
priceEntry = Entry(m)

def DataExtraction():
    try:
        dataIndex = itemListbox.curselection()[0]
        curPart = existingParts[dataIndex]
        typeEntry.delete(first=0, last=len(typeEntry.get()))
        modelEntry.delete(first=0, last=len(modelEntry.get()))
        priceEntry.delete(first=0, last=len(priceEntry.get()))
        typeEntry.insert(0, curPart.type)
        modelEntry.insert(0, curPart.model)
        priceEntry.insert(0, curPart.price)
    except:
        error()

addOrUpdate = IntVar()
addOrUpdate.set(1)
addItem = Radiobutton(m, text="Add New Item", variable = addOrUpdate, value=2)
updateItem = Radiobutton(m, text="Update Current Item", variable= addOrUpdate, value=1)
addInstruction = Label(m, text="To make a new item, use 'Add New Item' option.",justify=LEFT)
updateInstruction = Label(m,text="To edit information, use 'Update Current Item' option.", justify=LEFT)

#Commands for buttons responsible for either updating or adding new items
def DataUpdate():
    if addOrUpdate.get() == 1 :
        try:
            dataIndex = itemListbox.curselection()[0]
            existingParts[dataIndex].type = typeEntry.get()
            existingParts[dataIndex].model = modelEntry.get()
            existingParts[dataIndex].price = priceEntry.get()
            fileHandler.Assembler(existingParts)
            namesofParts()
        except:
            error()
    elif addOrUpdate.get() == 2:
        try:
            newPart = Part(typeEntry.get(), modelEntry.get(), priceEntry.get())
            existingParts.append(newPart)
            fileHandler.Assembler(existingParts)
            namesofParts()
        except:
            error()

#Method for exporting
def CreateCheque():
    try:
        fileHandler.Export(existingParts[itemListbox.curselection()[0]])
    except:
        error()

#Buttons
showButton = Button(m, text = "Show", command=DataExtraction)
updateButton = Button(m, text="Update", command=DataUpdate)
exportButton = Button(m,text="Export", command=CreateCheque)


#Gridding
Label1.grid(row=0, column=0)
itemListbox.grid(row = 1, column = 0, ipadx = 30)

typeLabel.grid(row=2, column=0)
typeEntry.grid(row=3, column=0, ipadx=50)

modelLabel.grid(row=4, column=0)
modelEntry.grid(row=5, column=0, ipadx=50)

priceLabel.grid(row=6, column=0)
priceEntry.grid(row=7, column=0, ipadx=50)


addInstruction.grid(row=8, column=0)
updateInstruction.grid(row=9, column=0)
addItem.grid(row=10, column=0, ipady=5)
updateItem.grid(row=11, column=0, ipady=5)

showButton.grid(row=12, column=0, ipadx=20, ipady= 5)
updateButton.grid(row=13, column=0, ipadx=15, ipady=5)
exportButton.grid(row=14, column=0, ipadx=17, ipady=5)


m.mainloop()