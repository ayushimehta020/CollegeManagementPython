# https://stackoverflow.com/questions/29898780/how-to-see-if-date-is-in-current-month-sql-server

from customtkinter import *
from PIL import Image
from tkcalendar import DateEntry
import datetime
import mysql.connector
from CTkMessagebox import CTkMessagebox
import os

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state("zoomed"))
app.title("College")

db = mysql.connector.connect(host="localhost", user="root", password="", database="college_mgt")
mycursor = db.cursor()
course = StringVar()

username = "Guest"

if os.path.exists("session.txt"):
    with open("session.txt", "r") as file:
        username = file.read().strip()

def load_attendance(event):
    if course.get() != "-- SELECT MONTH --":
        id = ""

        sql = "SELECT stud_id FROM student WHERE mobile_no=%s"
        values = (username,)
        mycursor.execute(sql, values)
        res = mycursor.fetchone()
        id = res[0]

        sql = "SELECT date, status FROM stud_attendance WHERE student_id=%s AND MONTHNAME(%s)"
        values = (id, course.get())
        mycursor.execute(sql, values)
        res = mycursor.fetchall()
        
        for widget in table_frame.winfo_children():
            if isinstance(widget, CTkFrame) and widget != header_frame:
                widget.destroy()

        # for i in range(1, len(res) + 1):
        #     table.
        #     table.delete_row(i)

        for i in range(len(res)):
            date, status = res[i]

            # Create a frame for each row
            row_frame = CTkFrame(table_frame)
            row_frame.pack(side="top", fill="x")

            # Add labels for name, date, and reason
            CTkLabel(row_frame, text=date, width=100).pack(pady=10, side="left")
            CTkLabel(row_frame, text=status, width=150).pack(pady=10, side="left")
    else:
        return

imgtemp = CTkImage(light_image=Image.open("Images/mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

frm = CTkFrame(app, width=460, height=500, fg_color="transparent")
frm.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(frm, text="Please select course").place(x=20, rely=0.05)
cmbCourse = CTkComboBox(frm, width=270, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"], command=load_attendance, variable=course)
cmbCourse.set("-- SELECT MONTH --")
cmbCourse.place(x=170, rely=0.05)

table_frame = CTkFrame(frm)
table_frame.place(relx=0.5, y=0.3, anchor="center")

# Create headers
header_frame = CTkFrame(table_frame)
header_frame.pack(side="top", fill="x")

CTkLabel(header_frame, text="Date", width=100, font=(CTkFont, 13, "bold")).pack(pady=5, side="left")
CTkLabel(header_frame, text="Status", width=150, font=(CTkFont, 13, "bold")).pack(pady=5, side="left")

# load_stud()

# print(y_position)
# print(attendance_data)
# CTkButton(frm, text="Mark Attendance", command=mark_attendance, width=200).place(x=20, y=y_position + 20)
# CTkButton(frm, text="Update Attendance", command=update_attendance, width=200).place(x=240, y=y_position + 20)

app.mainloop()