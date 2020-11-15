###################                      AIRLINE MANAGEMENT                   ####################

from tkinter.ttk import Combobox
import mysql.connector as sqltor
from tkinter import *
from tkinter import messagebox as mb
import datetime
from tkcalendar import *
import random

# File handling for the username, password and db name.
credentials=open('G:\DavesPython\Credentials.txt')
listt=credentials.read()
l1=listt.split(',')
mycon=sqltor.connect(host='localhost', user=l1[0], passwd=l1[1], database=l1[2])
cursor=mycon.cursor()

# Used for getting current date
now = datetime.datetime.now()

# This function is for authentication of user (Login Screen)
def loginwindow():
    loginwin=Tk()
    loginwin.title("Login Page")
    loginwin.geometry('600x400')
    loginwin.configure(bg='darkorange2')
    label1=Label(loginwin, text= "Login to enter :",bg='darkorange2', font=("Consolas Bold",21, 'underline')).pack()
    label1=Label(loginwin, text= "Username :",bg='darkorange2', font=("Century",16)).place(x=7, y=69)
    label1=Label(loginwin, text= "Password  :",bg='darkorange2', font=("Century",16)).place(x=7, y=128)
    e1=Entry(loginwin, width=29)
    e1.place(x=190, y=75)
    e2=Entry(loginwin, width=29)
    e2.place(x=190, y=135)
    username='admin'
    password='password'
    def loginclick():
        if e1.get()==username:
            if e2.get()==password:
                loginwin.destroy()
                mainwindow()
            else:
               mb.showerror('Error', 'The password is incorrect.\n\nPlease check and re-enter the password.')
        else:
            mb.showerror('Error', 'There is no user like this.\n\nPlease check and re-enter the username.')
    button=Button(loginwin, text='Login', bg='burlywood2',command=loginclick, font=("Bold",18)).place(x=430, y=93)
    loginwin.mainloop()

# Home Screen Window
def mainwindow():
    mainwin=Tk()
    mainwin.title("Airline Management")
    mainwin.geometry('780x490')
    mainwin.configure(bg='darkolivegreen')

    lbl=Label(mainwin, text="Hi !",bg='darkolivegreen', font=("Arial Bold Italic",37)).place(x=340,y=30)
    lbl2=Label(mainwin, text='Welcome to Python Airlines !!', fg='blue',bg='yellow', font=("Times New Roman",28,'underline')).place(x=202,y=111)
    def customerclick():
        mainwin.destroy()
        customerwindow()
    def employeeclick():
        mainwin.destroy()
        employeewindow()
    def adminclick():
        mainwin.destroy()
        adminwindow()
    def aboutclick():
        mainwin.destroy()
        aboutwindow()
    def closeclick():
        mainwin.destroy()
        
    btn=Button(mainwin, text="Customers", command=customerclick, font=("Bold",20)).place(x=73, y=209)
    btn1=Button(mainwin, text="Employees", command=employeeclick, font=("Bold",20)).place(x=529, y=209)
    btn2=Button(mainwin, text="Admin", command=adminclick, font=("Bold",20)).place(x=338,y=298)
    btn3=Button(mainwin, text="About", command=aboutclick, font=("Bold",20)).place(x=74, y=374)
    btn4=Button(mainwin, text="Exit ", command=closeclick, fg='red',font=("Bold",19)).place(x=568, y=374)

