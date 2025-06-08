import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

def mark_input(event):
    label = tkinter.Label(root, text=entry.get())
    label.pack()

root.bind("<Return>", mark_input)
root.mainloop()