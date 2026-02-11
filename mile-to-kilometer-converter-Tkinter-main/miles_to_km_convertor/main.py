from tkinter import *

window = Tk()
window.minsize(300, 300)
window.config(padx=50, pady=50)
window.title("Mile to Kilometer Convertor")

label_mile = Label(text="Miles")
label_mile.grid(column=0, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=0)

entry = Entry(width=20)
entry.grid(column=0, row=2)

result = Label(text="0")
result.grid(column=2, row=2)


def action():
    mile = float(entry.get())
    km = mile * 1.609
    result.config(text=f"{km}")
    print(entry.get())


button = Button(text="Calculate", command=action)
button.grid(column=0, row=3)

window.mainloop()
