import sys
from tkinter import *


def select_number(number):
    global num
    num = number
    num = StringVar()
    return num

root = Tk()
frame = Frame(root)
frame.pack()

root.title("Kalkulator v.0.1")


topFrame = Frame(root)
topFrame.pack(side = TOP)

txtDisplay = Entry(frame,bd=20,font=30)
txtDisplay.pack(side = TOP)

button_1 = Button(topFrame,padx=16,pady=16, bd=8, text="1", fg="black",command=lambda: select_number(1))
button_1.pack(side = LEFT)
button_2 = Button(topFrame,padx=16,pady=16, bd=8, text="2", fg="black",command=lambda: select_number(2))
button_2.pack(side = LEFT)
button_3 = Button(topFrame,padx=16,pady=16, bd=8, text="3", fg="black",command=lambda: select_number(3))
button_3.pack(side = LEFT)
button_4 = Button(topFrame,padx=16,pady=16, bd=8, text="4", fg="black",command=lambda: select_number(4))
button_4.pack(side = LEFT)


frame_1 = Frame(root)
frame_1.pack(side = TOP)

button_1A = Button(frame_1,padx=16,pady=16, bd=8, text="5", fg="black")
button_1A.pack(side = LEFT)
button_2A = Button(frame_1,padx=16,pady=16, bd=8, text="6", fg="black")
button_2A.pack(side = LEFT)
button_3A = Button(frame_1,padx=16,pady=16, bd=8, text="7", fg="black")
button_3A.pack(side = LEFT)
button_4A = Button(frame_1,padx=16,pady=16, bd=8, text="8", fg="black")
button_4A.pack(side = LEFT)


frame_2 = Frame(root)
frame_2.pack(side = TOP)

button_1B = Button(frame_2,padx=16,pady=16, bd=8, text="9", fg="black")
button_1B.pack(side = LEFT)
button_2B = Button(frame_2,padx=16,pady=16, bd=8, text="0", fg="black")
button_2B.pack(side = LEFT)
button_3B = Button(frame_2,padx=16,pady=16, bd=8, text="C", fg="black")
button_3B.pack(side = LEFT)
button_4B = Button(frame_2,padx=16,pady=16, bd=8, text="=", fg="black")
button_4B.pack(side = LEFT)


frame_3 = Frame(root)
frame_3.pack(side = TOP)

button_1C = Button(frame_3,padx=16,pady=16, bd=8, text="*", fg="black")
button_1C.pack(side = LEFT)
button_2C = Button(frame_3,padx=16,pady=16, bd=8, text="/", fg="black")
button_2C.pack(side = LEFT)
button_3C = Button(frame_3,padx=16,pady=16, bd=8, text="-", fg="black")
button_3C.pack(side = LEFT)
button_4C = Button(frame_3,padx=16,pady=16, bd=8, text="+", fg="black")
button_4C.pack(side = LEFT)

root.mainloop()