
from argparse import Action
from cgitb import text

from email.mime import image
from ipaddress import collapse_addresses
from operator import iconcat
import tkinter
from turtle import color
ablak = tkinter.Tk()
ablak.geometry("500x500")

def szamol():
    Belefer = 0
    bor = e1.get()
    pi = 3.14
    r = e2.get()
    m = e3.get()
    afroamerikaiferfi = tkinter.PhotoImage("afroamerikaiferfi.png")
    amogus = tkinter.PhotoImage("amogus.png")
    megoldas=float(r)*float(r)*float(pi)*float(m)
    megoldas2 = megoldas/100
    mennyifermegbele = megoldas2-float(bor)
    print(str(megoldas2)+ " liter a kapacitása")
    
    if float(megoldas2) < float(bor):
        print("Nem fér bele")
        Belefer+=1
    else:
        print("Belefér")
        Belefer+=2
    print(mennyifermegbele,"Liter bor fér még bele")
    if Belefer == 1:
        lnem = tkinter.Label(ablak, text="NEM FÉR BELE!",image=amogus)
        lnem.grid(row=1,column=0)
    elif Belefer == 2:
        ligen = tkinter.Label(ablak, text="BELEFÉR!",image=afroamerikaiferfi)
        ligen.grid(row=1,column=0)
        
    
        
        


l1 = tkinter.Label(ablak,
                   text="Bor mennyisége(L)",
                   bg="gold")
l1.grid(row=1,column=0)

l2 = tkinter.Label(ablak,
                   text="Sugár(cm)",
                   bg="gold")
l2.grid(row=2,column=0)

l3 = tkinter.Label(ablak,
                   text="Magasság(cm)",
                   bg="gold")
l3.grid(row=3,column=0)


e1 = tkinter.Entry(ablak)
e1.grid(row=1,column=1)

e2 = tkinter.Entry(ablak)
e2.grid(row=2,column=1)


e3 = tkinter.Entry(ablak)
e3.grid(row=3,column=1)

gomb = tkinter.Button(ablak,
                   text="Kiszámolás",	
                   activebackground="gold",
                   command=szamol)
gomb.grid(row=4,column=4)


ablak.mainloop()