import tkinter

root = tkinter.Tk()

count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
    count.set(count.get() + 1)

def decrement():
    count.set(count.get() - 1)

button_increment = tkinter.Button(root, text=" + ", command=increment)
button_increment.pack()

button_decrement = tkinter.Button(root, text=" - ", command=decrement)
button_decrement.pack()

root.mainloop()