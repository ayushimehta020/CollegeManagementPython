from customtkinter import *
from PIL import ImageTk, Image
import subprocess
import mysql.connector
from CTkMessagebox import CTkMessagebox

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

# username = "admin"
imgTemp = CTkImage(light_image=Image.open("back2.jpg"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
# img2 = imgTemp.resize((app.winfo_screenwidth(), app.winfo_screenheight()))
# img = ImageTk.PhotoImage(imgTemp, size=(app.winfo_screenwidth(), app.winfo_screenheight()))
img_label = CTkLabel(app, image=imgTemp, text='')
img_label.place(relx=0.5, rely=0.5, anchor="center")

# if username == "admin":
#     app.destroy()
#     # import login
#     # login.deiconify()
#     subprocess.run([sys.executable, "login.py"])

db = mysql.connector.connect(host="localhost", user="root", password="", database="college_mgt")
mycursor = db.cursor()

def login():
    unm = txtunm.get()
    pwd = txtpwd.get()
    sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
    values=(unm, pwd)
    mycursor.execute(sql, values)
    res = mycursor.fetchall()
    if unm == "admin" and pwd == "1234":
        app.destroy()
        # import login
        # login.deiconify()
        subprocess.run([sys.executable, "home.py"])
    else:
        CTkMessagebox(frm2, width=200, height=100, title="College", message="Invalid Username or Password!", icon="cancel", icon_size=(30, 30))

# frm1 = CTkFrame(app)
# frm1.pack(expand=True)

frm2 = CTkFrame(app, width=500, height=400, fg_color="transparent")
frm2.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(frm2, text="Login", font=("Ubuntu", 30)).grid(row=0, column=0, columnspan=4, pady=(40, 0))

CTkLabel(frm2, text="Enter Username").grid(row=1, column=1, padx=12, pady=(30, 15))
txtunm = CTkEntry(frm2)
txtunm.grid(row=1, column=2, pady=(30, 15))

CTkLabel(frm2, text="Enter Password").grid(row=2, column=1, padx=12, pady=(0, 10))
txtpwd = CTkEntry(frm2)
txtpwd.grid(row=2, column=2, pady=(0, 10))

CTkButton(frm2, text="Login", command=login, width=260).grid(row=3, column=1, columnspan=3, pady=(20, 30), padx=15)

# CTkLabel(frm2, text="Invalid Username or Password!").grid(row=2, column=1, padx=12, pady=(0, 10))

app.mainloop()