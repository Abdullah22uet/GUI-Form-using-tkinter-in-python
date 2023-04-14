# This is a simple form using tkinter . 
# In this form we can enter name and father name and we can select checkbox and radio button. 
# We can also submit data and it will print in console.
# That's all.

import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.title("Application Form")
root.configure(background="#70066e")
root.geometry("500x600+50+50")
root.resizable(0,0)

#function of submit data
def print_data():
    print("----------- New data is entered -----------")
    name_of_student = e1.get( )
    father_of_student = e2.get( )
    checkbox_data = check_box.get()
    checkbox_data2 = check_box2.get()
    checkbox_data3 = check_box3.get()
    checkbox_data4 = check_box4.get()
    checkbox_data5 = check_box5.get()
    checkbox_data6 = check_box6.get()
    radio_data = radio_button.get()
    print("Name of student is : ",name_of_student)
    print("Father of student is : ",father_of_student)
    print("Checkbox data is : ",checkbox_data,checkbox_data2,checkbox_data3,checkbox_data4,checkbox_data5,checkbox_data6)
    print("Radio data is : ",radio_data)

#picture
img = PhotoImage(file='C:\\Users\\Dell\\Desktop\\Abdullah uet data\\python\\form\\real_uet_logo.png')
label1 = Label(root,image=img,bg="#70066e",).pack(pady=20)
heading = Label(root,text="Admission Form",font=("Arial",15),fg="orange",bg="#70066e",).pack(pady=20)

# Title and input boxes
student_name = Label(root,text="Enter name : ",font=("vardana",11),bg="#70066e",fg="white",).place(x=60,y=220)
e1= Entry(root,font=("vardana",12),bg="white",fg="black",)
e1.place(x=250,y=220)
father_name = Label(root,text="Enter father name : ",font=("vardana",11),bg="#70066e",fg="white",).place(x=60,y=250)
e2= Entry(root,font=("vardana",12),bg="white",fg="black",)
e2.place(x=250,y=250)

# checkboxes
check_content = Label(root,text="What languages you learn?",font=("vardana",11),bg="#70066e",fg="white",).place(x=60,y=300)
check_box = StringVar(value=0)
check_box2 = StringVar(value=0)
check_box3 = StringVar(value=0)
check_box4 = StringVar(value=0)
check_box5 = StringVar(value=0)
check_box6 = StringVar(value=0)
check1 = Checkbutton(root,text="Python",variable=check_box,onvalue="python:yes",offvalue="python:no",).place(x=60,y=330)
check2 = Checkbutton(root,text="Java",variable=check_box2,onvalue="java:yes",offvalue="java:no",).place(x=200,y=330)
check3 = Checkbutton(root,text="C++",variable=check_box3,onvalue="c++:yes",offvalue="c++:no",).place(x=350,y=330)
check4 = Checkbutton(root,text="Php",variable=check_box4,onvalue="php:yes",offvalue="php:no",).place(x=60,y=360)
check5 = Checkbutton(root,text="SQL",variable=check_box5,onvalue="SQL:yes",offvalue="SQL:no",).place(x=200,y=360)
check6 = Checkbutton(root,text="C#",variable=check_box6,onvalue="C#:yes",offvalue="C#:no",).place(x=350,y=360)

#radio button
radio_content = Label(root,text="Age?",font=("vardana",11),bg="#70066e",fg="white",).place(x=60,y=410)
radio_button = StringVar(value=False)
radio1 = Radiobutton(root,variable=radio_button,text="Above 18",value="above 18",).place(x=60,y=440)
radio2 = Radiobutton(root,variable=radio_button,text="Below 18",value="below 18",).place(x=60,y=470)

#button
btn = Button(root,text="Submit",font=("Arial",12),bg="orange",width=40,fg="black",relief=RIDGE,command=print_data,).place(x=70,y=530)

root.mainloop()

#end of code