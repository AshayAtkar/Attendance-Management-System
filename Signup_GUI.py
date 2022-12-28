from tkinter import *
from PIL import Image,ImageTk
import os
from subprocess import call
import mysql.connector as sql
from tkinter import messagebox as msg

    

class Sign:
    def database_create(self):
        if(self.pass_word.get()==self.re_pass_word.get()):
            self.login = sql.connect(host='localhost',user='root',password='root')
            self.password = sql.connect(host='localhost',user='root',password='root',database='sams')
            self.pas = self.password.cursor()
            self.query_insert = "INSERT INTO login (Username,Password) VALUES(%s,%s)"
            self.variable = (self.user_name.get(),self.pass_word.get())
            self.pas.execute(self.query_insert,self.variable)
            self.password.commit()
            self.signup_root.destroy()
            self.path = r"C:\Users\Ayushi\Desktop\Attendance Management System"
            os.chdir(self.path)
            call(["python","login_page.py"])
        else:
            msg.showerror("Warning", "Passowrd not same as re- entered password")
    def __init__(self,signup_root):
        self.signup_root = signup_root
        self.signup_root.title("Sign Up")
        self.signup_root.geometry("1000x500")
        self.signup_root.minsize(1000,500)
        self.signup_root.maxsize(1000,500)
        
        self.image1 = Image.open(r"C:\Users\Ayushi\Desktop\Attendance Management System\Login.png") 
        self.image1 = self.image1.resize((400, 500))
        self.photoimage1 = ImageTk.PhotoImage(self.image1)
        self.lblimage = Label(image = self.photoimage1, borderwidth = 6, relief = RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)
        
        self.main_frame = Frame(self.signup_root, width=600, height=500, relief=SUNKEN, bg='#4a7abc')
        self.main_frame.place(x=0, y = 0)
        
        self.signup = Label(signup_root, text="SIGN UP", font="comicsans 20 bold", bg='red', fg='white', width=25, height=1)
        self.signup.place(x = 85, y = 125)
        
        self.username = Label(self.signup_root, text="Username :", font="comicsans 15 bold", bg='#4a7abc', fg='white', width=17, height=1)
        self.password = Label(self.signup_root, text="Password :", font="comicsans 15 bold", bg='#4a7abc', fg='white', width=17, height=1)
        self.re_password = Label(self.signup_root, text="Re-enter Password :", font="comicsans 15 bold", bg='#4a7abc', fg='white', width=17, height=1)
        self.username.place(x=85, y=200)
        self.password.place(x=85, y=250)
        self.re_password.place(x=45, y=300)
        
        self.user_name = StringVar()
        self.pass_word = StringVar()
        self.re_pass_word = StringVar()
        self.userentry = Entry(signup_root, textvariable=self.user_name, width=30)
        self.passentry = Entry(signup_root, textvariable=self.pass_word,show='*', width=30)
        self.re_passentry = Entry(signup_root, textvariable=self.re_pass_word,show='*', width=30)
        self.userentry.place(x = 260, y = 205)
        self.passentry.place(x = 260, y = 255)
        self.re_passentry.place(x= 260 , y= 305)
        
        self.signup_button = Button(self.signup_root, text="Sign Up", font="comicsans 10 bold", bg='green',
                               fg='white', width=17, height=1,command=self.database_create)
        self.signup_button.place(x=225, y=350)