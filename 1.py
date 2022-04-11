
from tkinter import *
ablak1 = Tk()
gyoker = 'C:\\Users\\morelliadamoflavio\\Desktop\\TkInter\\TkInter'
ablak1.geometry('450x450')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica.png')
ablak1.iconphoto(True, icon)

elsokep = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica2.png')

cimke1 = Label(ablak1,
    text='Első mező:'
).grid(row = 0,column = 0)

cimke2 = Label(ablak1,
    text='Második mező:'
).grid(row = 1,column = 0)

cimke3 = Label(ablak1,
    text='Harmadik mező:'
).grid(row = 2,column = 0)

mezo1 = Entry(ablak1)
mezo1.grid(row=0,column=1)

mezo2 = Entry(ablak1)
mezo2.grid(row=1,column=1)

mezo3 = Entry(ablak1)
mezo3.grid(row=2,column=1)

kep = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica2.png')


# =======
from tkinter import *
ablak1 = Tk()
gyoker = 'C:\\Users\\morelliadamoflavio\\Desktop\\TkInter\\TkInter'
ablak1.geometry('450x450')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica.png')
ablak1.iconphoto(True, icon)

elsokep = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica2.png')

cimke1 = Label(ablak1,
    text='Első mező:'
).grid(row = 0,column = 0)

cimke2 = Label(ablak1,
    text='Második mező:'
).grid(row = 1,column = 0)

cimke3 = Label(ablak1,
    text='Harmadik mező:'
).grid(row = 2,column = 0)

mezo1 = Entry(ablak1)
mezo1.grid(row=0,column=1)

mezo2 = Entry(ablak1)
mezo2.grid(row=1,column=1)

mezo3 = Entry(ablak1)
mezo3.grid(row=2,column=1)

kep = PhotoImage(file='C:\\Users\\morelliadamoflavio\\Desktop\\cica2.png')


# >>>>>>> 92f35d2018ee896c3980993570053f5398770970
ablak1.mainloop()