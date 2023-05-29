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

class Face_recognition_system1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System(Teacher)")

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

        #face detection
        img6 = Image.open(r"images\facial.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6= ImageTk.PhotoImage(img6)

        btn1 = Button(canvas, image=self.photoimg6, cursor="hand2",command=self.face_data)
        btn1.place(x=250, y=100, width=220, height=220)

        btn1_1 = Button(canvas, text="Face Detector", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.face_data)
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
 

        #developer
        img11 = Image.open(r"images\Developer.webp")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        btn1 = Button(canvas, image=self.photoimg11, cursor="hand2",command=self.developer)
        btn1.place(x=400, y=400, width=220, height=220)

        btn1_1 = Button(canvas, text="Developer", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.developer)
        btn1_1.place(x=400, y=600, width=220, height=40)

        #exit
        img12 = Image.open(r"images\exit.jpg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12= ImageTk.PhotoImage(img12)

        btn1 = Button(canvas, image=self.photoimg12, cursor="hand2",command=self.iExit)
        btn1.place(x=700, y=400, width=220, height=220)

        btn1_1 = Button(canvas, text="EXIT", cursor="hand2",font=("Allcan DEMO",15, "bold"),command=self.iExit)
        btn1_1.place(x=700, y=600, width=220, height=40)

        


    def iExit(self):
        self.iExit=messagebox.askyesno("exit","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
    def open_html(self):
            webbrowser.open_new_tab('contact_me.html')

        #---------------- function buttons-----------------

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


if __name__ == "__main__":
    root= Tk()
    obj = Face_recognition_system1(root)
    root.mainloop()