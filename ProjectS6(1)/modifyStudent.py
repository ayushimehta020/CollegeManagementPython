from customtkinter import *
from PIL import Image

app = CTk()
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

imgtemp = CTkImage(light_image=Image.open("mainback1.png"), size=(app.winfo_screenwidth(), app.winfo_screenheight()))
imgLabel = CTkLabel(app, image=imgtemp, text='')
imgLabel.place(relx=0.5, rely=0.5, anchor="center")

CTkLabel(app, text="Modify Student").pack()

app.mainloop()