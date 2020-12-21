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

#import feedback
#fb = feedback.Feedback("Kate`s testing", 3)
#fb.sort_by_name()
#fb.sort_by_mark()
#fb.statistic_by_mark(14)
#fb.filter_by_mark(10, "less")
