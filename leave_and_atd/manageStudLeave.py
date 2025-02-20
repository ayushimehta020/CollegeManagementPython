from customtkinter import *
from PIL import Image
import subprocess
import mysql.connector
import datetime
from CTkTable import *
from CTkMessagebox import CTkMessagebox

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state("zoomed"))
app.title("College")

username = "Guest"

if os.path.exists("session.txt"):
    with open("session.txt", "r") as file:
        username = file.read().strip()

db = mysql.connector.connect(host="localhost", user="root", password="", database="college_mgt")
mycursor = db.cursor()

names = []
date1 = datetime.date.today()
mob = ""

# btn1 = CTkButton(text="Approve").pack()

def load():
    global names
    global mob
    sql = "SELECT mobile_no FROM stud_leave WHERE status='Pending'"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    # mob = res[0][0]
    # print(res)
    # print(mob)

    for x in res:
        sql = "SELECT name FROM student WHERE mobile_no=%s"
        values = (x[0],)
        mycursor.execute(sql, values)
        res1 = mycursor.fetchall()

        for x in res1:
            names.append(x[0])

def load_leaves():
    sql = "SELECT mobile_no, start_date, end_date, reason FROM stud_leave WHERE status='Pending'"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    
    for widget in table_frame.winfo_children():
        if isinstance(widget, CTkFrame) and widget != header_frame:
            widget.destroy()

    # for i in range(1, len(res) + 1):
    #     table.
    #     table.delete_row(i)

    for i in range(len(res)):
        mobile, start_date, end_date, reason = res[i]
        name = names[i] if i < len(names) else "Unknown"  # Ensure we have a name

        # Create a frame for each row
        row_frame = CTkFrame(table_frame)
        row_frame.pack(side="top", fill="x")

        # Add labels for name, date, and reason
        CTkLabel(row_frame, text=name, width=100).pack(pady=10, side="left")
        CTkLabel(row_frame, text=f"{start_date} - {end_date}", width=150).pack(pady=10, side="left")
        CTkLabel(row_frame, text=reason, width=200).pack(pady=10, side="left")

        # Create Approve button
        approve_button = CTkButton(row_frame, text="Approve", command=lambda frame=row_frame, mob=mobile, startDt=start_date, endDt=end_date: approveLeave(frame=frame, mob=mob, startDt=startDt, endDt=endDt), fg_color="#3fb05b", hover_color="#2e8544")
        approve_button.pack(side="left", padx=5)

        # Create Reject button
        reject_button = CTkButton(row_frame, text="Reject", command=lambda frame=row_frame, mob=mobile, startDt=start_date, endDt=end_date: rejectLeave(frame, mob=mob, startDt=startDt, endDt=endDt), fg_color="#fa5050", hover_color="#a30202")
        reject_button.pack(side="left", padx=5)

def approveLeave(frame, mob, startDt, endDt):
    mobile = mob
    startDate = startDt
    endDate = endDt
    id = ""

    sql = "SELECT stud_id FROM student WHERE mobile_no=%s"
    values=(mobile,)
    mycursor.execute(sql, values)
    res = mycursor.fetchone()

    if res:
        id = res[0]
        # days = endDate.day - startDate.day + 1
        dates = []

        current_date = startDate
        while current_date <= endDate:
            dates.append(current_date)
            current_date += datetime.timedelta(days=1)

    sql = "UPDATE stud_leave SET status=%s WHERE mobile_no=%s AND start_date=%s AND end_date=%s"
    values = ("Approved", mobile, startDate, endDate)
    mycursor.execute(sql, values)
    db.commit()

    if len(res) > 0:
        CTkMessagebox(table_frame, width=100, height=50, icon="check", icon_size=(20, 20), message="Leave Approved!")

        for date in dates:
            sql = "SELECT status FROM stud_attendance WHERE student_id=%s AND date=%s"
            values=(id, date)
            mycursor.execute(sql, values)
            res = mycursor.fetchone()

            if res:
                sql = "UPDATE stud_attendance SET status=%s, date=%s WHERE student_id=%s"
                values = ("Leave", date, id)
                mycursor.execute(sql, values)
                db.commit()
            else:
                sql = "INSERT INTO stud_attendance(student_id, date, status) VALUES(%s, %s, %s)"
                values = (id, date, "Leave")
                mycursor.execute(sql, values)
                db.commit()

                if mycursor.rowcount > 0:
                    CTkMessagebox(app, message="Done!")

    frame.destroy()

def rejectLeave(frame, mob, startDt, endDt):
    mobile = mob
    startDate = startDt
    endDate = endDt
    
    sql = "UPDATE stud_leave SET status=%s WHERE mobile_no=%s and start_date=%s AND end_date=%s"
    values=("Rejected", mobile, startDate, endDate)
    mycursor.execute(sql, values)
    db.commit()

    if mycursor.rowcount > 0:
        CTkMessagebox(table_frame, width=100, height=50, icon="check", icon_size=(20, 20), message="Leave Rejected!")
        print(res)

    frame.destroy()

# def changeTo(event):
#     from_date = dtFrom.get_date()
#     dtTo.configure(mindate=from_date)

imgtemp = CTkImage(light_image=Image.open("Images/mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

if username == "" or username == "Guest":
    app.destroy()
    subprocess.run([sys.executable, "login.py"])
else:
    sql = "SELECT role FROM admin WHERE username=%s"
    values = (username,)
    mycursor.execute(sql, values)
    res = mycursor.fetchone()

    if res[0] == "faculty":
        # CTkLabel(frm, text="No. of Days", justify="left", anchor="w").grid(row=1, column=1, padx=(30, 12), pady=(30, 10), sticky="w")
        # txtDays = CTkEntry(frm, width=220)
        # txtDays.grid(row=1, column=2, pady=(30, 10), padx=(10, 20))

        table_frame = CTkFrame(app)
        table_frame.place(relx=0.5, y=200, anchor="center")

        # Create headers
        header_frame = CTkFrame(table_frame)
        header_frame.pack(side="top", fill="x")

        CTkLabel(header_frame, text="Name", width=100, font=(CTkFont, 13, "bold")).pack(pady=5, side="left")
        CTkLabel(header_frame, text="Date", width=150, font=(CTkFont, 13, "bold")).pack(pady=5, side="left")
        CTkLabel(header_frame, text="Reason", width=200, font=(CTkFont, 13, "bold")).pack(pady=5, side="left")
        CTkLabel(header_frame, text="Actions", width=300, font=(CTkFont, 13, "bold")).pack(pady=5, side="left")

        # help(ttk.Treeview)
        # ttk.Treeview.heading(table, "#0", ["Name", "Date", "Reason", "Action"])

        # table = CTkTable(app, column=4, row=1, font=("Consolas", 15))
        # table.place(relx=0.5, y=200, anchor="center")

        # table.insert(0, 0, "Name")
        # table.insert(0, 1, "Date")
        # table.insert(0, 2, "Reason")
        # table.insert(0, 3, "Actions")

        load()
        load_leaves()

        app.mainloop()
    else:
        app.destroy()
        subprocess.run([sys.executable, "login.py"])
