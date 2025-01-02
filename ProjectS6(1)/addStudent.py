from customtkinter import *
from PIL import Image
from tkcalendar import DateEntry
from tkinter import ttk

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

imgtemp = CTkImage(light_image=Image.open("mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

frm = CTkFrame(app, width=500, height=400, fg_color="transparent")
frm.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(frm, text="Enter Name").grid(row=1, column=1, padx=12, pady=(30, 10))
txtnm = CTkEntry(frm)
txtnm.grid(row=1, column=2, pady=(30, 10), padx=10)

CTkLabel(frm, text="Select Course").grid(row=2, column=1, padx=12, pady=(0, 10))
cmbcrs = CTkComboBox(frm)
cmbcrs.grid(row=2, column=2, padx=10, pady=(0, 10))

CTkLabel(frm, text="Select Year").grid(row=3, column=1, padx=12, pady=(0, 10))
cmbyear = CTkComboBox(frm)
cmbyear.grid(row=3, column=2, padx=10, pady=(0, 10))

CTkLabel(frm, text="Select Semester").grid(row=3, column=1, padx=12, pady=(0, 10))
cmbsem = CTkComboBox(frm)
cmbsem.grid(row=3, column=2, pady=(0, 10), padx=10)

CTkLabel(frm, text="Date of Birth").grid(row=4, column=1, padx=12, pady=(0, 10))
dtDob = DateEntry(frm, date_pattern="yyyy-mm-dd", cursor="hand2", width=20, background="blue", foreground="white", fieldbackground="black")
dtDob.grid(row=4, column=2, pady=(0, 10), padx=10)

# CTkLabel(frm, text="Enter Name").grid(row=1, column=1, padx=12, pady=(30, 15))
# txtnm = CTkEntry(frm)
# txtnm.grid(row=1, column=2, pady=(30, 15), padx=10)

app.mainloop()