from customtkinter import *
import subprocess

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

def home():
    app.destroy()
    subprocess.run([sys.executable, "home.py"])

CTkButton(app, text="Back", command=home).pack()

app.mainloop()