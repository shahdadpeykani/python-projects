from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canva.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Kanye says..")
window.config(pady=50, padx=50)

canva = Canvas(width=300, height=414)
background = PhotoImage(file="background.png")
canva.create_image(150, 207, image=background)
quote_text = canva.create_text(150, 207, text="Kanye Quotes Goes Here", width=250, font=("Arel", 20, "bold"),
                               fill="white")
canva.grid(column=0, row=0)

kanye_img = PhotoImage(file="kanye.png")
button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
button.grid(column=1, row=3)
button.grid(column=0, row=1)
window.mainloop()
