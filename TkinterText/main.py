from tkinter import *

# Window
window = Tk()
window.title("Tkinter Screen")
window.minsize(width= 600, height= 600)
window.config(padx= 25, pady= 25) # Moves away from the edges.

text = Text(width= 30, height= 5)
text.focus() # To give priority.
text.pack()

def write_text():
    print(text.get("1.0", END)) # To start at first row.
    #print(text.get("2.0", END))  # To start at second row.

button_of_text = Button(text= "Send", command= write_text)
button_of_text.pack()

window.mainloop()