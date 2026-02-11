from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# --------------------------------------------- PASSWORD GENERATOR ----------------------------------#
def generate_password():
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

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------------------------------- SAVE PASSWORD ---------------------------------------#

def save():
    website = web_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty field", message="Please fill out all parts!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------------------------- FIND PASSWORD ---------------------------------------#
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# -------------------------------------------- UI SETUP ---------------------------------------------#

window = Tk()
window.minsize(300, 300)
window.title("Password Manager")
window.config(padx=50, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(pady=5)
# entries
web_entry = Entry(width=24)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "shahdad@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# buttons
generate_button = Button(text="generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
