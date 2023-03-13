#tkinter ir GUI bibliotēka, un messagebox tieks izmantots kļudām
from tkinter import *
from tkinter import messagebox

#klase, kurā tiek saglabātā informācija par produktu
class Produkts:
    def __init__(self, informacija, prieksmets, cena):
        self.informacija = informacija
        self.prieksmets = prieksmets
        self.cena = cena

#Klase, kura lasa un maina informāciju tekstā failā.
class FailaMaina():
    def __init__(self):
        self.Produkts = []

    #Metode lai progrāma lasa informāciju un izveido daļas no katram trijam daļam
    def dekonstruktors(self):
        dokuments = open("./makslas_veikals/Noliktāva.txt","r")
        #Izveidoja listu visam daļam
        eksistejusiProdukti = []
        #Tekstu lasīšana un to reģistrēšana kā 3 dažādas linijas
        uzrakstitaisTeksts = dokuments.readlines() 
        #Cikls, kurš dalā informaciju uz dažadiem elementiem
        for pozicija in range(0, len(uzrakstitaisTeksts)-1,3):  
            list_informacija = uzrakstitaisTeksts[pozicija].strip()
            list_prieksmets = uzrakstitaisTeksts[pozicija+1].strip()
            list_cena = float(uzrakstitaisTeksts[pozicija+2].strip())
            #Pēc informācijas lasīšanai, pievieno to listā
            eksistejusiProdukti.append(Produkts(list_informacija, list_prieksmets, list_cena))
        dokuments.close()
        return eksistejusiProdukti


    #Metode, kura ieraksta jaunus datus tekstu failā    
    def konstruktors(self, eksistejusiProdukti):
        faila = open("./makslas_veikals/Noliktāva.txt","w")
        jaunaInformacija = ""
        for jaunsProdukts in eksistejusiProdukti:
            jaunaInformacija += jaunsProdukts.informacija + "\n" + jaunsProdukts.prieksmets + "\n" + str(jaunsProdukts.cena) + "\n"
        faila.write(jaunaInformacija)
    
    #Metode, kura ieraksta informāciju arejā tekstā failā
    def eksportesana(self, eksistejusaisProdukts):
        ceks = open("./makslas_veikals/Čeks.txt", "w")
        teksts = (
        "- Makslas Veikals - \n Informacija: " + eksistejusaisProdukts.informacija 
        + "\n Prieksmets: " + eksistejusaisProdukts.prieksmets 
        + "\n Cena:" + str(eksistejusaisProdukts.cena) + " EUR"
        )
        ceks.write(teksts)

failaMaina = FailaMaina()

eksistejusiProdukti = failaMaina.dekonstruktors()

#GUI Logu veidošana
m = Tk()
m.title('Mākslas Veikala Noliktāva')

#Instrukcija lietotājiem
izvelesanaTeksts = Label(m, text="Izvēleties objektu vai izveidojiet jaunu, ar kuru ir jāstrādā.")

#Lauks, kurā būs redzāma visa informācija par visiem produktiem
produktuOpcijas = Listbox(m)

#Metode, kura ievāda informāciju no faila laukā
def produktuVardi():
    produktuOpcijas.delete(0, END)
    for izveletsProdukts in range(len(eksistejusiProdukti)):
        produktuOpcijas.insert (izveletsProdukts, eksistejusiProdukti[izveletsProdukts].prieksmets)

produktuVardi()

#Kļudas logs jā objekts nav izvelēts
def kluda():
   messagebox.showerror('Python Error', 'Error: Lūdzu, izvēleties objektu!')

#Lauki, kur būs noradīta informācija par produktiem 
#un kur lietotājs var izmainīt vai nokopēt informāciju.
informacijaIeraksts = Entry(m)
prieksmetaIeraksts = Entry(m)
cenaIeraksts = Entry(m)

#Vārdi laukiem
informacijaTeksts = Label(m, text="Informācija:", justify=LEFT)
prieksmetsTeksts = Label(m, text="Priekšmēts:", justify=LEFT)
cenaTeksts = Label(m, text="Cena (EUR):", justify=LEFT)

