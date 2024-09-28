from tkinter import *

window = Tk()
window.minsize(150 , 150)
window.title("Mile to Km Converter")
window.config(padx = 50 , pady = 50)

def button_clicked():
    miles = float(input.get())
    kilometers = miles* 1.689
    lable3.config(text=kilometers)


input = Entry(width=7)
input.grid(column = 1 , row = 0)


lable1 = Label(text = "Miles")
lable1.grid(column = 2,row = 0)

lable2 = Label(text = "is equal to")
lable2.grid(column = 0,row = 1)

lable3 = Label(text = "0")
lable3.grid(column = 1,row = 1)

lable4 = Label(text = "Km")
lable4.grid(column = 2,row = 1)

button = Button(text = "Calculate",command = button_clicked)
button.grid(column = 1,row = 2)





window.mainloop()