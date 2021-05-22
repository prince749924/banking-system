import os  # for creating directories Admin/Customer if it is not exists.
from datetime import date  # for date of account creation when new customer account is created.
import tkinter as tk
from tkinter import *


# Tkinter GUI starts:
root = tk.Tk()

class welcomeScreen:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1100x750")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("NIC ASIA BANK LIMITED")
        p1 = PhotoImage(file='images/nic-logo.PNG')
        window.iconphoto(True, p1)
        window.configure(background="#cf0000")
        window.configure(cursor="arrow")

        self.Canvas1 = tk.Canvas(window, background="#ffffff", borderwidth="0", insertbackground="black", relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.1, rely=0.1, relheight=0.751, relwidth=0.752)

        # load the .gif image file
        self.gif1 = PhotoImage(file='images/nic-login-form.PNG')
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.Canvas1.create_image(25, 0, image=self.gif1, anchor=NW)


        self.Button1 = tk.Button(self.Canvas1, command=self.selectEmployee, activebackground="#ececec",
                                 activeforeground="#000000", background="#cf0000", disabledforeground="#a3a3a3",
                                 foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''ADMIN''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.435, rely=0.583, height=50, width=100)


        self.Button2 = tk.Button(self.Canvas1, command=self.selectCustomer, activebackground="#ececec",
                                 activeforeground="#000000", background="#cf0000", disabledforeground="#a3a3a3",
                                 foreground="#f9f9f9", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",
                                 text='''CUSTOMER''')
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.place(relx=0.435, rely=0.730, height=50, width=100)


        self.Label1 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#e04728",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#000000",
                               text='''  Welcome to the system \n \n Please Select Your Role''')
        self.Label1.place(relx=0.345, rely=0.380, height=100, width=250)


    def selectEmployee(self):
        self.master.withdraw()
        #adminLogin(Toplevel(self.master))

    def selectCustomer(self):
        self.master.withdraw()
        #CustomerLogin(Toplevel(self.master))


top = welcomeScreen(root)
root.mainloop()
