import manager

'''from tkinter import *
import threading
import time

label = None

def window():
    global label

    root = Tk()
    label = Label(root, text = '', fg='black')
    label.pack()
    root.mainloop()

thread = threading.Thread(target = window)
thread.start()
time.sleep(1)

while True:
    mytext = str(time.time())
    label.config(text = mytext)'''  # теоретично можливий вивід в вікні

Manager = manager.Manager()
Manager.ConsoleView()
