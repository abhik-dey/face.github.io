from tkinter import *
import tkinter.font
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox, simpledialog
import mysql.connector
import numpy as np
import os
import cv2
import csv
from tkinter import filedialog
import shutil

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        self.var_sub_id=StringVar()
        self.var_start=StringVar()
        self.var_end=StringVar()
        self.var_day=StringVar()
        self.var_name=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()

        #----variables---------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        bg_img=Image.open(r"C:\Users\abhik dey\Desktop\Face recognition system\images\images.png")
        bg_img=bg_img.resize((1540,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1530,height=710)

        canvas = Canvas(self.root, width=1530, height=710)
        canvas.create_image(0, 0, image=self.photoimg, anchor="nw")
        canvas.pack()
        
        
        font = tkinter.font.Font(family="Allcan DEMO", size=30, weight="bold")
        title_lbl = Label(canvas, text="ATTENDANCE",font=font, fg="white", bg="black")
        title_lbl.place(x=0, y=20, width=1380, height=45) 

        main_frame = Frame(canvas, bd=2)
        main_frame.place(x=0,y=80,width=1500, height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="light grey", relief=SOLID,text="Time Table",font=("Allcan DEMO",15, "bold"))
        Left_frame.place(x=10,y=10,width=670,height=580)

        Left_img=Image.open(r"C:\Users\abhik dey\Desktop\Face recognition system\images\smit.png")
        Left_img=Left_img.resize((660,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(Left_img)

        f_lbl_left=Label(Left_frame,image=self.photoimg_left)
        f_lbl_left.place(x=3,y=0,width=660,height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE)
        left_inside_frame.place(x=3,y=135,width=660, height=420)

        #labels and entery
        subjectId_label=Label(left_inside_frame, text="Subject ID:",font=("Allcan DEMO",12, "bold"))
        subjectId_label.grid(row=0,column=0,pady=15,sticky=W)

        subject_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_sub_id,font=("Allcan DEMO",12, "bold"))
        subject_entry.grid(row=0,column=1,pady=15,sticky=W)

        #roll
        division_label=Label(left_inside_frame, text="Section:",font=("Allcan DEMO",12, "bold"))
        division_label.grid(row=0,column=2,pady=15,padx=12,sticky=W)

        self.division_combo=ttk.Combobox(left_inside_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=18,textvariable=self.var_div)
        self.division_combo["values"]=("Section","A","B","C")
        self.division_combo.current(0)
        self.division_combo.grid(row=0,column=3,pady=15,sticky=W)

        #dept
        start_label=Label(left_inside_frame, text="Start Time:",font=("Allcan DEMO",12, "bold"))
        start_label.grid(row=1,column=2,pady=15,padx=12,sticky=W)

        self.start_combo=ttk.Combobox(left_inside_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=18,textvariable=self.var_start)
        self.start_combo["values"]=("select","9:00:00","10:00:00","11:00:00","12:00:00","14:00:00","15:00:00","16:00:00")
        self.start_combo.current(0)
        self.start_combo.grid(row=1,column=3,pady=15,sticky=W)

        #time
        end_label=Label(left_inside_frame, text="End Time:",font=("Allcan DEMO",12, "bold"))
        end_label.grid(row=2,column=2,pady=15,padx=12,sticky=W)

        self.end_combo=ttk.Combobox(left_inside_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=18,textvariable=self.var_end)
        self.end_combo["values"]=("select","10:00:00","11:00:00","12:00:00","13:00:00","15:00:00","16:00:00","17:00:00")
        self.end_combo.current(0)
        self.end_combo.grid(row=2,column=3,pady=15,sticky=W)

        #date
        day_label=Label(left_inside_frame, text="Day:",font=("Allcan DEMO",12, "bold"))
        day_label.grid(row=2,column=0,pady=15,sticky=W)

        self.day_combo=ttk.Combobox(left_inside_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=18,textvariable=self.var_day)
        self.day_combo["values"]=("Day","Monday","Tuesday","Wednesay","Thrusday","Friday","Saturday")
        self.day_combo.current(0)
        self.day_combo.grid(row=2,column=1,pady=15,sticky=W)


        #attendance
        name_label=Label(left_inside_frame, text="Subject name:",font=("Allcan DEMO",12, "bold"))
        name_label.grid(row=1,column=0,pady=15,sticky=W)

        self.name_combo=ttk.Combobox(left_inside_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=18,textvariable=self.var_name)
        self.name_combo["values"]=("Subjects","PP Lab","FLAT","CN-II","CN Lab","Mini Project","Minor Specialization","PE-IV","PE-V","PE-VI")
        self.name_combo.current(0)
        self.name_combo.grid(row=1,column=1,pady=15,sticky=W)

         #buttons frame
        btn_frame=LabelFrame(left_inside_frame,bd=2, relief=RIDGE)
        btn_frame.place(x=3,y=370,width=650,height=29)

        Delete=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        Delete.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.export_csv,width=19,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        export_btn.grid(row=0,column=1)

        Add_btn=Button(btn_frame,text="Add",width=19,command=self.add_data,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        Add_btn.grid(row=0,column=3)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2, relief=SOLID,text="Attendance ",font=("Allcan DEMO",15, "bold"),bg="light grey")
        right_frame.place(x=690,y=10,width=660,height=580)

        Right_img=Image.open(r"C:\Users\abhik dey\Desktop\Face recognition system\images\smit.png")
        Right_img=Right_img.resize((660,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(Right_img)

        f_lbl_right=Label(right_frame,image=self.photoimg_right)
        f_lbl_right.place(x=3,y=0,width=650,height=130)

        #top frame
        top_frame=Frame(right_frame,bd=2, relief=RIDGE)
        top_frame.place(x=4,y=135,width=650,height=130)

        search_id_label=Label(top_frame, text="Section",font=("Allcan DEMO",12, "bold"))
        search_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.search_id_combo=ttk.Combobox(top_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=15)
        self.search_id_combo["values"]=("Select","A","B","C")
        self.search_id_combo.current(0)
        self.search_id_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_start_label=Label(top_frame, text="Start time",font=("Allcan DEMO",12, "bold"))
        search_start_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        self.search_start_combo=ttk.Combobox(top_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=15)
        self.search_start_combo["values"]=("Select","9:00:00","10:00:00","11:00:00","12:00:00","14:00:00","15:00:00","16:00:00")
        self.search_start_combo.current(0)
        self.search_start_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        search_end_label=Label(top_frame, text="End time",font=("Allcan DEMO",12, "bold"))
        search_end_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        self.search_end_combo=ttk.Combobox(top_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=15)
        self.search_end_combo["values"]=("Select","10:00:00","11:00:00","12:00:00","13:00:00","15:00:00","16:00:00","17:00:00")
        self.search_end_combo.current(0)
        self.search_end_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        search_day_label=Label(top_frame, text="Day",font=("Allcan DEMO",12, "bold"))
        search_day_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        self.search_day_combo=ttk.Combobox(top_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=15)
        self.search_day_combo["values"]=("Select","Monday","Tuesday","Wednesay","Thrusday","Friday","Saturday")
        self.search_day_combo.current(0)
        self.search_day_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        search_btn=Button(top_frame,text="Search",width=12,font=("Allcan DEMO",10, "bold"),bg="grey",fg="white",command=self.fetch_attendance_data)
        search_btn.grid(row=2,column=4,padx=4)


         # table frame
        table_frame=Frame(right_frame,bd=2, relief=RIDGE)
        table_frame.place(x=4,y=265,width=650,height=290)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Attendance_table=ttk.Treeview(table_frame,column=("id","rollno","name","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("id",text="Student Id")
        self.Attendance_table.heading("rollno",text="Roll no.")
        self.Attendance_table.heading("name",text="Name")
        self.Attendance_table.heading("department",text="Department")
        self.Attendance_table.heading("date",text="Date")
        self.Attendance_table.heading("time",text="Time")
        self.Attendance_table.heading("attendance",text="Attendance")
        self.Attendance_table["show"]="headings"

        self.Attendance_table.column("id",width=100)
        self.Attendance_table.column("rollno",width=100)
        self.Attendance_table.column("name",width=100)
        self.Attendance_table.column("department",width=100)
        self.Attendance_table.column("time",width=100)
        self.Attendance_table.column("date",width=100)
        self.Attendance_table.column("attendance",width=100)

        self.Attendance_table.pack(fill=BOTH,expand=1)
        self.Attendance_table.bind("<ButtonRelease>",self.get_cursor)
        

    def add_data(self):
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into timetable values(%s,%s,%s,%s,%s)",(

                                                                                                                self.var_div.get(),
                                                                                                                self.var_sub_id.get(),
                                                                                                                self.var_start.get(),
                                                                                                                self.var_end.get(),
                                                                                                                self.var_day.get(),
                                                                                                                
                                                                                                            ))
                my_cursor.execute("insert into subject values(%s,%s)",(

                                                                                                                self.var_sub_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                
                                                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","Time table has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #fetch data
    def fetch_attendance_data(self):

        subject_id = self.search_id_combo.get()
        start_time = self.search_start_combo.get()
        end_time = self.search_end_combo.get()
        day = self.search_day_combo.get()

        # Check if any combo box has a selected value
        if subject_id == "Select" and start_time == "Select" and end_time == "Select" and day == "Select":
            return
        
        conn = mysql.connector.connect(host="localhost", user="root", password="Abhik1@1dey", database="face_recognizer")
        my_cursor = conn.cursor()
        
        # Construct SQL query based on selected values
        query = f"SELECT attendance.* FROM attendance JOIN timetable ON attendance.time BETWEEN timetable.start_time AND timetable.end_time WHERE timetable.start_time = '{start_time}' AND timetable.end_time = '{end_time}' AND attendance.day = timetable.day_of_week AND timetable.day_of_week = '{day}' AND attendance.Division = timetable.division AND timetable.division = '{subject_id}'"

        # Execute query and fetch data
        my_cursor.execute(query)
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.Attendance_table.delete(*self.Attendance_table.get_children())
            for i in data:
                self.Attendance_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    #delete 
    def delete_data(self):
        try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from attendance where Student_id=%s"
                    val=(self.var_atten_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_attendance_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted attendance details",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #export csv
    def export_csv(self):
        subject_id = self.search_id_combo.get()
        start_time = self.search_start_combo.get()
        end_time = self.search_end_combo.get()
        day = self.search_day_combo.get()
        if subject_id == "Select" and start_time == "Select" and end_time == "Select" and day == "Select":
             messagebox.showerror("Error","Select the attendance to download",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhik1@1dey", database="face_recognizer")
                cursor = conn.cursor()
                

                # Fetch the attendance data from the database
                query = f"SELECT attendance.* FROM attendance JOIN timetable ON attendance.time BETWEEN timetable.start_time AND timetable.end_time WHERE timetable.start_time = '{start_time}' AND timetable.end_time = '{end_time}' AND attendance.day = timetable.day_of_week AND timetable.day_of_week = '{day}' AND attendance.Division = timetable.division AND timetable.division = '{subject_id}'"
                cursor.execute(query)
                data = cursor.fetchall()

                # Prompt the user to enter the name of the CSV file
                file_name = simpledialog.askstring("Save Attendance Data", "Enter file name:")
                if file_name:
                    file_path = os.path.join(os.path.expanduser("~"), "Downloads", file_name + ".csv")
                    with open(file_path, "w", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerows(data)
                    messagebox.showinfo("Attendance Data Saved", f"Attendance data saved to {file_path}")
                    shutil.move(file_path, os.path.join(os.path.expanduser("~"), "Downloads"))
                conn.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    def get_cursor(self,event=""):
        cursor_row=self.Attendance_table.focus()
        content=self.Attendance_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dept.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_time.set(rows[5])
        self.var_atten_attendance.set(rows[6])


if __name__ == "__main__":
    root= Tk()
    obj = Attendance(root)
    root.mainloop()