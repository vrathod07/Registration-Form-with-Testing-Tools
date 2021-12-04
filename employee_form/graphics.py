import tkinter
from tkinter import *
from main import *


root = Tk()
root.geometry("500x500")

#declaring string variable
name = tkinter.StringVar()
username = tkinter.StringVar()
date_of_joining =tkinter.StringVar()
birth_date = tkinter.StringVar()
phone_number = tkinter.IntVar()
Designation = tkinter.StringVar()
Street = tkinter.StringVar()
City = tkinter.StringVar()
State = tkinter.StringVar()
Zip_code= tkinter.StringVar()
email_var = tkinter.StringVar()
passw_var = tkinter.StringVar()

def quit():
    global root
    root.quit()

def submit():

    name_var = name.get()
    username_var = username.get()
    doj = date_of_joining.get()
    dob = birth_date.get()
    number = phone_number.get()
    designation = Designation.get()
    street = Street.get()
    city = City.get()
    state= State.get()
    zip = Zip_code.get()
    email = email_var.get()
    password = passw_var.get()

    name.set("")
    username.set("")
    date_of_joining.set("")
    birth_date.set("")
    phone_number.set("")
    Designation.set("")
    Street.set("")
    City.set("")
    State.set("")
    Zip_code.set("")
    email_var.set("")
    passw_var.set("")

    x = [name_var,username_var,email,password,doj,dob,number,designation,street,city,state,zip] #name ,username,email,password,jod,dob,number,designation,street,city,state,zip
    y = []
    y.append(x)
    emp = Employee(x)
    emp.create_file()
    print(x)

name_label = tkinter.Label(root,text="Name", font=('Arial',20))
name_entry = tkinter.Entry(root, textvariable=name, font=('Arial', 20, 'normal'))

username_label = tkinter.Label(root,text="Username", font=('Arial',20))
username_entry = tkinter.Entry(root, textvariable=username, font=('Arial', 20, 'normal'))

doj_label = tkinter.Label(root,text="Date of Joining", font=('Arial',20))
doj_entry = tkinter.Entry(root, textvariable=date_of_joining, font=('Arial', 20, 'normal'))

dob_label = tkinter.Label(root,text="Birth Date", font=('Arial',20))
dob_entry = tkinter.Entry(root, textvariable=birth_date, font=('Arial', 20, 'normal'))

email_label = tkinter.Label(root,text="email", font=('Arial',20))
email_entry = tkinter.Entry(root, textvariable=email_var, font=('Arial', 20, 'normal'))

passw_label = tkinter.Label(root, text='Password', font=('Arial', 20))
passw_entry = tkinter.Entry(root, textvariable=passw_var, font=('Arial', 20, 'normal'), show='*')

number_label = tkinter.Label(root,text="Number", font=('Arial',20))
number_entry = tkinter.Entry(root, textvariable=phone_number, font=('Arial', 20, 'normal'))

Designation_label = tkinter.Label(root,text="Designation", font=('Arial',20))
Designation_entry = tkinter.Entry(root, textvariable=Designation, font=('Arial', 20, 'normal'))

Street_label = tkinter.Label(root,text="Street", font=('Arial',20))
Street_entry = tkinter.Entry(root, textvariable=Street, font=('Arial', 20, 'normal'))

City_label = tkinter.Label(root,text="City", font=('Arial',20))
City_entry = tkinter.Entry(root, textvariable=City, font=('Arial', 20, 'normal'))

State_label = tkinter.Label(root,text="State", font=('Arial',20))
State_entry = tkinter.Entry(root, textvariable=State, font=('Arial', 20, 'normal'))

zip_label = tkinter.Label(root,text="Zip", font=('Arial',20))
zip_entry = tkinter.Entry(root, textvariable=Zip_code, font=('Arial', 20, 'normal'))

button_submit = tkinter.Button(master=root, text="Submit", command=submit)
button_quit = tkinter.Button(master=root, text="Quit", command=quit)


name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1)
doj_label.grid(row=2,column=0)
doj_entry.grid(row=2,column=1)
dob_label.grid(row=3,column=0)
dob_entry.grid(row=3,column=1)
email_label.grid(row=4,column=0)
email_entry.grid(row=4,column=1)
passw_label.grid(row=5,column=0)
passw_entry.grid(row=5,column=1)
number_label.grid(row=6,column=0)
number_entry.grid(row=6,column=1)
Designation_label.grid(row=7,column=0)
Designation_entry.grid(row=7,column=1)
Street_label.grid(row=8,column=0)
Street_entry.grid(row=8,column=1)
City_label.grid(row=9,column=0)
City_entry.grid(row=9,column=1)
State_label.grid(row=10,column=0)
State_entry.grid(row=10,column=1)
zip_label.grid(row=11,column=0)
zip_entry.grid(row=11,column=1)

button_submit.grid(row=12,column=0)
button_quit.grid(row=12,column=1)



root.mainloop()