import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import webbrowser

try:
    file = open("data.txt", mode="r")
    file.close()
except FileNotFoundError:
    print("The file wasnt there, creating...")
    file = open("data.txt", mode="a+")
    messagebox.showinfo("Info", "Please select where the rest of the files are saved, this will most likly be a folder in your downloads labeled sparxHacks")
    fileLocation = filedialog.askdirectory()
    sparxHacks = fileLocation + "/sparxHacks/sparxHacks.exe"
    timesTablesHacks = fileLocation + "/sparxTimeTablesHacks/sparxTimeTablesHacks.exe"
    file.write(sparxHacks + "\n")
    file.write(timesTablesHacks + "\n")
    file.close()

with open("data.txt", "r") as file:
    data = file.readlines()

data = [line.strip() for line in data]

def sparxHacks():
    print("sparxHacks")
    os.startfile(data[0])
    m.quit()

def sparxTimesTablesHacks():
    print("sparxTimesTablesHacks")
    os.startfile(data[1])
    m.quit()

def github():
    webbrowser.open(r"https://github.com/dinotnt-lab")

m = tk.Tk()
m.title("Sparx Hacks Menu")
m.geometry("400x200")
m.resizable(False, False)

button1 = tk.Button(m, text='Sparx Hacks', command=sparxHacks)
button1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

button2 = tk.Button(m, text='Sparx Times Tables Hacks', command=sparxTimesTablesHacks)
button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

button3 = tk.Button(m, text='Quit', command=m.quit)
button3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

label = tk.Label(m, text="Made by dinotnt_", fg="blue", cursor="hand2")
label.place(x=300, y=175)
label.bind("<Button-1>", lambda e: github())

m.mainloop()