import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from glob import glob
from tkinter import messagebox
from subprocess import call
from tkcalendar import Calendar
from datetime import date


class stats :
    def main_menu(self):
        self.root.destroy()
        self.path = r"C:\Users\Ayushi\Desktop\Attendance Management System"
        os.chdir(self.path)
        call(["python","Attendance_GUI.py"])
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Statistics")
        self.root.geometry("1000x500+0+0")

        # Creating A Main Frame
        self.main_frame = Frame(root)
        self.main_frame.pack(fill=BOTH, expand=1)

        # Creating A Canvas
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Adding A Scrollbar To The Canvas
        self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        self.second_frame = Frame(self.my_canvas, width=1000, height=3000, bg='blue')

        # Add that New frame To a Window In The Canvas
        self.my_canvas.create_window((0,0), window=self.second_frame, anchor="nw")
        
        # ================Image================
        self.image1 = Image.open(r"C:\Users\Ayushi\Desktop\Attendance Management System\stat_img.jpg") 
        self.image1 = self.image1.resize((543, 500), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(self.image1)
        self.lblimage = Label(self.second_frame, image = self.photoimage1, bd = 4, relief = RAISED)
        self.lblimage.place(x = 432, y = 0)

        # ==============Heading==================
        self.lbl = Label(self.second_frame, text='Attendance Statistics', font="comicsans 20 bold", bg='red', fg='black', width=25, height=1)
        self.lbl.place(x=0, y=0)

        # ========================Starting Date and Ending Date==========
        self.str_dt_lbl = Label(self.second_frame, text="  Enter date for which \nstats are required", font="comicsans 15 bold", bg='blue', fg='white', width=17, height=2)
        self.str_dt_lbl.place(x=0, y=150)

        # =======================Ending Date=================
        self.str_dt = StringVar()
        self.str_dt_entry = Entry(self.second_frame, textvariable=self.str_dt, width=20)
        self.str_dt_entry.place(x=260, y = 170)
        
        self.cal_button = Button(self.second_frame,text="Date", font="comicsans 10 bold", bg='white', fg='black', width=3, height=1,command = self.datet)
        self.cal_button.place(x = 390,y = 170)
        
        # ================Get Statistics Button===================
        self.get_stat_but = Button(self.second_frame, text="Get Statistics", font="comicsans 10 bold", bg='white', fg='black', width=17, height=1, command = self.get_stats)
        self.get_stat_but.place(x=60, y=250)

        # ================Back Button===================
        self.back_but = Button(self.second_frame, text="Back", font="comicsans 10 bold", bg='white', fg='black', width=17, height=1,command=self.main_menu)
        self.back_but.place(x=225, y=250)

        # ==================Instruction Label=================
        ins_lbl = Label(self.second_frame, text="NOTE - Enter date from the DATE picker", font="comicsans 15 bold", bg='blue', fg='red', width=35, height=1)
        ins_lbl.place(x=5, y=350)
    def datechoose(self):
        self.datepick = self.cal.get_date()
        print(self.datepick)
        self.cal.destroy()
        self.choosedate.destroy()
        
    def datet(self):
        self.today = date.today()
        print(self.today.year)
        self.cal = Calendar(self.second_frame, selectmode = 'day',
                day = self.today.day,month = self.today.month,year = self.today.year)
        self.cal.place(x=390,y=200)
        self.choosedate = Button(self.second_frame,text="Choose date", font="comicsans 10 bold", bg='white', fg='black', width=17, height=1,command=self.datechoose)
        self.choosedate.place(x=390,y=200)
    
    def get_stats(self):
        self.check_dt = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        self.check_mo = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.err_chk_lst = self.datepick.split('/')
        if len(self.err_chk_lst) == 3:
            if (self.err_chk_lst[1] not in self.check_dt) and (self.err_chk_lst[0] not in self.check_mo) and (self.err_chk_lst[2] not in range(2021, 2051)) :
                messagebox.showerror('Invalid Input', 'Error! Enter date in ')
        else :
            messagebox.showerror('Invalid Input', "Error! Enter date in 'DD-MM-YYYY' format")
        self.my_list = os.listdir(path="C:/Users/Ayushi/Desktop/Attendance Management System/images")
        self.students_name = []
        for per in self.my_list:
            self.students_name.append(os.path.splitext(per)[0])
        self.stat_txt = Text(self.second_frame,bd = 4, relief = RAISED, height=2500, width=1000)
        self.stat_txt.place(x=0, y=500)
        self.filename = self.err_chk_lst[1]+'-'+ self.err_chk_lst[0] +'-'+ self.err_chk_lst[2] +   '.csv'
        print(self.filename)
        os.chdir(r"C:\Users\Ayushi\Desktop\Attendance Management System\stat_files")
        self.curr_file = open(self.filename,'r')
        self.presentees = self.curr_file.readlines()
        self.presentees = [self.presentees[i][0:-1] for i in range(len(self.presentees))]
        self.absentees = list(set(self.students_name) - set(self.presentees))
        print(self.absentees)
        print(self.presentees)
        self.stat_txt.insert(END, "Present Students\n")
        self.stat_txt.insert(END, f"{self.presentees}\n")
        self.stat_txt.insert(END, '\n')
        self.stat_txt.insert(END, "\nAbsent Students\n")
        self.stat_txt.insert(END, f"{self.absentees}\n")
        self.stat_txt.insert(END, '\n')
        self.stat_txt.insert(END, '________________________________________________________\n')