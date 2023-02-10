from Part import *

#making a class for a File Handler
class FileHandler():
    def __init__(self):
        self.Parts = []

    #method for reading the data
    def Disassembler(self):
        file1 = open("PC parts2.txt","r")
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
        file1 = open("PC parts2.txt","w")
        b = ""
        for x in existingParts:
            # b = b + "string" is the same thing as b += "string" (b + the next thing after it)
            b += x.type + "\n" + x.model + "\n" + str(x.price) + "\n"
        file1.write(b)
    
    #method for exporting data into an outside file
    def Export(self, existingPart):
        cheque = open("Cheque.txt", "w")
        text = "- PC Part - \n Type: " + existingPart.type + "\n Model: " + existingPart.model + "\n Price:" + str(existingPart.price)
        cheque.write(text)