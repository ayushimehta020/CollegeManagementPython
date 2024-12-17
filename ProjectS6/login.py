import subprocess
import sys
from customtkinter import *
from CTkMessagebox import CTkMessagebox

root = CTk()
root.geometry("500x500")

def login():
    unm = txtunm.get()
    pwd = txtpwd.get()

    if (unm == "admin" and pwd == "test"):
        # root.destroy()
        # CTk.quit(root)
        # root.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
        # exit()
        root.destroy()
        # sys.exit()
        # import home
        subprocess.run([sys.executable, "home.py"])
    else:
        CTkMessagebox(root, title="Project", message="Invalid!")

CTkLabel(root, text="Enter Username").pack()
txtunm = CTkEntry(root)
txtunm.pack()

CTkLabel(root, text="Enter Password").pack()
txtpwd = CTkEntry(root)
txtpwd.pack()

CTkButton(root, text="Login", command=login).pack()

root.mainloop()