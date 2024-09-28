from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
words = {}
data_dict = {}
try:
    data = pandas.read_csv("Words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("french_words.csv")
    data_dict = orginal_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


#-------------------------------DATA HANDLING-------------------------#


def display_french_data():
    global words, flip_timer
    window.after_cancel(flip_timer)
    words = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=words["French"], fill="black")
    canvas.itemconfig(canvas_image, image=image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global words
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=words["English"], fill='white')
    canvas.itemconfig(canvas_image, image=back_image)


def is_know():
    global words
    data_dict.remove(words)
    display_french_data()
    df = pandas.DataFrame(data_dict)
    df.to_csv("Words_to_learn.csv", index=False)


#---------------------------------UI-------------------------------#


window = Tk()
window.title("Flash Card App")
# window.minsize(width=800, height=526)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 40, "bold"))
#  =canvas.title(text="French", anchor="center")
# french_label.grid(column=0, row=0)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=display_french_data)
wrong_button.grid(column=1, row=1)

display_french_data()
window.mainloop()
