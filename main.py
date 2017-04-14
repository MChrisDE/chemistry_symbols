from letthefunbegin import letthefunbegin
from getallsymbole import get_all
from tkinter import *

allel = get_all()
print(allel)

master = Tk()
master.wm_title("CHEMIE IST COOL")
p
titel = Label(master, text="CHEMIE IST COOL", font=("Century Gothic", 11))
titel.grid(row=0, column=0, padx=40, pady=5)

inpud = StringVar()
entry = Entry(master, textvariable=inpud, width=50)
entry.grid(row=1, column=0, padx=40, pady=5)
entry.bind("<Return>", lambda event: letthefunbegin(allel, inpud))

submit = Button(master, text="Eingabe", font=("Century Gothic", 11), command=lambda: letthefunbegin(allel, inpud))
submit.grid(row=3, column=1, padx=10, pady=5)

master.mainloop()
