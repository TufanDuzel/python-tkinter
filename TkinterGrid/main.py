import tkinter

# Window
window = tkinter.Tk()
window.title("Tkinter Screen")
window.minsize(450, 300)

# Label
my_label = tkinter.Label(text= "This is a label.", font= ("Arial", 10, "bold"))
my_label.config(bg= "black", fg= "white") # See the parameters.
my_label.grid(row= 0, column= 0)

def click_button():
    user_input = my_entry.get()
    print(user_input)

# Entry
my_entry = tkinter.Entry(width= 20)
my_entry.grid(row= 1, column= 1) # It splits the screen 2 pieces. And puts the button second part.

# Button
my_button = tkinter.Button(text= "This is a button.", command= click_button)

my_button.update() # To get height and width infos for the button. Otherwise you'll get 1.
print(my_button.winfo_height())
print(my_button.winfo_width())

my_button.grid(row= 2, column= 2) # It splits the screen 3 pieces. And puts the button third part.

window.mainloop()