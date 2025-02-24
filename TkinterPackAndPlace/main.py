import tkinter

# Window
window = tkinter.Tk()
window.title("Tkinter Screen")
window.minsize(450, 300)

# Label
my_label = tkinter.Label(text= "This is a label.", font= ("Arial", 10, "bold"))
my_label.config(bg= "black", fg= "white") # See the parameters.
my_label.place(x= 10, y= 10) # To set the position of label.

def click_button():
    user_input = my_entry.get()
    print(user_input)

# Entry
my_entry = tkinter.Entry(width= 20)
my_entry.pack() # To put automatically.

# Button
my_button = tkinter.Button(text= "This is a button.", command= click_button)

my_button.update() # To get height and width infos for the button to center the button.
print(my_button.winfo_height())
print(my_button.winfo_width())

my_button.place(x= 225 - 59, y= 150 - 14) # To center the button.

window.mainloop()