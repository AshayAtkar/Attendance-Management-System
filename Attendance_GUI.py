from tkinter import *
from PIL import Image,ImageTk
import os
from subprocess import call
import statistics_final as st
import face_rec_final as fr

#take attendance
#register a student
#remove student
#get attendance data

class home_page:
    def __init__(self,main_root):
        self.main_root = main_root
        self.main_root.title("STUDENT MANAGEMENT SYSTEM")
        self.main_root.geometry("1000x500")
        self.main_root.minsize(1000,500)
        self.main_root.maxsize(1000,500)
        self.gui()
    
    def statistics_file(self):
        self.main_root.destroy()
        attend = Tk()
        obj = st.stats(attend)
        attend.mainloop()
        
    def image_register_file(self):
        self.main_root.destroy()
        self.path = r"C:\Users\Ayushi\Desktop\Attendance Management System"
        os.chdir(self.path)
        call(["python","image_register_final.py"])
        
    def login_file(self):
        self.main_root.destroy()
        self.path = r"C:\Users\Ayushi\Desktop\Attendance Management System"
        os.chdir(self.path)
        call(["python","login_page.py"])
        
    def attendance(self):
        self.path = r"C:\Users\Ayushi\Desktop\Attendance Management System"
        self.obj = fr.Encoding_Attendance(self.datevar.get())
        

    def gui(self):
        # ==================Image on login page=====================
        self.image1 = Image.open(r"C:\Users\Ayushi\Desktop\Attendance Management System\Login.png") 
        self.image1 = self.image1.resize((400, 500))
        self.photoimage1 = ImageTk.PhotoImage(self.image1)
        self.lblimage = Label(image = self.photoimage1, borderwidth = 6, relief = RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)

        # ============================Constructing Main Frame========================
        self.main_frame = Frame(self.main_root, width=600, height=500, relief=SUNKEN, bg='#3a86ff')
        self.main_frame.place(x=0, y = 0)

        # ====================Adding Text "STUDENT MANAGEMENT SYSTEM"=======================
        self.main = Label(self.main_root, text="STUDENT MANAGEMENT SYSTEM", font="comicsans 20 bold", bg='red', 
                     fg='white', width=35, height=1)
        self.main.place(x = 0, y = 50)

        # =====================Button for Taking attendance=================
        self.attendance_button = Button(self.main_root, text="Take Attendance", font="comicsans 13 bold", bg='green', 
                                   fg='white', width=17, height=1,command = self.attendance)
        self.attendance_button.place(x=200, y=150)
        
        # ===================Constructing String Variable======================
        self.datevar = StringVar()
        
        # ========================Taking Date Input==========================
        self.date_required = Entry(self.main_root,textvariable=self.datevar,width=20)
        self.date_required.place(x=400 ,y = 150)

        # ==========================Button for registering new student======================
        self.register_button = Button(self.main_root, text="Register a Student", font="comicsans 13 bold", bg='green', 
                                 fg='white', width=17, height=1,command=self.image_register_file)
        self.register_button.place(x=200, y=225)

        # ==========================Button for redirecting to statistics page======================
        self.getdata_button = Button(self.main_root, text="Get Attendance Data", font="comicsans 13 bold", bg='green', 
                                fg='white', width=17, height=1,command=self.statistics_file)
        self.getdata_button.place(x=200, y=300)

        # ==========================Button for Loging Out======================
        self.logout_button = Button(self.main_root, text="Log Out", font="comicsans 10 bold", bg='green', 
                               fg='white', width=17, height=1,command=self.login_file)
        self.logout_button.place(x=425, y=100)