# https://stackoverflow.com/questions/72567680/tkinter-combobox-variable-issue
# https://www.plus2net.com/python/tkinter-DateEntry.php

from customtkinter import *
from PIL import Image
from tkcalendar import DateEntry
# import tkinter.ttk as ttk
# from tkinter import *
import tkinter
import mysql.connector
from CTkMessagebox import CTkMessagebox
import datetime

app = CTk()
# app.grid_columnconfigure(0, weight=1)
# app.after(0, lambda:app.state('zoomed'))
app.attributes('-zoomed', True)
app.title("College")

db = mysql.connector.connect(host="localhost", user="root", password="", database="college_mgt")
mycursor = db.cursor()

gen = StringVar(value="Male")

def all_courses():
    # w = event.widget
    # w.event_generate('<Down>', when='head')
    # CTkMessagebox(frm, width=100, height=50, icon="check", icon_size=(20, 20), message="Record Inserted Successfully!")
    # print(choice)
    sql = "SELECT name FROM course"
    mycursor.execute(sql, )
    res = mycursor.fetchall()
    print(res)
    # lst = [i for i in res]
    # cmbcrs.set('-- SELECT COURSE --')
    lst = []
    for i in range(0, len(res)):
        # cmbcrs['values'] = i
        lst.append(res[i][0])
        print(res[i][0])
    print(lst)
    # lst_new = [i for i in lst]
    # cmbcrs['values'] = lst
    # cmbcrs.configure(values=lst)
    return lst

def get_year(event):
    # cmbyear.configure(values=[])
    course = cmbcrs.get()
    if course and course != "-- SELECT COURSE --":
        sql = "SELECT duration FROM course WHERE name=%s"
        values = (course,)
        mycursor.execute(sql, values)
        res = mycursor.fetchall()
        # cmbyear['values'] = []
        # cmbyear.configure(values=[])
        # cmbyear.set('-- SELECT YEAR --')
        lst = []
        for i in range(1, int(res[0][0][0]) + 1):
            lst.append(str(i))
        cmbyear['values'] = lst
        cmbyear.configure(values=lst)
        return lst
    else:
        CTkMessagebox(frm, width=100, height=50, icon="cancel", icon_size=(20, 20), message="Please select course")

def get_sem(event):
    # cmbsem.configure(values=[])
    dur = int(cmbyear.get())
    if dur and dur != "-- SELECT YEAR --":
        lst = []
        if dur == 1:
            lst.append("1")
            lst.append("2")
        elif dur == 2:
            lst.append("3")
            lst.append("4")
        elif dur == 3:
            lst.append("5")
            lst.append("6")
        else:
            lst.append("7")
            lst.append("8")
        cmbsem['values'] = lst
        cmbsem.configure(values=lst)
        return lst
    else:
        CTkMessagebox(frm, width=100, height=50, icon="cancel", icon_size=(20, 20), message="Please select year")


lst1 = all_courses()
# lst2 = get_year()

def insert():
    name = txtnm.get()
    course = cmbcrs.get()
    year = cmbyear.get()
    sem = cmbsem.get()
    dob = dtDob.get_date()
    mob_no = txtmob.get()
    age = txtage.get()
    gender = gen
    addr = str(Result.get("1.0",'end-1c'))
    if name.strip() and course.strip() != "-- SELECT COURSE --" and year.strip() != "-- SELECT YEAR --" and sem.strip() != "-- SELECT SEMESTER --" and dob and len(mob_no.strip()) == 10 and age.strip() and gender and addr.strip():
        gen1 = "F" if gender == "Female" else "M"
        sql = "INSERT INTO student(name, course, year, semester, dob, mobile_no, age, gender, address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, course, year, sem, dob, mob_no, age, gen1, addr)
        mycursor.execute(sql, values)
        db.commit()
        if mycursor.rowcount > 0:
            CTkMessagebox(frm, width=100, height=50, icon="check", icon_size=(20, 20), message="Student added successfully!")
        else:
            CTkMessagebox(frm, width=100, height=50, icon="cancel", icon_size=(20, 20), message="Student cannot be inserted!")
    else:
        CTkMessagebox(frm, width=100, height=50, icon="cancel", icon_size=(20, 20), message="Please enter valid values!")

def clear():
    txtnm.delete(0, END)
    cmbcrs.set("-- SELECT COURSE --")
    # cmbcrs.option_clear()
    cmbyear.set("-- SELECT YEAR --")
    # cmbyear['values'] = []
    cmbyear.configure(values=[])
    cmbsem.set("-- SELECT SEMESTER --")
    cmbsem.configure(values=[])
    dtDob.set_date(datetime.date.today())
    txtmob.delete(0, END)
    txtage.delete(0, END)
    
    Result.delete(1.0, END)

