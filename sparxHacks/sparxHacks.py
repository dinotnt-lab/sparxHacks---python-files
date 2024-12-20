from webbrowser import open_new_tab
from PIL import ImageGrab
from os import chdir, path, makedirs, startfile
from tkinter import messagebox
import tkinter as tk
from keyboard import wait, press_and_release, write
from time import sleep
from shutil import move
from pyautogui import position, click
from re import match
from clipboard import paste
import chatgpt
import questionRecognition

currentPath = path.dirname(path.abspath(__file__))
chdir(currentPath)
print(currentPath)
imageFolderPath = currentPath + "\Images"
dataPath = currentPath + "\data.txt"

x_lock = 0
y_lock = 0
x_cookie = 0
y_cookie = 0
x_cookieURL = 0
y_cookieURL = 0
x_done = 0
y_done = 0
x_answer = 0
y_answer = 0

def show_message(title, text):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    messagebox.showinfo(title, text)
    root.destroy()

def setup():
    try:
        if not path.exists(imageFolderPath):
            makedirs(imageFolderPath)

        else:
            print("Folder already created at: " + imageFolderPath)

        if not path.exists(dataPath):
            with open(dataPath, "a") as datafile:
                open_new_tab("www.google.com")

                show_message("Setup", "Put your mouse over the lock in the top left and press enter")
                wait('enter')
                print("enter")
                pos = position()
                datafile.write(str(pos) + "\n")
                sleep(1)

                show_message("Setup", "Now click it and put your mouse over 'cookies' and press enter")
                wait('enter')
                print("enter")
                pos = position()
                datafile.write(str(pos) + "\n")
                sleep(1)

                show_message("Setup", "Now click it twice and put your mouse over first link under 'allow' and press enter")
                wait('enter')
                print("enter")
                pos = position()
                datafile.write(str(pos) + "\n")
                sleep(1)

                show_message("Setup", "Now put your mouse over 'done' and press enter")
                wait('enter')
                print("enter")
                pos = position()
                datafile.write(str(pos) + "\n")
                sleep(1)

                press_and_release("ctrl+w")
                open_new_tab("www.sparxmaths.uk/student/homework")

                show_message("Setup", "Now put your mouse over 'answer' and press enter")
                wait('enter')
                print("enter")
                pos = position()
                datafile.write(str(pos) + "\n")
                sleep(1)

                press_and_release("ctrl+w")
        else:
            print("Data File already created")

    except Exception as e:
        print(e)

    print("currentPath: " + currentPath)
    print("imageFolderPath: " + imageFolderPath)

    get_coords()
    
    open_new_tab("https://www.sparxmaths.uk/student/homework")
    open_new_tab("www.gauthmath.com")
    sleep(3)
    press_and_release("ctrl+1")

    messagebox.showinfo("Infomation", "This application only works if you have no other internet tabs open (other than sparx and gauth) and have not put any additonal files into the Sparx Hacks folder. Open your first question and press space")

def take_image():
    image = ImageGrab.grab()
    image.save("screenshot.png")
    imagePath = path.join(imageFolderPath, 'screenshot.png')
    move("screenshot.png", imagePath)
    print(imagePath)
    
    return imagePath

def copy_image():
    try:
        startfile(imageFolderPath)
    except Exception as e:
        print(f"Error opening folder: {e}")
    sleep(1) 
    press_and_release("right")
    sleep(0.2)
    press_and_release("ctrl+c")
    sleep(0.1)
    press_and_release("ctrl+w")

def get_coords():
    global x_lock, y_lock, x_cookie, y_cookie, x_cookieURL, y_cookieURL, x_done, y_done, x_answer, y_answer
    with open(dataPath, "r") as datafile:
        lock = datafile.readline()
        match_result = match(r"Point\(x=(\d+), y=(\d+)\)", lock.strip())
        x_lock = int(match_result.group(1))
        y_lock = int(match_result.group(2))

        cookie = datafile.readline()
        match_result = match(r"Point\(x=(\d+), y=(\d+)\)", cookie.strip())
        x_cookie = int(match_result.group(1))
        y_cookie = int(match_result.group(2))

        cookieURL = datafile.readline()
        match_result = match(r"Point\(x=(\d+), y=(\d+)\)", cookieURL.strip())
        x_cookieURL = int(match_result.group(1))
        y_cookieURL = int(match_result.group(2))

        done = datafile.readline()
        match_result = match(r"Point\(x=(\d+), y=(\d+)\)", done.strip())
        x_done = int(match_result.group(1))
        y_done = int(match_result.group(2))

        answer = datafile.readline()
        match_result = match(r"Point\(x=(\d+), y=(\d+)\)", answer.strip())
        x_answer = int(match_result.group(1))
        y_answer = int(match_result.group(2))

def clear_cookies():
    click(x_lock, y_lock)
    sleep(1)
    click(x_cookie, y_cookie)
    sleep(0.2)
    click(x_cookie, y_cookie)
    sleep(0.2)
    click(x_cookieURL, y_cookieURL)
    sleep(0.2)
    for i in range(10):
        press_and_release("delete")
        sleep(0.1)
    click(x_done, y_done)

    press_and_release("f5")

def gauth_run():
    sleep(0.3)
    press_and_release("ctrl+2")
    sleep(0.3)
    press_and_release("ctrl+w")
    sleep(0.5)
    open_new_tab("gauthmath.com")
    sleep(3)
    clear_cookies()
    sleep(3)
    press_and_release("ctrl+v")
    sleep(1)
    messagebox.showinfo("Copy", "Please press copy then space")
    wait('space')
    return paste()

def open_sparx_answers():
    sleep(0.3)
    press_and_release("ctrl+1")
    sleep(0.3)
    click(x_answer, y_answer)

def execute_answer(answer, answertype):
    if "both" in answertype:
        show_message("Both", f"Please select {answer}, submit and press space")
    elif "2 type" in answertype:
        show_message("2 Type", f"Please select {answer}, submit and press space")
    elif "type" in answertype:
        write(''.join(filter(str.isdigit, answer)))
        press_and_release("enter")
    elif "multiple select" in answertype:
        show_message("Multiple Select", f"Please select {answer}, submit and press space")
    elif "select from box" in answertype:
        show_message("Select in Box", f"Please select {answer}, submit and press space")
    elif "select" in answertype:
        show_message("Select", f"Please select {answer}, submit and press space")

setup()

while True:
    wait('space')

    image_dir = take_image()

    copy_image()

    answerstr = gauth_run()
    answer = chatgpt.getAnswer(answerstr)

    open_sparx_answers()

    sleep(2)
    
    take_image()

    answertype, confidence = questionRecognition.imagetypecheck(imageFolderPath + "\screenshot.png")

    answer = answer.replace("$", "")
    print("Answer type: " + answertype)
    print("Confidence: " + str(round(confidence, 2)*100) + "%")
    print("Answer: " + answer)

    execute_answer(answer, answertype)