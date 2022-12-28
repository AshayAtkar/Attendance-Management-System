from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from subprocess import call
import os
import mysql.connector as sql
import Attendance_GUI
import Signup_GUI


class Student_Management_System :
    # ============Verifying Credentials==============
    def check(self):
        for self.name,self.secret in self.name_list:
            if(self.name==self.uservalue.get() and self.secret==self.passvalue.get()):
                return True
        return False
    def show(self):
        self.login = sql.connect(host='localhost',user='root',password='root',database='sams')
        self.cur = self.login.cursor()
        self.query_access = "SELECT * FROM login"
        self.cur.execute(self.query_access)
        self.name_list = self.cur.fetchall()
        if(self.check()):
            msg.showinfo("login successful","Login Successful")
            self.call_another_python_file()
        else:
            msg.showwarning("WARNING","WRONG PASSWORD OR USERNAME")
            
    def call_another_python_file(self):
        self.root.destroy()
        self.main_root=Tk()
        self.obj = Attendance_GUI.home_page(self.main_root)
        self.main_root.mainloop()
        
        
    def call_sign_up_file(self):
        self.root.destroy()
        self.signup_root=Tk()
        self.obj = Signup_GUI.Sign(self.signup_root)
        self.signup_root.mainloop()
        
    def __init__(self, root) :
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x500+0+0")

        # ============Image==============
        self.image1 = Image.open(r"C:\Users\Ayushi\Desktop\Attendance Management System\Login.png") 
        self.image1 = self.image1.resize((400, 500), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(self.image1)
        self.lblimage = Label(self.root, image = self.photoimage1, bd = 4, relief = RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)

        # ===================Blue frame ================
        self.main_frame = Frame(self.root, width=590, height=500, relief=SUNKEN, bg='blue')
        self.main_frame.place(x=0, y = 0)

        # ======================LOGIN=====================
        self.login = Label(self.root, text="LOGIN", font="comicsans 20 bold", bg='red', fg='black', width=25)
        self.login.place(x = 85, y = 125)

        # ========================Username password==========
        self.username = Label(self.root, text="Username", font="comicsans 15 bold", bg='blue', fg='white', width=17)
        self.password = Label(self.root, text="Password", font="comicsans 15 bold", bg='blue', fg='white', width=17)
        self.username.place(x=85, y=200)
        self.password.place(x=85, y=250)

        # =======================Taking entry=================
        self.uservalue = StringVar()
        self.passvalue = StringVar()
        self.userentry = Entry(self.root, textvariable=self.uservalue, width=25)
        self.passentry = Entry(self.root, textvariable=self.passvalue,show='*', width=25)
        # print(uservalue)
        self.userentry.place(x=362, y = 205)
        self.passentry.place(x = 362, y = 255)


        # ===================Login Button====================
        self.login_button = Button(self.root, text="Login", font="comicsans 10 bold", bg='white',
                                   fg='black', width=17, height=1,command=self.show)
        self.signup_button = Button(self.root, text="Signup", font="comicsans 10 bold", bg='white',
                                    fg='black', width=17, height=1,command=self.call_sign_up_file)
        self.login_button.place(x=155, y=300)
        self.signup_button.place(x=305, y=300)

if __name__ =='__main__':

    root = Tk()
    obj = Student_Management_System(root)
    root.mainloop()