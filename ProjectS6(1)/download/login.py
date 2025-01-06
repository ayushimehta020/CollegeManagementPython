import customtkinter as ctk
from tkinter import StringVar, messagebox
from customtkinter import CTkImage
from PIL import Image
import mysql.connector
import subprocess

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.title("Login Page")
        self.attributes("-fullscreen", True)  # Open in fullscreen mode by default
        self.bind("<Escape>", lambda e: self.toggle_fullscreen())  # Toggle fullscreen with ESC

        # Backgriund image
        self.background_image = Image.open("background1.jpg")
        self.bg_image = CTkImage(light_image=self.background_image, 
                         size=(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relx=0.5, rely=0.5, anchor="center")


        # Center Frame
        self.center_frame = ctk.CTkFrame(self, width=400, height=300, corner_radius=15 , fg_color="transparent")
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center" )

        # Title
        title_label = ctk.CTkLabel(self.center_frame, text="Login", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Username Field
        username_label = ctk.CTkLabel(self.center_frame, text="Username:", font=("Arial", 14))
        username_label.grid(row=1, column=0, pady=10, padx=20, sticky="e")
        self.username_entry = ctk.CTkEntry(self.center_frame, width=250)
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)

        # Password Field
        password_label = ctk.CTkLabel(self.center_frame, text="Password:", font=("Arial", 14))
        password_label.grid(row=2, column=0, pady=10, padx=20, sticky="e")
        self.password_entry = ctk.CTkEntry(self.center_frame, show="*", width=250)
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)

        # Error Message
        self.error_message = StringVar()
        self.error_label = ctk.CTkLabel(self.center_frame, textvariable=self.error_message, text_color="red", font=("Arial", 12))
        self.error_label.grid(row=3, column=0, columnspan=2, pady=(5, 10))

        # Login Button
        login_button = ctk.CTkButton(self.center_frame, text="Login", command=self.validate_login, width=200, height=40, font=("Arial", 14))
        login_button.grid(row=4, column=0, columnspan=2, pady=(10, 20))

        # Add custom title bar buttons (Close, Minimize, Maximize)
        self.create_custom_titlebar_buttons()

    def create_custom_titlebar_buttons(self):
        """Create custom close, minimize, and maximize buttons."""
        # Close button
        self.close_button = ctk.CTkButton(self, text="X", width=30, height=30, command=self.close_window, fg_color="red", font=("Arial", 12, "bold"))
        self.close_button.place(x=self.winfo_screenwidth() - 40, y=10)

        # Minimize button
        self.minimize_button = ctk.CTkButton(self, text="_", width=30, height=30, command=self.minimize_window, fg_color="gray", font=("Arial", 12, "bold"))
        self.minimize_button.place(x=self.winfo_screenwidth() - 120, y=10)

        # Maximize button
        self.maximize_button = ctk.CTkButton(self, text="□", width=30, height=30, command=self.maximize_window, fg_color="gray", font=("Arial", 12, "bold"))
        self.maximize_button.place(x=self.winfo_screenwidth() - 80, y=10)

    def close_window(self):
        """Close the window."""
        self.destroy()

    def minimize_window(self):
        """Minimize the window."""
        self.iconify()

    def maximize_window(self):
        """Maximize the window."""
        if self.state() == 'normal':  # If the window is normal, maximize it
            self.state('zoomed')  # Maximize window (this works in Tkinter)
        else:  # If it's zoomed, restore to normal state
            self.state('normal')

    def toggle_fullscreen(self):
        """Toggle fullscreen mode on ESC key press."""
        current_state = self.attributes("-fullscreen")
        self.attributes("-fullscreen", not current_state)

    def connect_to_database(self):
        """Connect to the database and return the connection object."""
        try:
            connection = mysql.connector.connect(
                host="localhost",  # Change to your host
                user="root",       # Change to your MySQL username
                password="",       # Change to your MySQL password
                database="employee"  # Change to your database name
            )
            return connection
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
            return None

    def validate_login(self):
        """Validate username and password by checking the database."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.error_message.set("Please enter both username and password.")
            return

        # Connect to the database
        db_connection = self.connect_to_database()
        if db_connection is None:
            return

        # Prepare and execute the SQL query to select the user
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM `login` WHERE unm=%s and pwd=%s", (username,password))
        user = cursor.fetchone()

        if user and user[2] == password:  # Check if password matches
            self.error_message.set("")
            self.redirect_to_home()  # Redirect to home page
        else:
            self.error_message.set("Invalid username or password. Please try again.")

        # Close database connection
        cursor.close()
        db_connection.close()

    def redirect_to_home(self):
        """Redirect to the home page."""
        self.destroy()  # Close the current login window
        subprocess.run(["python", "home.py"])  # Run the home.py script


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
