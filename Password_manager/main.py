from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# -------------------------------SEARCH PASSWORD--------------------------------- #


def search_password():
    web = website_entry.get()
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="File not found")
    else:
        if web in data:
            new_dict = data[web]
            messagebox.showinfo(title=web, message=f"Email: {new_dict['email']}\n Password: {new_dict['password']}")
        else:
            messagebox.showinfo(title="error", message="No data Found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_generated = "".join(password_list)
    password_entry.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    web = website_entry.get()
    mail = email_entry.get()
    pas = password_entry.get()

    new_data = {web:
                {
                    "email": mail,
                    "password": pas
                }
                }

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Oops", message="please dont leave any entries")
    else:
        # is_ok = messagebox.askokcancel(title=web,message=f"These are details entered:Email: {mail}\nPassword = {pas}")
        # if is_ok:
        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)


website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "888niharikaniha@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)


generate = Button(text="Generate Password", width=15, command=password_generator)
generate.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save_password)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="search", width=15, command=search_password)
search.grid(column=2, row=1)

window.mainloop()
