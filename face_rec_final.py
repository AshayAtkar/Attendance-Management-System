import face_recognition
import cv2
import os
import sys
import numpy as np
import time
import student_name

class Encoding_Attendance:
    def __init__(self,datevar):
        self.datevar = datevar
        self.a = 0
        self.count = []
        self.i = 0
        self.obj = student_name.Students_name()
        self.namelist = self.obj.names()
        self.names = self.namelist[0]
        self.mylist = self.namelist[1]
        print(len(self.names))
        if len(self.mylist) == 0 :
            print("Error! Cannot find registered students")
            sys.exit()
        self.students_im = []
        for per in self.mylist:
            self.image = cv2.imread(f'{"images"}/{per}')
            self.students_im.append(self.image)
            self.count.append(0)
        print(self.mylist)
        print(self.students_im)
        self.encodelistknown = self.findencodings()
        print("Encoding Complete")
        print(self.mylist)
        print(self.names)
        print("Taking Attendance, Please Wait ......")
        self.attendance()
        

        #==============================Encoding ends============================

        
    def findencodings(self):
        self.encodelist = []
        for img in self.students_im :
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.encode = face_recognition.face_encodings(img)[0]
            self.encodelist.append(self.encode)
        return self.encodelist
    
    def attendance(self):
        os.chdir(f"C:/Users/Ayushi/Desktop/Attendance Management System/{self.datevar}")
        self.list_of_frames = os.listdir()
        i=0
        while(i < (len(self.list_of_frames) - 1)):
            self.img = cv2.imread(f"frame{i}.jpg")
            self.imgS = cv2.resize(self.img, (0, 0), None, 0.25, 0.25)
            self.imgS = cv2.cvtColor(self.imgS, cv2.COLOR_BGR2RGB)
            self.faces_in_frame = face_recognition.face_locations(self.imgS)
            self.encodecap = face_recognition.face_encodings(self.imgS, self.faces_in_frame)
            
            for encodeFace, faceLoc in zip(self.encodecap, self.faces_in_frame) :
                self.matches = face_recognition.compare_faces(self.encodelistknown, encodeFace)
                self.faceDis = face_recognition.face_distance(self.encodelistknown, encodeFace)
                self.match_index = np.argmin(self.faceDis)
                self.name = self.names[self.match_index].upper()
                if self.matches[self.match_index]:
                    self.count[self.match_index] = self.count[self.match_index] + 1
            
            i=i+1
        print(self.count)
        self.cwf = os.getcwd().split("\\")[-1]
        os.chdir(r'C:\Users\Ayushi\Desktop\Attendance Management System\stat_files')
        self.my_file = open(self.cwf + ".csv","w+")
        for j in range(0, len(self.names)) :
            if self.count[j] >= (len(self.list_of_frames)/2) :
                self.my_file.writelines(self.names[j] + "\n")
        self.my_file.close()