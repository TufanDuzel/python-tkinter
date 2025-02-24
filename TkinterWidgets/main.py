from tkinter import *

# Window
window = Tk()
window.title("Tkinter Screen")
window.minsize(width= 600, height= 600)
window.config(padx= 25, pady= 25) # Moves away from the edges.

def scale_selected(value):
    print(value)

# Scale
scale = Scale(from_= 0, to= 50, command= scale_selected)
scale.pack()

def spinbox_selected():
    print(spinbox.get())

# Spinbox
spinbox = Spinbox(from_= 0, to= 50, command= spinbox_selected)
spinbox.pack()

def checkbutton_selected():
    print(check_state.get())

# Check Button
check_state = IntVar() # If it's clicked, it returns 1, otherwise 0.
check_button = Checkbutton(text = "Check", variable= check_state, command= checkbutton_selected)
check_button.pack()

def radio_selected():
    print(radio_checked_state.get())

# Radio Button
radio_checked_state = IntVar()
radio_button_1 = Radiobutton(text= "Option 1", value= 10, variable= radio_checked_state, command= radio_selected)
radio_button_2 = Radiobutton(text= "Option 2", value= 20, variable= radio_checked_state, command= radio_selected)
radio_button_1.pack()
radio_button_2.pack()

# Listbox
listbox = Listbox()
my_list = ["Tufan", "Ross", "Jay", "Manny"]

for i in range(len(my_list)):
    listbox.insert(i, my_list[i])

listbox.pack()

window.mainloop()