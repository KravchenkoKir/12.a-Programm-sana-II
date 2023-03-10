from tkinter import *
from tkinter import messagebox

#klase, kurā tiek saglabātā informācija par produktu
class Dala:
    def __init__(self, tips, modelis, cena):
        self.tips = tips
        self.modelis = modelis
        self.cena = cena

#Klase, kura lasa un maina informāciju tekstā failā.
class FileHandler():
    def __init__(self):
        self.Dalas = []

    #Metode lai progrāma lasa informāciju un izveido daļas no katram trijam daļam
    def Dekonstruktors(self):
        dokuments = open("./art_store/Noliktāva.txt","r")
        #making list for data
        eksistejosasDalas = []
        #reading the file with the data, returning it as a list of lines
        uzrakstitaisTeksts = dokuments.readlines() 
        # Splitting the list into parts consisting 3 pieces each
        for y in range(0, len(uzrakstitaisTeksts)-1,3):  
            list_tips = uzrakstitaisTeksts[y].strip()
            list_modelis = uzrakstitaisTeksts[y+1].strip()
            list_cena = float(uzrakstitaisTeksts[y+2].strip())
            #adding the piece of the read data into the list made for it
            eksistejosasDalas.append(Dala(list_tips, list_modelis, list_cena))
        dokuments.close()
        return eksistejosasDalas


    #method for writing a piece of data    
    def Assembler(self, eksistejosasDalas):
        file1 = open("./art_store/Noliktāva.txt","w")
        b = ""
        for x in eksistejosasDalas:
            # b = b + "string" is the same thing as b += "string" (b + the next thing after it)
            b += x.tips + "\n" + x.modelis + "\n" + str(x.cena) + "\n"
        file1.write(b)
    
    #method for exporting data into an outside file
    def Export(self, eksistejosasDala):
        ceks = open("./art_store/Čeks.txt", "w")
        text = "- ArtStore - \n Informācija: " + eksistejosasDala.tips + "\n Priekšmets: " + eksistejosasDala.modelis + "\n Cena:" + str(eksistejosasDala.cena) + " EUR"
        ceks.write(text)

fileHandler = FileHandler()

eksistejosasDalas = fileHandler.Dekonstruktors()


m = Tk()
m.title('Art Store Storage')


Label1 = Label(m, text="Choose an object or make a new one to work with.")

itemListbox = Listbox(m)

#method for entering the names of parts into the listbox
def namesofParts():
    itemListbox.delete(0, END)
    for curPart in range(len(eksistejosasDalas)):
        itemListbox.insert (curPart, eksistejosasDalas[curPart].modelis)

namesofParts()

#Error popup if nothing is chosen
def error():
   messagebox.showerror('Python Error', 'Error: Please select an item!')

#creating objects

typeLabel = Label(m, text="Additional Information:", justify=LEFT)
modelLabel = Label(m, text="Item:", justify=LEFT)
priceLabel = Label(m, text="Cena (EUR):", justify=LEFT)

typeEntry = Entry(m)
modelEntry = Entry(m)
priceEntry = Entry(m)

def DataExtraction():
    try:
        dataIndex = itemListbox.curselection()[0]
        curPart = eksistejosasDalas[dataIndex]
        typeEntry.delete(first=0, last=len(typeEntry.get()))
        modelEntry.delete(first=0, last=len(modelEntry.get()))
        priceEntry.delete(first=0, last=len(priceEntry.get()))
        typeEntry.insert(0, curPart.tips)
        modelEntry.insert(0, curPart.modelis)
        priceEntry.insert(0, curPart.cena)
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
            eksistejosasDalas[dataIndex].tips = typeEntry.get()
            eksistejosasDalas[dataIndex].modelis = modelEntry.get()
            eksistejosasDalas[dataIndex].cena = priceEntry.get()
            fileHandler.Assembler(eksistejosasDalas)
            namesofParts()
        except:
            error()
    elif addOrUpdate.get() == 2:
        try:
            newPart = Dala(typeEntry.get(), modelEntry.get(), priceEntry.get())
            eksistejosasDalas.append(newPart)
            fileHandler.Assembler(eksistejosasDalas)
            namesofParts()
        except:
            error()

#Method for exporting
def CreateCheque():
    try:
        fileHandler.Export(eksistejosasDalas[itemListbox.curselection()[0]])
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