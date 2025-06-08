import tkinter

def create_input_label(frame, label_name):
    input_label = tkinter.Frame(frame, borderwidth=5)
    input_label.pack(fill="x")

    label = tkinter.Label(input_label, text=label_name, width=10)
    label.pack(side="left")

    entry = tkinter.Entry(input_label)
    entry.pack()

def create_radio_button(frame):
    radio_var = tkinter.StringVar(value="Light")
    radio_light = tkinter.Radiobutton(frame, text="Light", variable=radio_var, value="Light")
    radio_light.pack(anchor="center")

    radio_dark = tkinter.Radiobutton(frame, text="Dark", variable=radio_var, value="Dark")
    radio_dark.pack()

def create_radio_label(frame, label_name):
    radio_label = tkinter.Frame(frame)
    radio_label.pack()

    label = tkinter.Label(radio_label, text=label_name)
    label.pack(side="left")

    create_radio_button(radio_label)

def create_checkbox_label(frame, label_name):
    checkbox_label = tkinter.Frame(frame)
    checkbox_label.pack()

    check_value = tkinter.BooleanVar()
    checkbox = tkinter.Checkbutton(
        checkbox_label,
        text=label_name,
        variable=check_value
    )
    checkbox.pack()

def create_slider(frame, label_name):
    checkbox_label = tkinter.Frame(frame)
    checkbox_label.pack()

    label = tkinter.Label(checkbox_label, text=label_name)
    label.pack(side="left")

    slider_value = tkinter.IntVar(value=0)
    slider = tkinter.Scale(checkbox_label,from_=0,to=5,orient="horizontal",variable=slider_value)
    slider.pack()

root = tkinter.Tk()

input_label_frame = tkinter.Frame(root, width=200)
input_label_frame.pack()

create_input_label(input_label_frame, "Name")
create_input_label(input_label_frame, "Age")

create_radio_label(root, "Preferred Theme")

create_checkbox_label(root,"Subscribe to Newsletter")

create_slider(root, "Rate Us")

button_frame = tkinter.Frame(root, padx=10, pady=10)
button_frame.pack()

button = tkinter.Button(button_frame, text="Submit")
button.pack()

root.mainloop()