# Customer Screen
def customerwindow():
    customerwin=Tk()
    customerwin.title('Menu-->Customer')
    customerwin.geometry('900x600')
    customerwin.configure(bg='cadet blue')
    lbl4=Label(customerwin, text="Please select an option below...", bg='Gold',font=("Aharoni Bold",21, 'underline')).place(x=239,y=120)
    def ticketbookingclick():
        customerwin.destroy()
        ticketbookingwindow()
    def ticketstatusclick():
        customerwin.destroy()
        ticketstatuswindow()
    def ticketcancelclick():
        customerwin.destroy()
        ticketcancelwindow()
    def viewflightsclick():
        customerwin.destroy()
        viewflightswindow()
    def cusbackclick():
        customerwin.destroy()
        mainwindow()
    btn5=Button(customerwin, text="Ticket Booking", command=ticketbookingclick, fg='green',font=("Bold",20)).place(x=129, y=229)
    btn6=Button(customerwin, text="Ticket Status",command=ticketstatusclick, fg='blue',font=("Bold",20)).place(x=538, y=229)
    btn20=Button(customerwin, text="Ticket Cancellation",command=ticketcancelclick,font=("Bold",20)).place(x=103, y=388)
    btn21=Button(customerwin, text="View Flights",fg='brown',command=viewflightsclick,font=("Bold",20)).place(x=542, y=388)
    btn22=Button(customerwin, text="Back",command=cusbackclick, fg='red',font=("Bold",19)).place(x=767, y=513)

# Employees Screen
def employeewindow():
    employeewin=Tk()
    employeewin.title('Menu-->Employee')
    employeewin.geometry('900x600')
    employeewin.configure(bg='dark olive green')
    
    lbl13=Label(employeewin, text="Please select an option below...", bg='Gold',font=("Aharoni Bold",21, 'underline')).place(x=239,y=120)

    def pilotsclick():
        employeewin.destroy()
        pilotswindow()
    def cabincrewclick():
        employeewin.destroy()
        cabincrewwindow()
    def maintenanceengineersclick():
        employeewin.destroy()
        maintenanceengineerswindow()
    def airportstaffsclick():
        employeewin.destroy()
        airportstaffswindow()
    def empbackclick():
        employeewin.destroy()
        mainwindow()
    btn8=Button(employeewin, text="Pilots",command=pilotsclick, fg='dodger blue',font=("Bold",20)).place(x=91, y=321)
    btn9=Button(employeewin, text="Cabin Crew",command=cabincrewclick, fg='deep pink',font=("Bold",20)).place(x=272, y=319)
    btn10=Button(employeewin, text="Maintenance Engineers",command=maintenanceengineersclick, fg='gray17',font=("Bold",20)).place(x=197, y=457)
    btn11=Button(employeewin, text=" Airport Staffs",command=airportstaffsclick, fg='forest green',font=("Bold",20)).place(x=538, y=319)
    btn12=Button(employeewin, text="Back",command=empbackclick, fg='red',font=("Bold",18)).place(x=777, y=497)

