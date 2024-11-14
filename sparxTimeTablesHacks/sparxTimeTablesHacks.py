import pytesseract
from PIL import ImageGrab
import keyboard
import os
import re
import time
import winsound
from tkinter import messagebox

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

os.chdir(os.path.dirname(os.path.abspath(__file__)))
currentPath = os.getcwd()

fails = 0
prevQuestion = []

def TakeImage():
    image = ImageGrab.grab(bbox=(570, 170, 950, 300))
    image.save("image.png")
    image.close()
    imagePath = currentPath + r"\image.png"
    return imagePath

def getAnswer(path):
    global fails, prevQuestion
    string = pytesseract.image_to_string(path, config="--oem 3 --psm 11")
    print(string)
    try:
        numbers = re.findall(r'\d+', string)
        first_num = int(numbers[0])
        second_num = int(numbers[1])

        if ("?x" in string) or ("? x" in string):
            answer = int(second_num / first_num)
        elif "x" in string:
            answer = int(first_num * second_num)
        elif "+" in string:
            answer = int(first_num / second_num)

        question = [first_num, second_num]
        print(str(question) + "->" + str(answer))
        if question == prevQuestion:
            UserHelp()
            return
        prevQuestion = [first_num, second_num]

        fails = 0
        return answer
    except Exception as e:
        print(e)
        fails = fails + 1
        return None

def typeAnswer(answer):
    answer_str = str(answer)
    print(answer_str)

    for digit in answer_str:
        keyboard.press(digit)
        print("typing: " + digit)
        time.sleep(0.1)

    keyboard.press_and_release("enter")

def UserHelp():
    winsound.PlaySound('erro.wav', winsound.SND_ASYNC)
    messagebox.showerror("Error", "There has been a recurring error with this screen. Please complete it and get to a new question then press 'home' to continue.")
    keyboard.wait("home")
    print("ok")

def Run():
    global fails
    while allow:
        time.sleep(2)
        print("go")

        if fails > 3:
            UserHelp()
            fails = 0
        else:
            imagePath = TakeImage()

            answer = getAnswer(path=imagePath)
            print(str(answer))

            typeAnswer(answer)
            print("done")

messagebox.showinfo("Info", "This program has only been tested on sticker collector, on a specific monitor size and is not the best so it may require user intervention to proceed. It cannot detect the difference between a question screen or an incorrect screen so its possible it can mess stuff up. I recommend NOT using the numpad (if you have one) because 7 restarts the code.")

keyboard.wait("home")

allow = True
Run()