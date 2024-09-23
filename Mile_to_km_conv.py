from tkinter import*
# Create new window and configuration
window =Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height =150)

def cal_mile_km():
    km = float(miles_input.get()) * float(1.60934)
    km_output.config(text=km)


# creating Labels first
miles = Label(text="Miles")
miles.grid(column=2,row=0,padx=10,pady=10)

is_eql =Label(text="is equal to")
is_eql.grid(column=0,row=1,padx=10,pady=10)

#Km
km_lbl=Label(text="Km")
km_lbl.grid(column=2,row=1,padx=10,pady=10)


#Create Entry field to get input in miles
miles_input = Entry(width=20)
miles_input.grid(column =1, row=0,padx=10,pady=10)

# Create Button
cal_btn = Button(text="Calculate",command=cal_mile_km)
cal_btn.grid(column=1,row=2,padx=10,pady=10)


km_output = Label(text = 0)
km_output.grid(column=1, row=1,padx=10,pady=10)






window.mainloop()