imgtemp = CTkImage(light_image=Image.open("mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

frm = CTkFrame(app, width=500, height=400, fg_color="transparent")
frm.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(frm, text="Enter Name", justify="left", anchor="w").grid(row=1, column=1, padx=(30, 12), pady=(30, 10), sticky="w")
txtnm = CTkEntry(frm, width=220)
txtnm.grid(row=1, column=2, pady=(30, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Select Course").grid(row=2, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
cmbcrs = CTkComboBox(frm, width=220, values=lst1, command=get_year)
cmbcrs.bind("<<ComboboxSelected>>", get_year)
cmbcrs.set('-- SELECT COURSE --')
# cmbcrs.bind('<Down>', lambda:all_courses)
# cmbcrs.configure(values=)
cmbcrs.grid(row=2, column=2, padx=(10, 20), pady=(0, 10), columnspan=2)

CTkLabel(frm, text="Select Year").grid(row=3, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
cmbyear = CTkComboBox(frm, width=220, command=get_sem)
cmbyear.set('-- SELECT YEAR --')
cmbyear.bind("<<ComboboxSelected>>", get_sem)
# cmbyear.bind("<<ComboboxSelected>>", get_year)
cmbyear.grid(row=3, column=2, padx=(10, 20), pady=(0, 10), columnspan=2)

CTkLabel(frm, text="Select Semester").grid(row=4, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
cmbsem = CTkComboBox(frm, width=220)
cmbsem.set('-- SELECT SEMESTER --')
cmbsem.grid(row=4, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

dt1 = datetime.date.today()
CTkLabel(frm, text="Date of Birth").grid(row=5, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
dtDob = DateEntry(frm, date_pattern="yyyy-mm-dd", cursor="hand2", width=33, background="blue", foreground="white", fieldbackground="black", maxdate=dt1)
dtDob.grid(row=5, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Enter Mobile Number").grid(row=6, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtmob = CTkEntry(frm, width=220)
txtmob.grid(row=6, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

# Age, Gender, Address
CTkLabel(frm, text="Enter Age").grid(row=7, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtage = CTkEntry(frm, width=220)
txtage.grid(row=7, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Select Gender").grid(row=8, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
rbMale = CTkRadioButton(frm, text="Male", value="Male", radiobutton_height=14, radiobutton_width=14, border_width_checked=3, variable=gen, border_width_unchecked=2)
rbMale.grid(row=8, column=2, pady=(0, 10))

rbFemale = CTkRadioButton(frm, text="Female", value="Female", radiobutton_height=14, border_width_checked=3, radiobutton_width=14, variable=gen, border_width_unchecked=2)
rbFemale.grid(row=8, column=3, pady=(0, 10))

CTkLabel(frm, text="Enter Address").grid(row=9, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
# txtAddr = CTkTextbox(frm, height=10)
# txtAddr.grid(row=8, column=2, pady=(0, 10), sticky="nsew")
# scrollBar = CTkScrollbar(frm, command=txtAddr.yview)
# scrollBar.grid(row=8, column=3, sticky="ns")
# txtAddr.configure(yscrollcommand=scrollBar.set)

# scrollBar = tkinter.Scrollbar(frm, orient="vertical")
# scrollBar.grid(row=8, column=2)
# txtAddr = tkinter.Text(frm, yscrollcommand=scrollBar.set, height=5, width=20)
# scrollBar.config(command=txtAddr.yview)
# txtAddr.grid(row=8, column=1)

# txt = tkinter.Text(frm, width=20, height=8)
# txt.grid(row=8, column=2, sticky="nsew", pady=(0, 30))

# create a Scrollbar and associate it with txt
# scrollb = tkinter.Scrollbar(frm, command=txt.yview, height=50)
# scrollb.grid(row=8, column=2, padx=(240, 0))
# txt['yscrollcommand'] = scrollb.set

# Result = tkinter.Text(frm,height=3,width=27)
# Result.place(x=208, y=340)

# Scroll = tkinter.Scrollbar(frm,command=Result.yview)
# Scroll.grid(row=9,column=3,padx=12,sticky='NS')
# Result.config(yscrollcommand=Scroll.set)

text_frame = CTkFrame(frm, width=220, height=100, fg_color="transparent")
text_frame.grid(row=9, column=2, pady=(0, 10), sticky="nsew", padx=10, columnspan=2)

# Add the Text widget
Result = tkinter.Text(text_frame, height=5, width=0, wrap="word", bd=0, relief="flat")
Result.pack(side="left", fill="both", expand=True)
# Result.place(x=0,y=0, anchor="nw", relwidth=0.5, relheight=1.0, padx=(0, 10))

# Add the scrollbar inside the same frame
Scroll = tkinter.Scrollbar(text_frame, command=Result.yview)
Scroll.pack(side="right", fill="y", padx=(0, 15))
Result.config(yscrollcommand=Scroll.set)  # Linking Text widget with Scrollbar

CTkButton(frm, text="Insert", width=210, command=insert).grid(row=10, column=1, padx=(30, 6), pady=(30, 20))
CTkButton(frm, text="Clear", width=210, fg_color="red", hover_color="#a30202", command=clear).grid(row=10, column=2, padx=6, pady=(30, 20), columnspan=2)

app.mainloop()
