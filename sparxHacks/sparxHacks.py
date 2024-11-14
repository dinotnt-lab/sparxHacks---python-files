import webbrowser
from PIL import ImageGrab
import os
from tkinter import messagebox
import keyboard
import time
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))
currentPath = os.getcwd()
imageFolderPath = currentPath + "\Images"

def setup():
    try:
        if not os.path.exists(imageFolderPath):
            os.makedirs(imageFolderPath)

        else:
            print("Folder already created at: " + imageFolderPath)

    except Exception as e:
        print(e)
    
    print("currentPath: " + currentPath)
    print("imageFolderPath: " + imageFolderPath)
    
    webbrowser.open_new_tab("https://www.sparxmaths.uk/student/homework")
    webbrowser.open_new_tab("gauthmath.com")
    time.sleep(3)
    keyboard.press_and_release("ctrl+1")

    messagebox.showinfo("Infomation", "This application only works if you have no other internet tabs open (other than sparx) and have not put any additonal files into the Sparx Hacks folder. If gauthmath stops giving answers, press 'home' to watch a short how to video, when the video finishes, please close the tab. Open your first question and press space")

def takeImage():
    image = ImageGrab.grab()
    image.save("screenshot.png")
    imagePath = os.path.join(imageFolderPath, 'screenshot.png')
    shutil.move("screenshot.png", imagePath)
    print(imagePath)
    
    return imagePath

def copyImage():
    try:
        os.startfile(imageFolderPath)
    except Exception as e:
        print(f"Error opening folder: {e}")
    time.sleep(1) 
    keyboard.press("right")
    time.sleep(0.2)
    keyboard.press("ctrl+c")
    time.sleep(0.1)
    keyboard.press_and_release("ctrl+w")

def gauth():
    copyImage()
    time.sleep(1)
    gauthReset()

def gauthReset():
    keyboard.press_and_release("ctrl+2")
    time.sleep(0.2)
    keyboard.press_and_release("ctrl+w")
    time.sleep(0.5)
    webbrowser.open("gauthmath.com")
    time.sleep(2)
    keyboard.press_and_release("ctrl+v")
    
def on_home_press(event):
    webbrowser.open_new_tab("https://youtu.be/k8kM9Aq0yE4")

setup()
while True:
    keyboard.on_press_key("home", on_home_press)
    
    keyboard.wait('space')

    imageDir = takeImage()

    gauth()