from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width =500 ,height =300)
window.config(padx=50, pady=50)

def button_clicked():
    my_label.config(text= input.get())



#Lable
my_label = Label(text="I m a Label", font = ("Arial",24,"bold"))
my_label["text"] = "New_label"
#my_label.config(text="New Text")
#my_label.pack()
# Instead of pack, we can we use place where we can specify x and Y co-ordinates
#my_label.place(x=0,y=0)
#Instaed pf place and pack we can use grid to place item on the screen
my_label.grid(column=0, row=0, padx=20, pady=20)

# Buttons
my_button = Button(text = "Click Me", command =button_clicked)
#my_button.pack()
my_button.grid(column=1, row=1, padx=20, pady=20)

def new_button_clicked():
    print("new Button is clicked")

new_button = Button(text="New_Button", command=new_button_clicked)
new_button.grid(column =2,row=0, padx=20, pady=20)

# Input Field (entry)
input = Entry(width = 20)  # Entry is class from Tkinter module
#input.pack()
input.grid(column=3, row=3,padx=20, pady=20)




window.mainloop()