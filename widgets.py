from tkinter import *
# Creating new window and configuration
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Creating Labels
label = Label(text ="This is old text ")
label.config(text = "This is new text")
label.pack()

# Buttons
def action():
    print("Do something")

# Call Action function when button is clicked
button = Button(text = "Click Me" ,command = action)
button.pack()

# Entries
input_text = Entry(width=60)
# Add some text to begin with
input_text.insert(END, string="Some text to begin with,")
# Get text in input_text(entry)
print(input_text.get())

input_text.pack()

# Text
text = Text(height=5, width=30)
#Put Cursor in Textbox
text.focus()
# Add some text to begin with
text.insert(END, "Example of multiline text")

# Gets current value in textbox at line1, character 0
print(text.get("1.0",END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100,command=scale_used)
scale.pack()

#CheckButtons
def checkbutton_used():
    # Print 1 if CheckButton checked,Otherwise 0.
    print(checked_state.get())

# Variable to hold on to checked state, 0 is off and 1 is On.
checked_state=IntVar()
checkbutton = Checkbutton(text="Is On?",variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#RadioButton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",value=1, variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2",value=2, variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(listbox):
    # Get Current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple","Mango","Pears","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()



window.mainloop()