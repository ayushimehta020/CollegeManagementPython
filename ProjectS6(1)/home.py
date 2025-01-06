from customtkinter import *
from PIL import Image
import subprocess

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

imgtemp = CTkImage(light_image=Image.open("homeback1.jpg"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

def addStudent():
    # app.deiconify()
    # import addstudent
    # CTkToplevel(addstudent)
    app.withdraw()
    subprocess.run([sys.executable, "addStudent.py"])
    app.deiconify()
    app.after(0, lambda:app.state('zoomed'))

def modifyStudent():
    app.withdraw()
    subprocess.run([sys.executable, "modifyStudent.py"])
    app.deiconify()
    app.after(0, lambda:app.state('zoomed'))

def addFaculty():
    app.withdraw()
    subprocess.run([sys.executable, "addFaculty.py"])
    app.deiconify()
    app.after(0, lambda:app.state('zoomed'))

def modifyFaculty():
    app.withdraw()
    subprocess.run([sys.executable, "modifyFaculty.py"])
    app.deiconify()
    app.after(0, lambda:app.state('zoomed'))

def addCourse():
    app.withdraw()
    subprocess.run([sys.executable, "addCourse.py"])
    app.deiconify()
    app.after(0, lambda:app.state('zoomed'))

def modifyCourse():
    app.withdraw()
    subprocess.run([sys.executable, "modifyCourse.py"])
    app.deiconify()
    app.after(0, lambda:app.state('zoomed'))

CTkButton(app, text="Add Student", width=350, height=50, font=("Consolas", 20), command=addStudent).place(relx=0.5, rely=0.2, anchor="center")
CTkButton(app, text="Modify Student", width=350, height=50, font=("Consolas", 20), command=modifyStudent).place(relx=0.5, rely=0.3, anchor="center")
CTkButton(app, text="Add Faculty", width=350, height=50, font=("Consolas", 20), command=addFaculty).place(relx=0.5, rely=0.4, anchor="center")
CTkButton(app, text="Modify Faculty", width=350, height=50, font=("Consolas", 20), command=modifyFaculty).place(relx=0.5, rely=0.5, anchor="center")
CTkButton(app, text="Add Course", width=350, height=50, font=("Consolas", 20), command=addCourse).place(relx=0.5, rely=0.6, anchor="center")
CTkButton(app, text="Modify Course", width=350, height=50, font=("Consolas", 20), command=modifyCourse).place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()