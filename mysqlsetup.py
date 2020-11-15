#############################       MySQL SETUP      ################################

import mysql.connector as sqltor
from tkinter import *
from tkinter import messagebox

# This is a tkinter window to get the values of the MySQL database from the user.
myconwin=Tk()
myconwin.title('MySQL configuration')
myconwin.geometry('780x490')
myconwin.configure(bg='darkorange')
label1=Label(myconwin, text="Welcome to MySQL setup!",bg='darkorange' ,font=("Century",21,'underline'))
label1.pack()
label2=Label(myconwin, text="Please enter the following...",bg='darkorange',font=("Gabriola",27))
label2.place(x=220, y=68)
label3=Label(myconwin, text=" MySQL Userame :",bg='darkorange' ,font=("Calibri",21)).place(x=77,y=189)
label4=Label(myconwin, text="MySQL Password :",bg='darkorange', font=('Calibri',21)).place(x=77,y=257)
label4=Label(myconwin, text="Database Name :",bg='darkorange', font=('Calibri',21)).place(x=77,y=326)

#These are functions for the action that will take place when button is clicked.
def submitclick():
# This will take the database values (username,passwd,db name) and store it in a '.txt' file in same location.
    a=entry1.get()
    b=entry2.get()
    c=entry3.get()
    d=","
    e=a+d+b+d+c
#  FILE HANDLING
    txtfile=open("Credentials.txt" , "w")
    txtfile.write(e)
    txtfile.close()
    mycon=sqltor.connect(host="localhost",user=a ,passwd=b,database="mysql")
    cursor=mycon.cursor()

#  DATABASE CREATION
    cursor.execute("create database {}".format(c))
    cursor.execute("use {}".format(c))

#  TABLE CREATION
    cursor.execute("""create table customers(
Ticket_No int,
Name char(69),
Phone_No bigint,
Source char(74),
Destination char(73),
Date_Of_Travel date,
Time time,
Class_Type char(76))""")
    cursor.execute('''create table flightinfo(
FlightNo char(9),
Aircraft_Type char(10),
Source char(62),
Destination char(62),
Status char(12),
Date date,
Time time)''')
    cursor.execute('''create table pilots(
empid char(4),
Name char(69),
Phone bigint,
Hiredate date,
Based_Location char(32),
Salary int)''')
    cursor.execute('''create table cabincrew(
empid char(4),
Name char(69),
Phone bigint,
HireDate date,
Based_Location char(32),
Salary int)''')
    cursor.execute('''create table airportstaffs(
empid char(4),
Name char(69),
Phone bigint,
HireDate date,
Based_Location char(32),
Salary int)''')
    cursor.execute('''create table me(
empid char(4),
Name char(69),
Phone bigint,
HireDate date,
Based_Location char(32),
Salary int)''')
    cursor.execute('''create table fleet(
Aircraft_Manufacturer char(16),
Aircraft_Model char(17),
Reg_No char(6))''')
    cursor.execute('''create table pantry(
Item_Name char(19),
Price int,
Stock int)''')
    cursor.execute('''create table expenses(
Particulars char(26),
Amount_Rs int)''')
    cursor.execute('''create table income(
Particulars char(26),
Amount_Rs int)''')
    mycon.commit()
    mycon.close()
    messagebox.showinfo("Information","Connection Successful.")
    myconwin.destroy()
def closeclick():
    myconwin.destroy()
button1=Button(myconwin, text="Submit",command=submitclick ,fg='lime',font=("Bold",20))
button1.place(x=509, y=402)
button2=Button(myconwin, text="Close",command=closeclick, fg='red2',font=("Bold",20)).place(x=649, y=402)
entry1=Entry(myconwin, width=40)
entry1.place(x=337,y=200)
entry2=Entry(myconwin, width=40)
entry2.place(x=337,y=268)
entry3=Entry(myconwin, width=40)
entry3.place(x=337,y=337)
myconwin.mainloop()

####################################
#                 Program ends!!  :)                            #
####################################
