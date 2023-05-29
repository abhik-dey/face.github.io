from tkinter import *
import tkinter.font
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        # image
        bg_img=Image.open(r"images\train.jpg")
        bg_img=bg_img.resize((1400,710),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1530,height=710)

        canvas = Canvas(self.root, width=1530, height=710)
        canvas.create_image(0, 0, image=self.photoimg, anchor="nw")
        canvas.pack()
        
        transparent = "white"
        font = tkinter.font.Font(family="Allcan DEMO", size=30, weight="bold")
        title_lbl = Label(canvas, text="TRAIN DATA SET",font=font, fg="black", bg=transparent)
        title_lbl.place(x=0, y=0, width=1380, height=45)


        btn1_1 = Button(canvas,text= "Train",cursor="hand2",command=self.train_classifier,font=("Microsoft Yahei UI Light",23,"bold"),bg="white",fg="black", borderwidth=2, highlightthickness=2,relief=SOLID)
        btn1_1.place(x=630, y=290, width=140, height=140)

    def train_classifier(data_dir, classifier_file=None):
        data_dir = "data"
        folders = os.listdir(data_dir)

        faces = [] 
        ids = []

        for folder in folders:
            folder_path = os.path.join(data_dir, folder)
            images = os.listdir(folder_path)
            
            for image in images:
                img_path = os.path.join(folder_path, image)
                img = Image.open(img_path).convert('L')
                imageNp = np.array(img, 'uint8')
                id = int(folder.split("_")[2])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
        ids=np.array(ids)

        #--------train the classifier--------
        if classifier_file is not None and os.path.exists(classifier_file):
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read(classifier_file)
            
            # Update the classifier with the new data
            clf.update(faces, ids)
        else:
            clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")


if __name__ == "__main__":
    root= Tk()
    obj = Train(root)
    root.mainloop()