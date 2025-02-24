import tkinter

# Window
window = tkinter.Tk()
window.title("Tkinter Screen")
window.minsize(450, 300)

# Label
my_label = tkinter.Label(text= "This is a label.", font= ("Arial", 10, "bold"))
my_label.config(bg= "black", fg= "white") # See the parameters.
my_label.pack() # It provides the label to be centered.

def click_button():
    user_input = my_entry.get()
    print(user_input)

# Entry
my_entry = tkinter.Entry(width= 20)
my_entry.pack()

# Button
my_button = tkinter.Button(text= "This is a button.", command= click_button)
my_button.pack()


window.mainloop()