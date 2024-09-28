from tkinter import  *

window = Tk()
window.title("the new game")
window.minsize(500,500)

label_win = Label(text ="Hello world" , font = ("Arial",24))
label_win.grid(column = 0,row = 0)

def button_clicked():
    label_win["text"] = input.get()


button = Button(text="click Me",command=button_clicked)
button.grid(column=1 , row=1)

button2 = Button(text = " new button")
button2.grid(column = 2 , row=0)

input = Entry(width=10)
input.grid(column = 3 , row = 2)
window.mainloop()
