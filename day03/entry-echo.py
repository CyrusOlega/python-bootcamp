import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

def print_input(event):
    user_input = entry.get()
    print(user_input)

root.bind("<Return>", print_input)
root.bind("<space>", print_input)
root.mainloop()