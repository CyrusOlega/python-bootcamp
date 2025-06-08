import tkinter

root = tkinter.Tk()

label = tkinter.Label(root, text="Enter password:")
label.pack()

entry = tkinter.Entry(root, show="*")
entry.pack()

display_result = tkinter.StringVar(root, value="Enter your password and press Submit.")
result_label = tkinter.Label(root, textvariable=display_result)
result_label.pack()

def verify(event=None):
    if entry.get() == "password":
        display_result.set("Password correct! Access granted.")
    else:
        display_result.set("Incorrect password. Try again.")

button = tkinter.Button(root, text="Submit", command=verify)
button.pack()
root.mainloop()