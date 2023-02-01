from tkinter.messagebox import showinfo
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
from tkinter import *

padding = 8
mainwindow = tkinter.Tk()
mainwindow.geometry("270x180")
mainwindow['padx'] = padding
mainwindow.wm_resizable(width=True, height=True)
mainwindow.title("Calculator GUI")

label = tkinter.Label(mainwindow, text="CALCULATOR")
label.grid(row=0, column=0, columnspan=3)
canvas = tkinter.Canvas(mainwindow, relief='raised', borderwidth=0, height=1000, width=1000)
canvas.grid(row=2, column=2)
button_list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
# button_dict = {}
# for item, value in enumerate(button_list):
#     button_dict[item] = button_dict.setdefault(item + 1, value)
# print(button_dict)


def add(x, y):
    calculation = x + y
    return calculation


def sub(x, y):
    calculation = x - y
    return calculation


def mul(x, y):
    calculation = x * y
    return calculation


def div(x, y):
    calculation = x / y
    return calculation


# result = tkinter.Entry(mainwindow)
# result.grid(row=1, column=2)
entry = StringVar()
entry.set("")
result = Entry(canvas, textvariable=entry, width=10, )
result.grid(row=0)
#
# def get_entry(text):
#
#     result.delete(0, END)
#     result.insert(0, text)


def ezfunc(value_splitter):
    x = int(value_splitter[0])
    q = int(value_splitter[1])
    yield x
    yield q


def click(event):
    global entry
    text = event.widget.cget("text")
    if text == "CE":
        entry.set("")
        result.update()
    elif text == "+":
        entry.set(entry.get() + "+")
        result.update()
    elif text == "-":
        entry.set(entry.get() + "-")
        result.update()
    elif text == "*":
        entry.set(entry.get() + "*")
        result.update()
    elif text == "/":
        entry.set(entry.get() + "/")
        result.update()

    elif text == "=":
        if '+' in entry.get():
            content = entry.get().split('+')
            l = ezfunc(content)
            r = add(l.__next__(), l.__next__())
            entry.set(r)
        elif '-' in entry.get():
            content = entry.get().split('-')
            l = ezfunc(content)
            r = sub(l.__next__(), l.__next__())
            entry.set(r)
        elif '*' in entry.get():
            content = entry.get().split('*')
            l = ezfunc(content)
            r = mul(l.__next__(), l.__next__())
            entry.set(r)
        elif '/' in entry.get():
            content = entry.get().split('/')
            l = ezfunc(content)
            r = div(l.__next__(), l.__next__())
            entry.set(r)

    for i in listb:
        if text == i:
            entry.set(entry.get() + str(text))
            result.update()

    # print(text)
    # pass


listb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for key in button_list:
    for item in listb:
        button = tkinter.Button(canvas, text=key, width=8)
        button.bind("<Button 1>", click)
        if key < 3:
            button.grid(row=1, column=key)
        elif 2 < key < 6:
            button.grid(row=2, column=key - 3)
        elif 5 < key < 9:
            button.grid(row=3, column=key - 6)
        else:
            button.grid(row=4, column=key - 9)
# Clear Buttons
clear = tkinter.Button(canvas, text="C", width=8)
clear.grid(row=4, column=1, columnspan=1)
CE = tkinter.Button(canvas, text="CE", width=8)
CE.bind("<Button 1>", click)
CE.grid(row=4, column=2,)
# Arithmetic Buttons
addition = tkinter.Button(canvas, text="+", width=8)
addition.grid(row=1, column=3)
addition.bind("<Button 1>", click)
Subtraction = tkinter.Button(canvas, text="-", width=8)
Subtraction.grid(row=2, column=3)
Subtraction.bind("<Button 1>", click)
Multiply = tkinter.Button(canvas, text="*", width=8)
Multiply.grid(row=3, column=3)
Multiply.bind("<Button 1>", click)
Divide = tkinter.Button(canvas, text="/", width=8)
Divide.grid(row=4, column=3)
Divide.bind("<Button 1>", click)
equal = tkinter.Button(canvas, text="=", width=8)
equal.grid(row=5, column=3)
equal.bind("<Button 1>", click)
mainwindow.mainloop()