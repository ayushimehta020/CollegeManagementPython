from customtkinter import *
from PIL import Image
from tkcalendar import DateEntry

app = CTk()
# app.grid_columnconfigure(0, weight=1)
# app.after(0, lambda:app.state('zoomed'))
app.attributes('-zoomed', True)
app.title("College")

gen = StringVar()

def insert():
    name = txtnm.get()
    dob = dtDob.get_date()
    age = txtage.get()
    gender = gen
    email = txtemail.get()
    mobile = txtmob.get()
    exp = txtexp.get()

    salary = txtsal.get()
    join_date = dtJoin.get_date()
    qual = txtqual.get()

def clear():
    pass

imgtemp = CTkImage(light_image=Image.open("mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

frm = CTkFrame(app, width=500, height=400, fg_color="transparent")
frm.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(frm, text="Enter Name", justify="left", anchor="w").grid(row=1, column=1, padx=(30, 12), pady=(30, 10), sticky="w")
txtnm = CTkEntry(frm, width=220)
txtnm.grid(row=1, column=2, pady=(30, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Date of Birth").grid(row=2, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
dtDob = DateEntry(frm, date_pattern="yyyy-mm-dd", cursor="hand2", width=33, background="blue", foreground="white", fieldbackground="black")
dtDob.grid(row=2, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Enter Age").grid(row=3, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtage = CTkEntry(frm, width=220)
txtage.grid(row=3, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Select Gender").grid(row=4, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
rbMale = CTkRadioButton(frm, text="Male", value="Male", radiobutton_height=14, radiobutton_width=14, border_width_checked=3, variable=gen, border_width_unchecked=2)
rbMale.grid(row=4, column=2, pady=(0, 10))

rbFemale = CTkRadioButton(frm, text="Female", value="Female", radiobutton_height=14, border_width_checked=3, radiobutton_width=14, variable=gen, border_width_unchecked=2)
rbFemale.grid(row=4, column=3, pady=(0, 10))

CTkLabel(frm, text="Enter Email").grid(row=5, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtemail = CTkEntry(frm, width=220)
txtemail.grid(row=5, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Enter Mobile Number").grid(row=6, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtmob = CTkEntry(frm, width=220)
txtmob.grid(row=6, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Enter Experience").grid(row=7, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtexp = CTkEntry(frm, width=220)
txtexp.grid(row=7, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Enter Experience").grid(row=7, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtexp = CTkEntry(frm, width=220)
txtexp.grid(row=7, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Select Department").grid(row=8, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
chkVal1 = CTkCheckBox(frm, checkbox_width=20, checkbox_height=20, text="IT")
chkVal1.grid(row=8, column=2, pady=(0, 10), padx=(10, 20))
chkVal2 = CTkCheckBox(frm, checkbox_width=20, checkbox_height=20, text="Commerce")
chkVal2.grid(row=9, column=2, pady=(0, 10), padx=(10, 20))
chkVal3 = CTkCheckBox(frm, checkbox_width=20, checkbox_height=20, text="Management")
chkVal3.grid(row=10, column=2, pady=(0, 10), padx=(10, 20))
chkVal4 = CTkCheckBox(frm, checkbox_width=20, checkbox_height=20, text="Other")
chkVal4.grid(row=11, column=2, pady=(0, 10), padx=(10, 20))

CTkLabel(frm, text="Enter Salary").grid(row=12, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtsal = CTkEntry(frm, width=220)
txtsal.grid(row=12, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Joining Date").grid(row=13, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
dtJoin = DateEntry(frm, date_pattern="yyyy-mm-dd", cursor="hand2", width=33, background="blue", foreground="white", fieldbackground="black")
dtJoin.grid(row=13, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkLabel(frm, text="Enter Qualification").grid(row=14, column=1, padx=(30, 12), pady=(0, 10), sticky="w")
txtqual = CTkEntry(frm, width=220)
txtqual.grid(row=14, column=2, pady=(0, 10), padx=(10, 20), columnspan=2)

CTkButton(frm, text="Insert", width=210, command=insert).grid(row=15, column=1, padx=(30, 6), pady=(30, 20))
CTkButton(frm, text="Clear", width=210, fg_color="red", hover_color="#a30202", command=clear).grid(row=15, column=2, padx=6, pady=(30, 20), columnspan=2)

app.mainloop()