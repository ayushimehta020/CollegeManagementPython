from tkinter import ttk  # Import ttk for Treeview
from customtkinter import *
from PIL import Image
import subprocess
import mysql.connector
from tkcalendar import DateEntry
import datetime
from CTkMessagebox import CTkMessagebox

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda: app.state("zoomed"))
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

def load():
    global names
    global mob
    sql = "SELECT mobile_no FROM stud_leave"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    mob = res[0][0]

    for x in res:
        sql = "SELECT name FROM student WHERE mobile_no=%s"
        values = (x[0],)
        mycursor.execute(sql, values)
        res1 = mycursor.fetchall()

        for x in res1:
            names.append(x[0])

# Create a Treeview widget
tree = ttk.Treeview(app, columns=("Name", "Date", "Reason"), show="headings", height=10)
tree.heading("Name", text="Name")
tree.heading("Date", text="Date")
tree.heading("Reason", text="Reason")
tree.pack(pady=20)

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(app, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

def load_leaves():
    sql = "SELECT start_date, end_date, reason FROM stud_leave"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    
    # Clear existing rows in the treeview
    for item in tree.get_children():
        tree.delete(item)

    # Add new rows with Approve and Reject buttons
    for i in range(len(res)):
        start_date, end_date, reason = res[i]
        name = names[i] if i < len(names) else "Unknown"  # Ensure we have a name

        # Insert the row into the treeview
        tree.insert("", "end", values=(name, f"{start_date} - {end_date}", reason))

        # Create a frame for buttons
        button_frame = CTkFrame(app)
        button_frame.pack(pady=5)

        # Create Approve button
        approve_button = CTkButton(button_frame, text="Approve", command=lambda name=name: approve_leave(name))
        approve_button.pack(side="left", padx=5)

        # Create Reject button
        reject_button = CTkButton(button_frame, text="Reject", command=lambda name=name: reject_leave(name))
        reject_button.pack(side="left", padx=5)

def approve_leave(name):
    # Logic to approve the leave for the student with the given name
    CTkMessagebox.showinfo("Leave Approved", f"Leave for {name} has been approved.")

def reject_leave(name):
    # Logic to reject the leave for the student with the given name
    CTkMessagebox.showinfo("Leave Rejected", f"Leave for {name} has been rejected.")

# Load data and leaves
load()
load_leaves()

app.mainloop()







# Create a frame to hold the table
table_frame = CTkFrame(app)
table_frame.place(relx=0.5, y=200, anchor="center")

# Create headers
header_frame = CTkFrame(table_frame)
header_frame.pack(side="top", fill="x")

CTkLabel(header_frame, text="Name", width=20).pack(side="left")
CTkLabel(header_frame, text="Date", width=100).pack(side="left")
CTkLabel(header_frame, text="Reason", width=200).pack(side="left")
CTkLabel(header_frame, text="Actions", width=100).pack(side="left")

def load_leaves():
    sql = "SELECT start_date, end_date, reason FROM stud_leave"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    
    # Clear existing rows in the table frame
    for widget in table_frame.winfo_children():
        if isinstance(widget, CTkFrame) and widget != header_frame:
            widget.destroy()

    # Add new rows with Approve and Reject buttons
    for i in range(len(res)):
        start_date, end_date, reason = res[i]
        name = names[i] if i < len(names) else "Unknown"  # Ensure we have a name

        # Create a frame for each row
        row_frame = CTkFrame(table_frame)
        row_frame.pack(side="top", fill="x")

        # Add labels for name, date, and reason
        CTkLabel(row_frame, text=name, width=20).pack(side="left")
        CTkLabel(row_frame, text=f"{start_date} - {end_date}", width=100).pack(side="left")
        CTkLabel(row_frame, text=reason, width=200).pack(side="left")

        # Create Approve button
        approve_button = CTkButton(row_frame, text="Approve", command=lambda name=name: approve_leave(name))
        approve_button.pack(side="left", padx=5)

        # Create Reject button
        reject_button = CTkButton(row_frame, text="Reject", command=lambda name=name: reject_leave(name))
        reject_button.pack(side="left", padx=5)

def approve_leave(name):
    # Logic to approve the leave for the student with the given name
    CTkMessagebox.showinfo("Leave Approved", f"Leave for {name} has been approved.")

def reject_leave(name):
    # Logic to reject the leave for the student with the given name
    CTkMessagebox.showinfo("Leave Rejected", f"Leave for {name} has been rejected.")
