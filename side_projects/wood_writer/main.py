import csv
import os.path
from datetime import *

# Класс, в котором хранится информация о клиенте и функции
class Info:
    # программа запрашивает информацию
    def __init__(self):
        self.client = input("Please enter a client's name: ")
        self.text = input("Please enter the required text: ")
        self.height = int(input("Please enter the height of wood: "))
        self.width = int(input("PLease enter the width of the wood: "))
        self.length = int(input("Please enter the length of the wood: "))
        self.woodPrice = float(input("Please enter the price for the material: "))

    # программа высчитывает цену, учитывая ПВН и платеж работникам
    def priceCalculator(self):
        # формула, взятая из ПДФ файла с заданием
        workerSalary = 15
        Tax = 21
        productPrice = (len(self.text))*1.2 + (self.width/100 * self.length/100 * self.height/100) * 3 * self.woodPrice
        taxSum = (productPrice + workerSalary)*Tax/100
        finalPrice = (productPrice + workerSalary + taxSum)
        # вывод конечного результата
        return finalPrice
    
    # программа выводит чек в друх разных видах - текстовый файл и CSV 
    def Export(self, price):
        mydate = datetime.now()
        # текстовый файл (программа перепишет файл с каждой новой полученной информацией)
        cheque = open("./wood_writer/Cheque.txt", "w")
        writing = mydate.strftime("Date and Time of printing: %d.%m.%Y %H : %M") + "\n Client name: " + self.client + "\n Ordered text: " + self.text + "\n Price in total: " + str(price) + "EUR"
        cheque.write(writing)
        # CSV файл
        """
        with open('CSVCheque.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Date and Time of printing:", mydate])
            writer.writerow(["Client name:", self.client])
            writer.writerow(["Ordered text:", self.text])
            writer.writerow(["Price in total:", str(price) + " EUR"])
        """
        is_created = os.path.isfile("./wood_writer/CSVCheque.csv")
        with open('./wood_writer/CSVCheque.csv', 'a', newline="") as f:
            writer = csv.writer(f)
            if not is_created:
                writer.writerow(["Date and Time of printing","Client name","Ordered text","Price in total"])
            writer.writerow([mydate, self.client, self.text, str(price)])
        
# задается обьект, с помощью которого работает программа, и затем с этим обьектом она выполняет заданные функции
woodThing = Info()
totalSum = woodThing.priceCalculator()
woodThing.Export(totalSum)