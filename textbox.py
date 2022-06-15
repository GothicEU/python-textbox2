from tkinter import *

root = Tk()
root.geometry("600x230")
root.title("Display tutorial")

def Take_input():
    INPUT = InputBox.get("1.0", "end-1c")
    print(INPUT)
    if not INPUT or len(INPUT) > 20:
        OutputLabel.pack()
    else:
        OutputLabel.destroy()
        InputBox.destroy()
        Display.destroy()
        textVar.set("Hello " + INPUT + "!")
        TextLabel.place(relx = 0.5, rely = 0.5, anchor = 'center')

textVar = StringVar()

textVar.set("What is your name?")

OutputLabel = Label(root, text = "Invalid input.\nTry again.", font = "Arial", bd = 15)

InputBox = Text(root, height = 3, width = 25, bg = "white")

Display = Button(root, height = 2, width = 20, text ="Confirm", command = lambda:Take_input())

TextLabel = Label(textvariable = textVar, font = ("Arial", 30), bd = 15)

TextLabel.pack()
InputBox.pack()
Display.pack()

mainloop()
