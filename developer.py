from tkinter import *
import tkinter.font
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import os
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("developer details")

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
        title_lbl = Label(canvas, text="DEVELOPERS",font=font, fg="white", bg=transparent)
        title_lbl.place(x=0, y=0, width=1380, height=45) 

        img5 = Image.open(r"images\abhik.jpg")
        img5 = img5.resize((250, 250), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl_left=Label(canvas,image=self.photoimg5)
        f_lbl_left.place(x=300,y=200,width=250,height=250)

        font = tkinter.font.Font(family="Allcan DEMO", size=15, weight="bold")
        title_lbl = Label(canvas, text="Abhik Dey(201900073) CSE",font=font, fg="white", bg="black")
        title_lbl.place(x=300, y=450, width=250, height=25) 

        img6 = Image.open(r"images\saksham.jpg")
        img6 = img6.resize((300, 250), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        f_lbl_lef=Label(canvas,image=self.photoimg6)
        f_lbl_lef.place(x=800,y=200,width=300,height=250)

        font = tkinter.font.Font(family="Allcan DEMO", size=15, weight="bold")
        title_lbl1 = Label(canvas, text="Saksham Suman(201900105) CSE",font=font, fg="white", bg="black")
        title_lbl1.place(x=800, y=450, width=300, height=25) 



if __name__ == "__main__":
    root= Tk()
    obj = Developer(root)
    root.mainloop()