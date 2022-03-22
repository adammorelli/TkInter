from tkinter import *
import time
ablak1 = Tk()
gyoker = 'C:\\Users\\morelliadamoflavio\\Desktop\\TkInter\\TkInter'
ablak1.geometry('450x450')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica.png')
ablak1.iconphoto(True, icon)
elsokep = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica2.png')

def kiszamit():
    print("Kiszámítás folyamatban...")
    for i in "....":
        print(".\n")
    
        time.sleep(1)
    
        print("..\n")
    
        
        time.sleep(1)
        
        print("...\n")

        time.sleep(1)
        
        print("...\n\n\n\n")

cimke1 = Label(ablak1,
    text='Sugár(cm):'
).grid(row = 0,column = 0)

cimke2 = Label(ablak1,
    text='Magasság(cm):'
).grid(row = 1,column = 0)

mezo1 = Entry(ablak1)
mezo1.grid(row=0,column=1)

mezo2 = Entry(ablak1)
mezo2.grid(row=1,column=1)

gomb=Button(ablak1, text="Kiszámít", command=kiszamit)
gomb.grid(row=1, column=3)























ablak1.mainloop() 