#Metode, kura parāda informāciju Ierakstu laukos
def datuLasisana():
    try:
        datuIndekss = produktuOpcijas.curselection()[0]
        izveletsProdukts = eksistejusiProdukti[datuIndekss]
        informacijaIeraksts.delete(first=0, last=len(informacijaIeraksts.get()))
        prieksmetaIeraksts.delete(first=0, last=len(prieksmetaIeraksts.get()))
        cenaIeraksts.delete(first=0, last=len(cenaIeraksts.get()))
        informacijaIeraksts.insert(0, izveletsProdukts.informacija)
        prieksmetaIeraksts.insert(0, izveletsProdukts.prieksmets)
        cenaIeraksts.insert(0, izveletsProdukts.cena)
    except:
        kluda()

#Pogas, ar kuriem lietotājs var izvelēties starp informacijas pievienošanu vai maiņu
pievienotVaiMainit = IntVar()
pievienotVaiMainit.set(1)

pievienotProduktu = Radiobutton(m, text="Pievienot Jaunu Produktu", variable = pievienotVaiMainit, value=2)
mainitProduktu = Radiobutton(m, text="Mainīt Izvelētu Produktu", variable= pievienotVaiMainit, value=1)

#Instrukcija lietotājiem
pievienosanaInstrukcija = Label(m, text="Lai izveidot jaunu objektu, izmanto 'Pievienot Jaunu Produktu' opciju.",justify=LEFT)
mainuInstrukcija = Label(m,text="Lai mainīt informaciju izvelētā objektā, izmanto 'Mainīt Izvelētu Produktu' opciju.", justify=LEFT)

#Metode, kura dara citus funkcijus, skatot uz izvelētu opciju
def datuMaina():
    if pievienotVaiMainit.get() == 1 :
        try:
            datuIndekss = produktuOpcijas.curselection()[0]
            eksistejusiProdukti[datuIndekss].informacija = informacijaIeraksts.get()
            eksistejusiProdukti[datuIndekss].prieksmets = prieksmetaIeraksts.get()
            eksistejusiProdukti[datuIndekss].cena = cenaIeraksts.get()
            failaMaina.konstruktors(eksistejusiProdukti)
            produktuVardi()
        except:
            kluda()
    elif pievienotVaiMainit.get() == 2:
        try:
            newPart = Produkts(informacijaIeraksts.get(), prieksmetaIeraksts.get(), cenaIeraksts.get())
            eksistejusiProdukti.append(newPart)
            failaMaina.konstruktors(eksistejusiProdukti)
            produktuVardi()
        except:
            kluda()

#Metode eksportesanai
def izveidoCeku():
    try:
        failaMaina.eksportesana(eksistejusiProdukti[produktuOpcijas.curselection()[0]])
    except:
        kluda()

#Pogas funkcijam
paraditPoga = Button(m, text = "Paradīt", command=datuLasisana)
mainitPoga = Button(m, text="Mainīt", command=datuMaina)
eksportetPoga = Button(m,text="Eksportēt", command=izveidoCeku)


#Visu GUI elementus uzvilkšana programmā (Gridding)
izvelesanaTeksts.grid(row=0, column=1)
produktuOpcijas.grid(row = 1, column = 1, ipadx = 90)

informacijaTeksts.grid(row=2, column=1)
informacijaIeraksts.grid(row=3, column=1, ipadx=90)

prieksmetsTeksts.grid(row=4, column=1)
prieksmetaIeraksts.grid(row=5, column=1, ipadx=90)

cenaTeksts.grid(row=6, column=1)
cenaIeraksts.grid(row=7, column=1, ipadx=90)

pievienosanaInstrukcija.grid(row=8, column=1)
mainuInstrukcija.grid(row=9, column=1)

pievienotProduktu.grid(row=10, column=1, ipady=5)
mainitProduktu.grid(row=11, column=1, ipady=5)

paraditPoga.grid(row=12, column=0, ipadx=50, ipady= 5)
mainitPoga.grid(row=12, column=1, ipadx=50, ipady=5)
eksportetPoga.grid(row=12, column=2, ipadx=50, ipady=5)


m.mainloop()