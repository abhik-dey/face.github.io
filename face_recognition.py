from tkinter import *
import tkinter.font
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from twilio.rest import Client
from sklearn.metrics import confusion_matrix
import schedule
import time


class Face_Recognition:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        bg_img=Image.open(r"images\face.jpg")
        bg_img=bg_img.resize((1390,710),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1390,height=710)

        canvas = Canvas(self.root, width=1530, height=710)
        canvas.create_image(0, 0, image=self.photoimg, anchor="nw")
        canvas.pack()
        
        transparent = "white"
        font = tkinter.font.Font(family="Allcan DEMO", size=30, weight="bold")
        title_lbl = Label(canvas, text="FACE RECOGNITION",font=font, fg="black", bg=transparent)
        title_lbl.place(x=0, y=0, width=1380, height=45)

        btn1_1 = Button(canvas, text="Face Recognition", cursor="hand2",command=self.face_recog,font=("Microsoft Yahei UI Light",15, "bold"),fg="white",bg="#57a1f8")
        btn1_1.place(x=905, y=490, width=286, height=90)

    #---------------attendence----------------------
    def mark_attendance(self,i,r,n,d,m):
        conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
        present = "PRESENT"
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d")
        time_string = now.strftime("%H:%M:%S")
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        day_of_week = date_object.strftime('%A')
        cursor = conn.cursor()

        query = "SELECT * FROM attendance WHERE Student_id = %s AND date = %s"
        values = (i, date_string)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result is None:
            query = "INSERT INTO attendance (Student_id, Roll, Name, Dept, date, time, status, day, Division) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (i, r, n, d, date_string, time_string, present, day_of_week, m)
            cursor.execute(query, values)
        conn.commit()
        conn.close()

    #---------------face recognition-----------------
    
    def face_recog(self):
        # def send_sms(sid, name, phone_number):
        # #      # Set up your Twilio account credentials
        #          account_sid = "ACb75d02357389e96d610fed16c8d749c8"
        #          auth_token = "1c127f431564ce5215b6ada00b5d2357"
        #          client = Client(account_sid, auth_token)

        # #          # Set up the message content
        #          message = client.messages \
        #                          .create(
        #                              body=f"Hello {name}! Your attendance has been marked.",
        #                              from_='+447782367705',
        #                              to=phone_number
        #              )
        true_labels = []
        predicted_labels = []

        def recognize(img,clf,faceCascade,section):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf,section)
            return img

        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf,section):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
            my_cursor=conn.cursor()

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                

                my_cursor.execute("SELECT Name FROM student WHERE Student_id="+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    n="+".join(str(name) for name in n)
                

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id="+str(id))
                r=my_cursor.fetchone()
                if r is not None:
                    r="+".join(str(roll) for roll in r)
                

                my_cursor.execute("SELECT Dept FROM student WHERE Student_id="+str(id))
                d=my_cursor.fetchone()
                if d is not None:
                    d="+".join(str(dept) for dept in d)
                

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id="+str(id))
                i=my_cursor.fetchone()
                if i is not None:
                    i="+".join(str(sid) for sid in i)
                
                
                my_cursor.execute("SELECT Division FROM student WHERE Student_id="+str(id))
                result=my_cursor.fetchone()
                if result is not None:
                    m=result[0]

                true_labels.append(i)  # Update with the actual label
                predicted_labels.append(id)  # Update with the predicted label
                print("Actual Label:", i)
                print("Predicted Label:", id)

                
                print(confidence)
                if confidence>76 and m == section:

                    cv2.putText(img,f"ID:{i}",(x,y-77),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Confidence Level: {confidence}",(x,y+300),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3 )

                    
                   
                    self.mark_attendance(i, r, n, d, m)
                    
                    # my_cursor.execute("SELECT Phone FROM student WHERE Student_id="+str(id))
                    # phone_number = my_cursor.fetchone()[0]

                    # #  # Send an SMS notification to the student's phone number
                    # send_sms(i, n, phone_number)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                                

                coord=[x,y,w,h]

            return coord

        def start_face_recognition():
            section = student_id_dropdown.get()

            video_cap=cv2.VideoCapture(0)

            video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1530)
            video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 790)

            

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade,section)
                cv2.imshow("Welcome to face recognition",img)

                if cv2.waitKey(1)==13:
                    video_cap.release()
                    cv2.destroyAllWindows()
                    break

        root = Tk()
        root.title("face")
        root.geometry("400x200")

                # Create a label for the student ID dropdown
        student_id_label = Label(root, text="Select Section:")
        student_id_label.pack()

                # Create a dropdown to select the student ID
        student_id_dropdown = ttk.Combobox(root, width=20, state="readonly")
        student_id_dropdown["values"]=("Select","A","B","C")
        student_id_dropdown.current(0)
        student_id_dropdown.pack()

        

                # Create a button to generate the dataset for the selected student ID
        generate_dataset_button = Button(root, text="submit", command=start_face_recognition)
        generate_dataset_button.pack()
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        def calculate_confusion_matrix():
            cm = confusion_matrix(true_labels, predicted_labels)
            print("Confusion Matrix:")
            print(cm)

        calculate_confusion_matrix()

if __name__ == "__main__":
    root= Tk()
    obj = Face_Recognition(root)
    root.mainloop()