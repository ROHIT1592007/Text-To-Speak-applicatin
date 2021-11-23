import tkinter as tk
import pyttsx3 

engine = pyttsx3.init()

root = tk.Tk()
root.title('Text-To-Speech')
root.configure(background='blue')

label = tk.Label(root,text="Type Something Here:",font="arial 25 bold", bg="blue", fg="red")
label.pack()

textarea = tk.Entry(root, width=30,font="arial 20")
textarea.pack()

def speak(text):
    engine.say(text)
    engine.runAndWait()

button = tk.Button(root,text="SPEAK",font="arial 25 bold", bg="yellow", fg="red", command=lambda:speak(textarea.get()))
button.pack()

root.mainloop()