# Admin Screen
def adminwindow():
    adminwin=Tk()
    adminwin.title('Menu-->Admin')
    adminwin.geometry('780x490')
    adminwin.configure(bg='darkolivegreen')

    lbl40=Label(adminwin,  text='Please select an option below:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack(pady=41)
    def pantryclick():
        adminwin.destroy()
        pantrywindow()
    def incomeclick():
        adminwin.destroy()
        incomewindow()
    def expensesclick():
        adminwin.destroy()
        expwindow()
    def fleetclick():
        adminwin.destroy()
        fleetwindow()
    def admbackclick():
        adminwin.destroy()
        mainwindow()
    buton1=Button(adminwin, text="Pantry",fg='saddle brown',command=pantryclick,font=("Bold",20)).place(x=73, y=209)
    buton2=Button(adminwin, text="Income",fg='cornsilk4',command=incomeclick,font=("Bold",20)).place(x=529, y=209)
    buton3=Button(adminwin, text="Expenses",fg='orange red',command=expensesclick,font=("Bold",20)).place(x=74, y=373)
    buton4=Button(adminwin, text="Fleet",fg='deepskyblue4',command=fleetclick,font=("Bold",20)).place(x=338, y=298)
    buton5=Button(adminwin, text="Back",fg='red',command=admbackclick,font=("Bold",20)).place(x=568, y=374)

# About Screen
def aboutwindow():
    aboutwin=Tk()
    aboutwin.title('Menu-->About')
    aboutwin.geometry('1100x600')
    aboutwin.configure(bg='darkolivegreen')

    lbl14=Label(aboutwin, text='Credits :', bg='darkolivegreen',font=("Century",41,'underline')).place(x=2,y=8)
    lbl15=Label(aboutwin, text='''Mukund Krishnan . V \n
    12-\'C\' (Commerce with Computer Science)''',fg='gold', bg='darkolivegreen',font=("Gisha Bold",17)).place(x=5,y=118)
    lbl16=Label(aboutwin, text='''Thrinethra . J\n
    12-\'A\' (Biology with Computer Science)''',fg='gold', bg='darkolivegreen',font=("Gisha Bold",18)).place(x=5,y=374)
    lbl17=Label(aboutwin, text='and', bg='darkolivegreen',font=("Consolas",31)).place(x=193,y=257)
    lbl18=Label(aboutwin, text='OF', bg='darkolivegreen',font=("Constantia",34)).place(x=541,y=257)
    lbl19=Label(aboutwin, text='''Amrita Vidyalayam,
    TRICHY''', bg='gold',font=("Gigi",26)).place(x=708,y=246)
    def abbackclick():
        aboutwin.destroy()
        mainwindow()
    btn19=Button(aboutwin, text="Back",fg='red2',command=abbackclick, font=("Bold",23)).place(x=989, y=506)


# Functions for all the buttons

# Functions for Customer Screen
def ticketbookingwindow():
    ticketbookingwin=Tk()
    ticketbookingwin.title("Menu-->Customer-->Ticket Booking")
    ticketbookingwin.geometry('700x600')
    ticketbookingwin.configure(bg='peachpuff3')

    lbl20=Label(ticketbookingwin,  text='Please enter the following details:', bg='peachpuff3', font=('Consolas Bold',21,'underline')).pack()
    lbl21=Label(ticketbookingwin, text='Name :',bg='peachpuff3', font=('Century',18)).place(x=39, y=86)
    lbl22=Label(ticketbookingwin, text='Phone number :',bg='peachpuff3', font=('Century',18)).place(x=38, y=127)
    lbl23=Label(ticketbookingwin, text='Source :',bg='peachpuff3', font=('Century',18)).place(x=39, y=168)
    lbl24=Label(ticketbookingwin, text='Destination :',bg='peachpuff3', font=('Century',18)).place(x=39, y=201)
    lbl25=Label(ticketbookingwin, text='Date of Travel :',bg='peachpuff3', font=('Century',17)).place(x=39, y=242)
    lbl26=Label(ticketbookingwin, text='Time :',bg='peachpuff3', font=('Century',18)).place(x=39, y=303)
    lbl27=Label(ticketbookingwin,text='Class Type:', bg='peachpuff3', font=('Century',18)).place(x=39,y=398)

    ticketno=random.randint(10000,50000)
    ent1=Entry(ticketbookingwin, width=45)
    ent1.place(x=334,y=93)
    ent2=Entry(ticketbookingwin, width=45)
    ent2.place(x=334,y=134)
    cmb1=Combobox(ticketbookingwin)
    cmb1['values']=('Select your Source city:','Delhi','Kolkata','Mumbai','Chennai','Cochin','Dubai')
    cmb1.current(0)
    cmb1.place(x=334,y=175)
    
    cmb2=Combobox(ticketbookingwin)
    cmb2['values']=('Select your Destination:','Delhi','Mumbai','Kolkata','Chennai','Cochin','Dubai')
    cmb2.current(0)
    cmb2.place(x=334,y=208)

    today=datetime.date.today()
    mindate=datetime.date(year=2020, month=10, day=1)
    maxdate=today+datetime.timedelta(days=90)
    cal=Calendar(ticketbookingwin, selectmode='day', year=2020, month=11, mindate=mindate, maxdate=maxdate, showweeknumbers=False, firstweekday="sunday")
    cal.config(date_pattern="yyyy-mm-dd")
    cal.place(x=334,y=249)
    
    cmb4=Combobox(ticketbookingwin)
    cmb4['values']=('Select a Time:','09:30:00','10:30:00','12:30:00','13:45:00','18:45:00','20:00:00','22:00:00')
    cmb4.current(0)
    cmb4.place(x=39, y=346)
    
    cmb5=Combobox(ticketbookingwin)
    cmb5['values']=('Select a class:','Economy','Premium_Economy', 'Business_Class','First_Class')
    cmb5.current(0)
    cmb5.place(x=39,y=441)
    def tbsubmit():
        var1="""INSERT INTO customers
        VALUES({},'{}',{},'{}','{}','{}','{}','{}')""".format(ticketno,ent1.get(),ent2.get(),cmb1.get(),cmb2.get(),cal.get_date(),cmb4.get(),cmb5.get())
        cursor.execute(var1)
        mycon.commit()
        mb.showinfo("Information","Data successfully submitted.")

    def tbclose():
        ticketbookingwin.destroy()
        customerwindow()

    btn23=Button(ticketbookingwin, text='Submit',fg='darkgreen',command=tbsubmit, font=('Bold',21)).place(x=429,y=520)
    btn24=Button(ticketbookingwin, text='Back',fg='red2',command=tbclose, font=('Bold',21)).place(x=565,y=520)

def ticketstatuswindow():
    ticketstatuswin=Tk()
    ticketstatuswin.title("Menu-->Customer-->Ticket Status")
    ticketstatuswin.geometry('1000x600')
    ticketstatuswin.configure(bg='peachpuff4')

    lbl27=Label(ticketstatuswin, text='Please enter your Phone Number:', bg='peachpuff4',font=('Consolas Bold',21,'underline')).pack(pady=13)
    lbl28=Label(ticketstatuswin, text='Phone Number:', bg='peachpuff4', font=('Century',18)).pack(pady=32)
    ent3=Entry(ticketstatuswin, width=45)
    ent3.pack()
    def checkstatusclick():
        var2="""SELECT * FROM customers
                WHERE Phone_No={}""".format(ent3.get())
        cursor.execute(var2)
        records=cursor.fetchall()
        lbl29=Label(ticketstatuswin, text=records, bg='peachpuff4',font=('Gill Sans MT',17)).pack(pady=183)
        lbl30=Label(ticketstatuswin, text='{Ticket Number, Name, Phone Number, Source, Destination, Date of travel, Flight time, Class}', bg='yellow',font=('Gill Sans MT',17)).place(x=57,y=420)
    def statusbackclick():
        ticketstatuswin.destroy()
        customerwindow()
    btn25=Button(ticketstatuswin, text='Check Status', fg='darkgreen', command=checkstatusclick, font=('Bold',19)).place(x=390,y=213)
    btn26=Button(ticketstatuswin, text='Back', fg='red', command=statusbackclick, font=('Bold',19)).place(x=599,y=213)
    
def ticketcancelwindow():
    ticketcancelwin=Tk()
    ticketcancelwin.title("Menu-->Customer-->Ticket Cancel")
    ticketcancelwin.geometry('600x400')
    ticketcancelwin.configure(bg='peachpuff3')
    
    lbl31=Label(ticketcancelwin, text='Please enter your Phone Number:', bg='peachpuff3',font=('Consolas Bold',21,'underline')).pack(pady=13)
    ent4=Entry(ticketcancelwin, width=35)
    ent4.pack()
    def cancelclick():
        res=''
        res=mb.askyesno('Confirmation','Are you sure?\n\nThis will delete your record from the database.')
        if res==True:
            var3="""DELETE FROM CUSTOMERS
                    WHERE Phone_No={}""".format(ent4.get())
            cursor.execute(var3)
            mycon.commit()
            mb.showinfo('Information','Record deleted successfully.')
    def cancelbackclick():
        ticketcancelwin.destroy()
        customerwindow()
    btn27=Button(ticketcancelwin, text='Submit', fg='darkgreen', command=cancelclick, font=('Bold',19)).place(x=339,y=325)
    btn28=Button(ticketcancelwin, text='Back', fg='red', command=cancelbackclick, font=('Bold',19)).place(x=472,y=325)
def viewflightswindow():
    viewflightswin=Tk()
    viewflightswin.title("Menu-->Customer-->View Flights")
    viewflightswin.geometry('900x500')
    viewflightswin.configure(bg='tan4')

    var5="SELECT*FROM flightinfo"
    cursor.execute(var5)
    num=0
    for flightinfo in cursor:
        for j in range(len(flightinfo)):
            ent5=Entry(viewflightswin, width=12,font=('Gill Sans MT',16))
            ent5.grid(row=num,column=j)
            ent5.insert(END,flightinfo[j])
        num=num+1
    def viewflightsaddclick():
        viewflightswin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Customer-->View Flights-->Add Flight")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Flight Number :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=45)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Aircraft Type :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=45)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Source :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=45)
        ent9.place(x=334,y=175)
        lbl34=Label(addpilotwin, text='Destination :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=209)
        ent10=Entry(addpilotwin, width=45)
        ent10.place(x=334,y=216)
        lbl34=Label(addpilotwin, text='Status :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=250)
        ent11=Entry(addpilotwin, width=45)
        ent11.place(x=334,y=257)
        lbl34=Label(addpilotwin, text='Date :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=291)
        ent12=Entry(addpilotwin, width=45)
        ent12.place(x=334,y=298)
        lbl34=Label(addpilotwin, text='Time :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=332)
        ent13=Entry(addpilotwin, width=45)
        ent13.place(x=334,y=339)
        def addsubmit():
            var="""INSERT INTO flightinfo
                         VALUES('{}','{}','{}','{}','{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get(),ent13.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            viewflightswindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def viewflightsbackclick():
        viewflightswin.destroy()
        customerwindow()
    btn29=Button(viewflightswin, text='Add', fg='darkgreen', command=viewflightsaddclick, font=('Bold',19)).grid(column=2,row=11)
    btn30=Button(viewflightswin, text='Back', fg='red', command=viewflightsbackclick, font=('Bold',19)).grid(column=3,row=11)


# Functions for Employee Screen
def pilotswindow():
    pilotswin=Tk()
    pilotswin.title("Menu-->Employee-->Pilots")
    pilotswin.geometry('900x500')
    pilotswin.configure(bg='tan4')

    var5="SELECT*FROM pilots"
    cursor.execute(var5)
    num=0
    for pilot in cursor:
        for j in range(len(pilot)):
            ent5=Entry(pilotswin, width=14,font=('Gill Sans MT',16))
            ent5.grid(row=num,column=j)
            ent5.insert(END,pilot[j])
        num=num+1
    def pilotsaddclick():
        pilotswin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Employee-->Pilots-->Add Pilot")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Employer ID :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=45)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Name :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=45)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Phone number :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=45)
        ent9.place(x=334,y=175)
        lbl34=Label(addpilotwin, text='Hire Date :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=209)
        ent10=Entry(addpilotwin, width=45)
        ent10.place(x=334,y=216)
        lbl34=Label(addpilotwin, text='Based Location :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=250)
        ent11=Entry(addpilotwin, width=45)
        ent11.place(x=334,y=257)
        lbl34=Label(addpilotwin, text='Salary :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=291)
        ent12=Entry(addpilotwin, width=45)
        ent12.place(x=334,y=298)
        def addsubmit():
            var="""INSERT INTO pilots
                         VALUES('{}','{}',{},'{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            pilotswindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def pilotsbackclick():
        pilotswin.destroy()
        employeewindow()
    btn29=Button(pilotswin, text='Add', fg='darkgreen', command=pilotsaddclick, font=('Bold',19)).grid(column=2,row=11)
    btn30=Button(pilotswin, text='Back', fg='red', command=pilotsbackclick, font=('Bold',19)).grid(column=3,row=11) 
def cabincrewwindow():
    cabincrewwin=Tk()
    cabincrewwin.title("Menu-->Employee-->Cabin Crew")
    cabincrewwin.geometry('900x500')
    cabincrewwin.configure(bg='darkolivegreen')

    var6="SELECT*FROM cabincrew"
    cursor.execute(var6)
    num=0
    for cabincrew in cursor:
        for j in range(len(cabincrew)):
            ent13=Entry(cabincrewwin, width=14,font=('Gill Sans MT',16))
            ent13.grid(row=num,column=j)
            ent13.insert(END,cabincrew[j])
        num=num+1
    def cabincrewaddclick():
        cabincrewwin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Employee-->Pilots-->Add Cabin Crew")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Employer ID :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=45)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Name :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=45)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Phone number :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=45)
        ent9.place(x=334,y=175)
        lbl34=Label(addpilotwin, text='Hire Date :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=209)
        ent10=Entry(addpilotwin, width=45)
        ent10.place(x=334,y=216)
        lbl34=Label(addpilotwin, text='Based Location :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=250)
        ent11=Entry(addpilotwin, width=45)
        ent11.place(x=334,y=257)
        lbl34=Label(addpilotwin, text='Salary :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=291)
        ent12=Entry(addpilotwin, width=45)
        ent12.place(x=334,y=298)
        def addsubmit():
            var="""INSERT INTO cabincrew
                         VALUES('{}','{}',{},'{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            cabincrewwindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def cabinbackclick():
        cabincrewwin.destroy()
        employeewindow()
        
    btn29=Button(cabincrewwin, text='Add', fg='darkgreen', command=cabincrewaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(cabincrewwin, text='Back', fg='red', command=cabinbackclick, font=('Bold',19)).grid(column=3,row=10)

def airportstaffswindow():
    airportstaffswin=Tk()
    airportstaffswin.title("Menu-->Employee-->Airport Staff")
    airportstaffswin.geometry('900x500')
    airportstaffswin.configure(bg='darkolivegreen')

    var6="SELECT*FROM airportstaffs"
    cursor.execute(var6)
    num=0
    for airportstaffs in cursor:
        for j in range(len(airportstaffs)):
            ent13=Entry(airportstaffswin, width=14,font=('Gill Sans MT',16))
            ent13.grid(row=num,column=j)
            ent13.insert(END,airportstaffs[j])
        num=num+1
    def airportstaffsaddclick():
        airportstaffswin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Employee-->Pilots-->Add Airport Staff")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Employer ID :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=45)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Name :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=45)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Phone number :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=45)
        ent9.place(x=334,y=175)
        lbl34=Label(addpilotwin, text='Hire Date :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=209)
        ent10=Entry(addpilotwin, width=45)
        ent10.place(x=334,y=216)
        lbl34=Label(addpilotwin, text='Based Location :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=250)
        ent11=Entry(addpilotwin, width=45)
        ent11.place(x=334,y=257)
        lbl34=Label(addpilotwin, text='Salary :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=291)
        ent12=Entry(addpilotwin, width=45)
        ent12.place(x=334,y=298)
        def addsubmit():
            var="""INSERT INTO airportstaffs
                         VALUES('{}','{}',{},'{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            airportstaffswindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def asbackclick():
        airportstaffswin.destroy()
        employeewindow()
        
    btn29=Button(airportstaffswin, text='Add', fg='darkgreen', command=airportstaffsaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(airportstaffswin, text='Back', fg='red', command=asbackclick, font=('Bold',19)).grid(column=3,row=10)

def maintenanceengineerswindow():
    maintenanceengineerswin=Tk()
    maintenanceengineerswin.title("Menu-->Employee-->Maintenance Engineers")
    maintenanceengineerswin.geometry('900x500')
    maintenanceengineerswin.configure(bg='darkolivegreen')

    var6="SELECT*FROM me"
    cursor.execute(var6)
    num=0
    for maintenanceengineers in cursor:
        for j in range(len(maintenanceengineers)):
            ent13=Entry(maintenanceengineerswin, width=14,font=('Gill Sans MT',16))
            ent13.grid(row=num,column=j)
            ent13.insert(END,maintenanceengineers[j])
        num=num+1
    def maintenanceengineersaddclick():
        maintenanceengineerswin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Employee-->Pilots-->Add Maintenance Engineer")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Employer ID :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=45)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Name :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=45)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Phone number :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=45)
        ent9.place(x=334,y=175)
        lbl34=Label(addpilotwin, text='Hire Date :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=209)
        ent10=Entry(addpilotwin, width=45)
        ent10.place(x=334,y=216)
        lbl34=Label(addpilotwin, text='Based Location :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=250)
        ent11=Entry(addpilotwin, width=45)
        ent11.place(x=334,y=257)
        lbl34=Label(addpilotwin, text='Salary :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=291)
        ent12=Entry(addpilotwin, width=45)
        ent12.place(x=334,y=298)
        def addsubmit():
            var="""INSERT INTO me
                         VALUES('{}','{}',{},'{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            maintenanceengineerswindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def asbackclick():
        maintenanceengineerswin.destroy()
        employeewindow()
        
    btn29=Button(maintenanceengineerswin, text='Add', fg='darkgreen', command=maintenanceengineersaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(maintenanceengineerswin, text='Back', fg='red', command=asbackclick, font=('Bold',19)).grid(column=3,row=10)

# Functions for Admin Screen
def pantrywindow():
    pantrywin=Tk()
    pantrywin.title("Menu-->Admin-->Pantry")
    pantrywin.geometry('900x500')
    pantrywin.configure(bg='darkolivegreen')

    var6="SELECT*FROM pantry"
    cursor.execute(var6)
    num=0
    for pantry in cursor:
        for j in range(len(pantry)):
            ent13=Entry(pantrywin, width=19,font=('Gill Sans MT',18))
            ent13.grid(row=num,column=j)
            ent13.insert(END,pantry[j])
        num=num+1
    def pantryaddclick():
        pantrywin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Admin-->Pantry-->Add Pantry Item")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Item Name :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=40)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Price :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=40)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Stock :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=40)
        ent9.place(x=334,y=175)
        def addsubmit():
            var="""INSERT INTO pantry
                         VALUES('{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            pantrywindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def asbackclick():
        pantrywin.destroy()
        adminwindow()
        
    btn29=Button(pantrywin, text='Add', fg='darkgreen', command=pantryaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(pantrywin, text='Back', fg='red', command=asbackclick, font=('Bold',19)).grid(column=3,row=10)

def fleetwindow():
    fleetwin=Tk()
    fleetwin.title("Menu-->Admin-->Fleet")
    fleetwin.geometry('900x500')
    fleetwin.configure(bg='darkolivegreen')

    var6="SELECT*FROM fleet"
    cursor.execute(var6)
    num=0
    for fleet in cursor:
        for j in range(len(fleet)):
            ent13=Entry(fleetwin, width=14,font=('Gill Sans MT',18))
            ent13.grid(row=num,column=j)
            ent13.insert(END,fleet[j])
        num=num+1
    def fleetaddclick():
        fleetwin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Admin-->fleet-->Add Fleet Item")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Aircraft Manufacturer :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=40)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Model :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=40)
        ent8.place(x=334,y=134)
        lbl34=Label(addpilotwin, text='Registration Number :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=168)
        ent9=Entry(addpilotwin, width=40)
        ent9.place(x=334,y=175)
        def addsubmit():
            var="""INSERT INTO fleet
                         VALUES('{}','{}','{}')""".format(ent7.get(),ent8.get(),ent9.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            fleetwindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def asbackclick():
        fleetwin.destroy()
        adminwindow()
        
    btn29=Button(fleetwin, text='Add', fg='darkgreen', command=fleetaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(fleetwin, text='Back', fg='red', command=asbackclick, font=('Bold',19)).grid(column=3,row=10)

def expwindow():
    expenseswin=Tk()
    expenseswin.title("Menu-->Admin-->Expenses")
    expenseswin.geometry('900x500')
    expenseswin.configure(bg='darkolivegreen')

    var6="SELECT*FROM expenses"
    cursor.execute(var6)
    num=0
    for expenses in cursor:
        for j in range(len(expenses)):
            ent13=Entry(expenseswin, width=18,font=('Gill Sans MT',19))
            ent13.grid(row=num,column=j)
            ent13.insert(END,expenses[j])
        num=num+1
    def expensesaddclick():
        expenseswin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Admin-->Expenses-->Add Expenses")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Particulars :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=40)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Amount (In ₹) :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=40)
        ent8.place(x=334,y=134)
        def addsubmit():
            var="""INSERT INTO expenses
                         VALUES('{}',{})""".format(ent7.get(),ent8.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            expwindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def asbackclick():
        expenseswin.destroy()
        adminwindow()
        
    btn29=Button(expenseswin, text='Add', fg='darkgreen', command=expensesaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(expenseswin, text='Back', fg='red', command=asbackclick, font=('Bold',19)).grid(column=3,row=10)

def incomewindow():
    incomewin=Tk()
    incomewin.title("Menu-->Admin-->Income")
    incomewin.geometry('900x500')
    incomewin.configure(bg='darkolivegreen')

    var6="SELECT*FROM income"
    cursor.execute(var6)
    num=0
    for income in cursor:
        for j in range(len(income)):
            ent13=Entry(incomewin, width=18,font=('Gill Sans MT',19))
            ent13.grid(row=num,column=j)
            ent13.insert(END,income[j])
        num=num+1
    def incomeaddclick():
        incomewin.destroy()
        addpilotwin=Tk()
        addpilotwin.title("Menu-->Admin-->Income-->Add Income")
        addpilotwin.geometry('700x600')
        addpilotwin.configure(bg='darkolivegreen')

        lbl32=Label(addpilotwin,  text='Please enter the following details:', bg='darkolivegreen', font=('Consolas Bold',21,'underline')).pack()
        lbl33=Label(addpilotwin, text='Particulars :',bg='darkolivegreen', font=('Century',18)).place(x=39, y=86)
        ent7=Entry(addpilotwin, width=40)
        ent7.place(x=334,y=93)
        lbl34=Label(addpilotwin, text='Amount (In ₹) :',bg='darkolivegreen', font=('Century',18)).place(x=38, y=127)
        ent8=Entry(addpilotwin, width=40)
        ent8.place(x=334,y=134)
        def addsubmit():
            var="""INSERT INTO income
                         VALUES('{}',{})""".format(ent7.get(),ent8.get())
            cursor.execute(var)
            mycon.commit()
            mb.showinfo("Information","Data successfully submitted.")
        def addback():
            addpilotwin.destroy()
            incomewindow()
        btn23=Button(addpilotwin, text='Submit',fg='darkgreen',command=addsubmit, font=('Bold',21)).place(x=429,y=520)
        btn24=Button(addpilotwin, text='Back',fg='red2',command=addback, font=('Bold',21)).place(x=565,y=520)
    def asbackclick():
        incomewin.destroy()
        adminwindow()
    btn29=Button(incomewin, text='Add', fg='darkgreen', command=incomeaddclick, font=('Bold',19)).grid(column=2,row=10)
    btn30=Button(incomewin, text='Back', fg='red', command=asbackclick, font=('Bold',19)).grid(column=3,row=10)

##### Main Function  Call ####
loginwindow()             ####
##############################


################################################
#     Program finished successfully!! :)       #
################################################