from tkinter import *
import tkinter.font
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
from attendance import Attendance
import webbrowser
from time import strftime
from datetime import datetime
from developer import Developer

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System(student)")

        bg_img=Image.open(r"images\images.png")
        bg_img=bg_img.resize((1540,710),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1530,height=710)

        canvas = Canvas(self.root, width=1530, height=710)
        canvas.create_image(0, 0, image=self.photoimg, anchor="nw")
        canvas.pack()
        
        transparent = "black"
        font = tkinter.font.Font(family="Allcan DEMO", size=30, weight="bold")
        title_lbl = Label(canvas, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=font, fg="white", bg=transparent)
        title_lbl.place(x=0, y=0, width=1380, height=45) 

        def time():
            string= strftime('%H:%M:%S')
            lb1.config(text= string)
            lb1.after(1000, time)

        lb1= Label(title_lbl, font=("Allcan DEMO",15, "bold"),background="black", foreground="white")
        lb1.place(x=0,y=0,width=110,height=50)
        time()
 
        #student details
        img5 = Image.open(r"images\Student.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(canvas, image=self.photoimg5,command=self.student_details, cursor="hand2")
        btn1.place(x=250, y=100, width=220, height=220)

        btn1_1 = Button(canvas, text="Student Details",command=self.student_details, cursor="hand2",font=("Allcan DEMO",15, "bold"))
        btn1_1.place(x=250, y=300, width=220, height=40)

        #attendence
        img7 = Image.open(r"images\attendence.webp")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7= ImageTk.PhotoImage(img7)

        btn1 = Button(canvas, image=self.photoimg7, cursor="hand2",command=self.attendance_data)
        btn1.place(x=550, y=100, width=220, height=220)

        btn1_1 = Button(canvas, text="Attendance", cursor="hand2",command=self.attendance_data,font=("Allcan DEMO",15, "bold"))
        btn1_1.place(x=550, y=300, width=220, height=40)

        #help
        img8 = Image.open(r"images\help.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        btn1 = Button(canvas, image=self.photoimg8, cursor="hand2",command=self.open_html)
        btn1.place(x=850, y=100, width=220, height=220)

        btn1_1 = Button(canvas, text="Help", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.open_html)
        btn1_1.place(x=850, y=300, width=220, height=40)
 
        #train data
        img9 = Image.open(r"images\train_data.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9= ImageTk.PhotoImage(img9)

        btn1 = Button(canvas, image=self.photoimg9, cursor="hand2",command=self.train_data)
        btn1.place(x=100, y=400, width=220, height=220)

        btn1_1 = Button(canvas, text="Train Data", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.train_data)
        btn1_1.place(x=100, y=600, width=220, height=40)

        #photos
        img10 = Image.open(r"images\photo.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        btn1 = Button(canvas, image=self.photoimg10, cursor="hand2",command=self.open_img)
        btn1.place(x=400, y=400, width=220, height=220)

        btn1_1 = Button(canvas, text="Photos", cursor="hand2",command=self.open_img,font=("Allcan DEMO",15, "bold"))
        btn1_1.place(x=400, y=600, width=220, height=40)

        #developer
        img11 = Image.open(r"images\Developer.webp")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        btn1 = Button(canvas, image=self.photoimg11, cursor="hand2",command=self.developer)
        btn1.place(x=700, y=400, width=220, height=220)

        btn1_1 = Button(canvas, text="Developer", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.developer)
        btn1_1.place(x=700, y=600, width=220, height=40)

        #exit
        img12 = Image.open(r"images\exit.jpg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12= ImageTk.PhotoImage(img12)

        btn1 = Button(canvas, image=self.photoimg12, cursor="hand2",command=self.iExit)
        btn1.place(x=1000, y=400, width=220, height=220)

        btn1_1 = Button(canvas, text="EXIT", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.iExit)
        btn1_1.place(x=1000, y=600, width=220, height=40)

        

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=messagebox.askyesno("exit","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
    def open_html(self):
            webbrowser.open_new_tab('contact_me.html')

        #---------------- function buttons-----------------

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


if __name__ == "__main__":
    root= Tk()
    obj = Face_recognition_system(root)
    root.mainloop()