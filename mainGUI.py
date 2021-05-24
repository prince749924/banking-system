# This project is developed by Prince Kumar Sah, Softwarica College, Coventry University UK

# Coventry ID:

# Section

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

        self.Canvas1 = tk.Canvas(window, background="#ffffff", borderwidth="0", insertbackground="black", relief="ridge", selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.1, rely=0.1, relheight=0.751, relwidth=0.752)

        # load the .gif image file
        self.gif1 = PhotoImage(file='images/nic-login-form.PNG')
        # put gif image on canvas pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.Canvas1.create_image(25, 0, image=self.gif1, anchor=NW)

        self.Button1 = tk.Button(self.Canvas1, command=self.selectEmployee, activebackground="#ececec", activeforeground="#000000", background="#cf0000", disabledforeground="#a3a3a3", foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0",text='''ADMIN''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.435, rely=0.583, height=50, width=100)

        self.Button2 = tk.Button(self.Canvas1, command=self.selectCustomer, activebackground="#ececec", activeforeground="#000000", background="#cf0000", disabledforeground="#a3a3a3", foreground="#f9f9f9", borderwidth="0", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0", text='''CUSTOMER''')
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.place(relx=0.435, rely=0.730, height=50, width=100)

        self.Label1 = tk.Label(self.Canvas1, background="#ffffff", disabledforeground="#e04728", font="-family {Segoe UI} -size 13 -weight bold", foreground="#000000", text='''  Welcome to the system \n \n Please Select Your Role by Clicking on the buttons below''')
        self.Label1.place(relx=0.075, rely=0.380, height=100, width=700)

    def selectEmployee(self):
        self.master.withdraw()
        adminLogin(Toplevel(self.master))

    def selectCustomer(self):
        self.master.withdraw()
        CustomerLogin(Toplevel(self.master))


# Error function
class Error:
    def __init__(self, window=None):
        global master
        master = window
        window.geometry("411x117+485+248")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Error")
        window.configure(background="#f2f3f4")

        global Label2

        self.Button1 = tk.Button(window, background="#d3d8dc", borderwidth="1", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9", foreground="#000000", highlightbackground="#d9d9d9",
                                 highlightcolor="black", pady="0", text='''OK''', command=self.goback)
        self.Button1.place(relx=0.779, rely=0.598, height=24, width=67)

        global _img0
        _img0 = tk.PhotoImage(file="./images/error_image.png")
        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000", image=_img0, text='''Label''')
        self.Label1.place(relx=0.024, rely=0.0, height=81, width=84)

    def setMessage(self, message_shown):
        Label2 = tk.Label(master, background="#f2f3f4", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 16", foreground="#000000", highlightcolor="#646464646464", text=message_shown)
        Label2.place(relx=0.210, rely=0.171, height=41, width=214)

    def goback(self):
        master.withdraw()


# Admin login function inside the system
class adminLogin:
    def __init__(self, window=None):
        self.master = window
        window.geometry("743x494+338+92")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Admin")
        window.configure(background="#cf0000")

        global Canvas1
        Canvas1 = tk.Canvas(window, background="#ffffff", insertbackground="black", relief="ridge", selectbackground="blue", selectforeground="white")
        Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)

        self.Label1 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 14 -weight bold", foreground="#000000", text="Admin Login")
        self.Label1.place(relx=0.135, rely=0.142, height=41, width=154)

        global Label2
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.067, rely=0.283, height=181, width=233)
        global _img0
        _img0 = tk.PhotoImage(file="./images/small-logo.PNG")
        Label2.configure(image=_img0)

        self.Entry1 = tk.Entry(Canvas1, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6", highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.607, rely=0.453, height=20, relwidth=0.26)

        self.Entry1_1 = tk.Entry(Canvas1, show='*', background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black",
                                 selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.607, rely=0.623, height=20, relwidth=0.26)

        self.Label3 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label3.place(relx=0.556, rely=0.453, height=21, width=34)
        global _img1
        _img1 = tk.PhotoImage(file="./images/user1.png")
        self.Label3.configure(image=_img1)

        self.Label4 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label4.place(relx=0.556, rely=0.623, height=21, width=34)
        global _img2
        _img2 = tk.PhotoImage(file="./images/lock1.png")
        self.Label4.configure(image=_img2)

        self.Label5 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label5.place(relx=0.670, rely=0.142, height=71, width=74)
        global _img3
        _img3 = tk.PhotoImage(file="./images/bank1.png")
        self.Label5.configure(image=_img3)

        self.Button = tk.Button(Canvas1, text="Login", borderwidth="0", width=10, background="#cf0000", foreground="#f9f9f9",
                                font="-family {Segoe UI} -size 10 -weight bold",
                                command=lambda: self.login(self.Entry1.get(), self.Entry1_1.get()))
        self.Button.place(relx=0.765, rely=0.755)

        self.Button_back = tk.Button(Canvas1, text="Back", borderwidth="0", width=10, background="#cf0000", foreground="#f9f9f9",
                                font="-family {Segoe UI} -size 10 -weight bold", command=self.back)
        self.Button_back.place(relx=0.545, rely=0.755)

        global admin_img
        admin_img = tk.PhotoImage(file="./images/small-logo.PNG")

    def back(self):
        self.master.withdraw()
        welcomeScreen(Toplevel(self.master))

    @staticmethod
    def setImg():
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.067, rely=0.283, height=181, width=233)
        Label2.configure(image=admin_img)

    def login(self, admin_id, admin_password):
        global admin_idNO
        admin_idNO = admin_id
        if check_credentials(admin_id, admin_password, 1, True):
            self.master.withdraw()
            adminMenu(Toplevel(self.master)) # Admin menu to access user
        else:
            Error(Toplevel(self.master))
            Error.setMessage(self, message_shown="Invalid Credentials!")
            self.setImg()

# Admin menu
class adminMenu:
    def __init__(self, window=None):
        self.master = window
        window.geometry("743x494+329+153")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Admin Menu")
        window.configure(background="#ffffff")

        self.Labelframe1 = tk.LabelFrame(window, relief='groove', borderwidth="8", font="-family {Segoe UI} -size 13 -weight bold", foreground="#000000", background="#fffffe")
        self.Labelframe1.place(relx=0.081, rely=0.081, relheight=0.415, relwidth=0.848)

        self.Button1 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000", background="#cf0000", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Close bank account", command=self.closeAccount)
        self.Button1.place(relx=0.667, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button2 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000", background="#cf0000", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Create bank account", command=self.createCustaccount)
        self.Button2.place(relx=0.04, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button3 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000", background="#cf0000", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Exit", command=self.exit)
        self.Button3.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button4 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000", background="#cf0000", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Create admin account", command=self.createAdmin)
        self.Button4.place(relx=0.04, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button5 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000", background="#cf0000", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Close admin account", command=self.deleteAdmin)
        self.Button5.place(relx=0.667, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button6 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000", background="#cf0000", foreground="#fffffe", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11 -weight bold", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Check account summary", command=self.showAccountSummary)
        self.Button6.place(relx=0.04, rely=0.683, height=34, width=181, bordermode='ignore')

        global Frame1
        Frame1 = tk.Frame(window, relief='groove', borderwidth="8", background="#fffffe")
        Frame1.place(relx=0.081, rely=0.547, relheight=0.415, relwidth=0.848)

    def closeAccount(self):
        CloseAccountByAdmin(Toplevel(self.master))

    def createCustaccount(self):
        createCustomerAccount(Toplevel(self.master))

    def createAdmin(self):
        createAdmin(Toplevel(self.master))

    def deleteAdmin(self):
        deleteAdmin(Toplevel(self.master))

    def showAccountSummary(self):
        checkAccountSummary(Toplevel(self.master))

    def printAccountSummary(identity):
        # clearing the frame
        for widget in Frame1.winfo_children():
            widget.destroy()
        # getting output_message and displaying it in the frame
        output = display_account_summary(identity, 1)
        output_message = Label(Frame1, text=output, background="#fffffe")
        output_message.pack(pady=20)

    def printMessage_outside(output):
        # clearing the frame
        for widget in Frame1.winfo_children():
            widget.destroy()
        # getting output_message and displaying it in the frame
        output_message = Label(Frame1, text=output, background="#fffffe")
        output_message.pack(pady=20)

    def exit(self):
        self.master.withdraw()
        adminLogin(Toplevel(self.master))


# Customer login inside the system
class CustomerLogin:
    def __init__(self, window=None):
        self.master = window
        window.geometry("743x494+338+92")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Customer")
        window.configure(background="#cf0000")

        global Canvas1
        Canvas1 = tk.Canvas(window, background="#ffffff", insertbackground="black", relief="ridge", selectbackground="blue", selectforeground="white")
        Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)

        Label1 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 14 -weight bold", foreground="#000000", text="Customer Login")
        Label1.place(relx=0.135, rely=0.142, height=41, width=154)

        global Label2
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.067, rely=0.283, height=181, width=233)
        global _img0
        _img0 = tk.PhotoImage(file="images/customer-logo.PNG")
        Label2.configure(image=_img0)

        self.Entry1 = tk.Entry(Canvas1, background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                               highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.607, rely=0.453, height=20, relwidth=0.26)

        self.Entry1_1 = tk.Entry(Canvas1, show='*', background="#e2e2e2", borderwidth="2", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.607, rely=0.623, height=20, relwidth=0.26)

        self.Label3 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label3.place(relx=0.556, rely=0.453, height=21, width=34)

        global _img1
        _img1 = tk.PhotoImage(file="./images/user1.png")
        self.Label3.configure(image=_img1)

        self.Label4 = tk.Label(Canvas1)
        self.Label4.place(relx=0.556, rely=0.623, height=21, width=34)
        global _img2
        _img2 = tk.PhotoImage(file="./images/lock1.png")
        self.Label4.configure(image=_img2, background="#ffffff")

        self.Label5 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label5.place(relx=0.670, rely=0.142, height=71, width=74)
        global _img3
        _img3 = tk.PhotoImage(file="./images/bank1.png")
        self.Label5.configure(image=_img3)

        self.Button = tk.Button(Canvas1, text="Login", borderwidth="0", width=10, background="#cf0000", foreground="#ffffff",
                                font="-family {Segoe UI} -size 10 -weight bold", command=lambda: self.login(self.Entry1.get(), self.Entry1_1.get()))
        self.Button.place(relx=0.765, rely=0.755)

        self.Button_back = tk.Button(Canvas1, text="Back", borderwidth="0", width=10, background="#cf0000", foreground="#ffffff",
                                     font="-family {Segoe UI} -size 10 -weight bold", command=self.back)
        self.Button_back.place(relx=0.545, rely=0.755)

        global customer_img
        customer_img = tk.PhotoImage(file="images/customer-logo.PNG")

    def back(self):
        self.master.withdraw()
        welcomeScreen(Toplevel(self.master))

    @staticmethod
    def setImg():
        settingIMG = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        settingIMG.place(relx=0.067, rely=0.283, height=181, width=233)
        settingIMG.configure(image=customer_img)

    def login(self, customer_account_number, customer_PIN):
        if check_credentials(customer_account_number, customer_PIN, 2, False):
            global customer_accNO
            customer_accNO = str(customer_account_number)
            self.master.withdraw()
            customerMenu(Toplevel(self.master))
        else:
            Error(Toplevel(self.master))
            Error.setMessage(self, message_shown="Invalid Credentials!")
            self.setImg()

# Customer Menu
class customerMenu:
    def __init__(self, window=None):
        self.master = window
        window.geometry("743x494+329+153")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Customer Menu")
        window.configure(background="#cf0000")

        self.Labelframe1 = tk.LabelFrame(window, relief='groove', font="-family {Segoe UI} -size 13 -weight bold", borderwidth="8",
                                         foreground="#000000", background="#fffffe")
        self.Labelframe1.place(relx=0.081, rely=0.081, relheight=0.415, relwidth=0.848)

        self.Button1 = tk.Button(self.Labelframe1, command=self.selectWithdraw, activebackground="#ececec",
                                 activeforeground="#000000", background="#cf0000", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Withdraw''')
        self.Button1.place(relx=0.667, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button2 = tk.Button(self.Labelframe1, command=self.selectDeposit, activebackground="#ececec",
                                 activeforeground="#000000", background="#cf0000", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Deposit''')
        self.Button2.place(relx=0.04, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button3 = tk.Button(self.Labelframe1, command=self.exit, activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#cf0000",
                                 borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11 -weight bold",
                                 foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text='''Exit''')
        self.Button3.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button4 = tk.Button(self.Labelframe1, command=self.selectChangePIN, activebackground="#ececec",
                                 activeforeground="#000000", background="#cf0000", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Change PIN''')
        self.Button4.place(relx=0.04, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button5 = tk.Button(self.Labelframe1, command=self.selectCloseAccount, activebackground="#ececec",
                                 activeforeground="#000000", background="#cf0000", borderwidth="0",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text='''Close account''')
        self.Button5.place(relx=0.667, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button6 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#cf0000", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11 -weight bold", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text='''Check your balance''', command=self.checkBalance)
        self.Button6.place(relx=0.04, rely=0.683, height=34, width=181, bordermode='ignore')

        global Frame1_1_2
        Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="8", background="#fffffe")
        Frame1_1_2.place(relx=0.081, rely=0.547, relheight=0.415, relwidth=0.848)

    def selectDeposit(self):
        depositMoney(Toplevel(self.master))

    def selectWithdraw(self):
        withdrawMoney(Toplevel(self.master))

    def selectChangePIN(self):
        changePIN(Toplevel(self.master))

    def selectCloseAccount(self):
        self.master.withdraw()
        closeAccount(Toplevel(self.master))

    def exit(self):
        self.master.withdraw()
        CustomerLogin(Toplevel(self.master))

    def checkBalance(self):
        output = display_account_summary(customer_accNO, 2)
        self.printMessage(output)
        print("check balance function called.")

    def printMessage(self, output):
        # clearing the frame
        for widget in Frame1_1_2.winfo_children():
            widget.destroy()
        # getting output_message and displaying it in the frame
        output_message = Label(Frame1_1_2, text=output, background="#fffffe")
        output_message.pack(pady=20)

    def printMessage_outside(output):
        # clearing the frame
        for widget in Frame1_1_2.winfo_children():
            widget.destroy()
        # getting output_message and displaying it in the frame
        output_message = Label(Frame1_1_2, text=output, background="#fffffe")
        output_message.pack(pady=20)


# backend function in order to the system

# check the credentials of users inside the system
def check_credentials(identity, password, choice, admin_access): # checks credentials of admin/customer and returns True or False
    folder_name = "./database/Admin" if (choice == 1) else "./database/Customer"
    file_name = "/adminDatabase.txt" if (choice == 1) else "/customerDatabase.txt"

    try:
        os.makedirs(folder_name, exist_ok=True)
        database = open(folder_name + file_name, "r")
    except FileNotFoundError:
        print("#", folder_name[2:], "database doesn't exists!\n# New", folder_name[2:], "database created automatically.")
        database = open(folder_name + file_name, "a")
        if choice == 1:
            database.write("admin\nadmin@123\n*\n")
    else:
        is_credentials_correct = False
        for line in database:
            id_fetched = line.replace("\n", "")
            password_fetched = database.__next__().replace("\n", "")
            if id_fetched == identity:
                if ((password == "DO_NOT_CHECK_ADMIN" and choice == 1 and admin_access == False) or (
                        password == "DO_NOT_CHECK" and choice == 2 and admin_access == True) or password_fetched == password):
                    is_credentials_correct = True
                    database.close()
                    return True
            if choice == 1:  # skips unnecessary lines in admin database.
                database.__next__()  # skipping line
            else:  # skips unnecessary lines in customer database.
                for index in range(10):
                    fetched_line = database.readline()
                    if fetched_line is not None:
                        continue
                    else:
                        break
        if is_credentials_correct:
            print("Success!")
        else:
            print("Failure!")

    database.close()
    return False


# GUI ends here
top = welcomeScreen(root)
root.mainloop()
