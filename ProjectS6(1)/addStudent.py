from customtkinter import *
from PIL import Image
from tkcalendar import DateEntry
# import tkinter.ttk as ttk
# from tkinter import *
import tkinter

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

gen = StringVar()

imgtemp = CTkImage(light_image=Image.open("mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

frm = CTkFrame(app, width=500, height=400, fg_color="transparent")
frm.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(frm, text="Enter Name", justify="left", anchor="w").grid(row=1, column=1, padx=12, pady=(30, 10), sticky="w")
txtnm = CTkEntry(frm, width=220)
txtnm.grid(row=1, column=2, pady=(30, 10), columnspan=2)

CTkLabel(frm, text="Select Course").grid(row=2, column=1, padx=12, pady=(0, 10), sticky="w")
cmbcrs = CTkComboBox(frm, width=220)
cmbcrs.grid(row=2, column=2, padx=10, pady=(0, 10), columnspan=2)

CTkLabel(frm, text="Select Year").grid(row=3, column=1, padx=12, pady=(0, 10), sticky="w")
cmbyear = CTkComboBox(frm, width=220)
cmbyear.grid(row=3, column=2, padx=10, pady=(0, 10), columnspan=2)

CTkLabel(frm, text="Select Semester").grid(row=4, column=1, padx=12, pady=(0, 10), sticky="w")
cmbsem = CTkComboBox(frm, width=220)
cmbsem.grid(row=4, column=2, pady=(0, 10), padx=10, columnspan=2)

CTkLabel(frm, text="Date of Birth").grid(row=5, column=1, padx=12, pady=(0, 10), sticky="w")
dtDob = DateEntry(frm, date_pattern="yyyy-mm-dd", cursor="hand2", width=33, background="blue", foreground="white", fieldbackground="black")
dtDob.grid(row=5, column=2, pady=(0, 10), padx=10, columnspan=2)

CTkLabel(frm, text="Enter Mobile Number").grid(row=6, column=1, padx=12, pady=(0, 10), sticky="w")
txtnm = CTkEntry(frm, width=220)
txtnm.grid(row=6, column=2, pady=(0, 10), padx=10, columnspan=2)

# Age, Gender, Address
CTkLabel(frm, text="Enter Age").grid(row=7, column=1, padx=12, pady=(0, 10), sticky="w")
txtnm = CTkEntry(frm, width=220)
txtnm.grid(row=7, column=2, pady=(0, 10), padx=10, columnspan=2)

CTkLabel(frm, text="Select Gender").grid(row=8, column=1, padx=12, pady=(0, 10), sticky="w")
rbMale = CTkRadioButton(frm, text="Male", value="Male", radiobutton_height=14, radiobutton_width=14, border_width_checked=3, variable=gen, border_width_unchecked=2)
rbMale.grid(row=8, column=2, pady=(0, 10))

rbFemale = CTkRadioButton(frm, text="Female", value="Female", radiobutton_height=14, border_width_checked=3, radiobutton_width=14, variable=gen, border_width_unchecked=2)
rbFemale.grid(row=8, column=3, pady=(0, 10))

CTkLabel(frm, text="Enter Address").grid(row=9, column=1, padx=12, pady=(0, 10), sticky="w")
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

Result = tkinter.Text(frm,height=3,width=27)
Result.place(x=208, y=340)
 
Scroll = tkinter.Scrollbar(frm,command=Result.yview)
Scroll.grid(row=9,column=3,padx=12,sticky='NS')
Result.config(yscrollcommand=Scroll.set)

CTkButton(frm, text="Insert", width=180).grid(row=10, column=1, padx=(14, 6), pady=(30, 20))
CTkButton(frm, text="Clear", width=180, fg_color="red").grid(row=10, column=2, padx=6, pady=(30, 20))

app.mainloop()