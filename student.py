from tkinter import *
import tkinter.font
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import os
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")


        #----------------variables-----------------
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_grad=StringVar()


        bg_img=Image.open(r"C:\Users\abhik dey\Desktop\Face recognition system\images\images.png")
        bg_img=bg_img.resize((1540,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1530,height=710)

        canvas = Canvas(self.root, width=1530, height=710)
        canvas.create_image(0, 0, image=self.photoimg, anchor="nw")
        canvas.pack()
        
        
        font = tkinter.font.Font(family="Allcan DEMO", size=30, weight="bold")
        title_lbl = Label(canvas, text="STUDENT MANAGEMENT SYSTEM",font=font, fg="white", bg="black")
        title_lbl.place(x=0, y=20, width=1380, height=45) 

        main_frame = Frame(canvas, bd=2)
        main_frame.place(x=0,y=80,width=1500, height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="light grey", relief=SOLID,text="Student Details",font=("Allcan DEMO",15, "bold"))
        Left_frame.place(x=10,y=10,width=670,height=580)

        
        Left_img=Image.open(r"C:\Users\abhik dey\Desktop\Face recognition system\images\smit.png")
        Left_img=Left_img.resize((660,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(Left_img)

        f_lbl_left=Label(Left_frame,image=self.photoimg_left)
        f_lbl_left.place(x=3,y=0,width=660,height=130)

        #current course
        current_frame=LabelFrame(Left_frame,bd=2, relief=RIDGE,text="Current course information",font=("Allcan DEMO",15, "bold"))
        current_frame.place(x=4,y=135,width=660,height=134)

        #department
        dept_label=Label(current_frame, text="Department",font=("Allcan DEMO",12, "bold"))
        dept_label.grid(row=0,column=2,padx=10)

        dept_combo=ttk.Combobox(current_frame,textvariable=self.var_dept,font=("Allcan DEMO",12, "bold"),state="readonly",width=20)
        dept_combo["values"]=("Select Department","Computer Science","AI and DS","IT","Civil","Mechanical","ECE","EEE")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_frame, text="Course",font=("Allcan DEMO",12, "bold"))
        course_label.grid(row=0,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("Allcan DEMO",12, "bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","Computer Application","Engineering and Architecture","Management and Bussiness Administration","Science")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_frame, text="Year",font=("Allcan DEMO",12, "bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("Allcan DEMO",12, "bold"),state="readonly",width=20)
        year_combo["values"]=("Select year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_frame, text="Semester",font=("Allcan DEMO",12, "bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("Allcan DEMO",12, "bold"),state="readonly",width=20)
        semester_combo["values"]=("Select semester","1","2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #graduation
        graduation_label=Label(current_frame, text="Graduation",font=("Allcan DEMO",12, "bold"))
        graduation_label.grid(row=2,column=0,padx=10,sticky=W)

        graduation_combo=ttk.Combobox(current_frame,textvariable=self.var_grad,font=("Allcan DEMO",12, "bold"),state="readonly",width=20)
        graduation_combo["values"]=("Select graduation","UG","PG")
        graduation_combo.current(0)
        graduation_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2, relief=RIDGE,text="Class student information",font=("Allcan DEMO",15, "bold"))
        class_student_frame.place(x=4,y=274,width=660,height=278)

        #student id
        studentId_label=Label(class_student_frame, text="Student ID",font=("Allcan DEMO",12, "bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Allcan DEMO",12, "bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame, text="Student Name",font=("Allcan DEMO",12, "bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Allcan DEMO",12, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame, text="Section",font=("Allcan DEMO",12, "bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Allcan DEMO",12, "bold"),state="readonly",width=18)
        class_div_combo["values"]=("Select section","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame, text="Roll No.",font=("Allcan DEMO",12, "bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Allcan DEMO",12, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame, text="Gender",font=("Allcan DEMO",12, "bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Allcan DEMO",12, "bold"),state="readonly",width=18)
        gender_combo["values"]=("Select gender","Male","Female","others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student_frame, text="DOB",font=("Allcan DEMO",12, "bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Allcan DEMO",12, "bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame, text="Email",font=("Allcan DEMO",12, "bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Allcan DEMO",12, "bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_student_frame, text="Phone No.",font=("Allcan DEMO",12, "bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Allcan DEMO",12, "bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_student_frame, text="Address",font=("Allcan DEMO",12, "bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Allcan DEMO",12, "bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher guide
        teacher_label=Label(class_student_frame, text="Teacher Guide",font=("Allcan DEMO",12, "bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Allcan DEMO",12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=7,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=7,column=1)

         #buttons frame
        btn_frame=LabelFrame(class_student_frame,bd=2, relief=RIDGE)
        btn_frame.place(x=4,y=200,width=648,height=29)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=LabelFrame(class_student_frame,bd=2, relief=RIDGE)
        btn_frame1.place(x=4,y=229,width=648,height=29)
        
        take_photo_btn=Button(btn_frame1,command=self.Generate_dataset,text="Take Photo Sample",width=29,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=29,font=("Allcan DEMO",12, "bold"),bg="grey",fg="white")
        update_photo_btn.grid(row=0,column=1)



        #right label frame
        right_frame=LabelFrame(main_frame,bd=2, relief=SOLID,text="Student Details",font=("Allcan DEMO",15, "bold"),bg="light grey")
        right_frame.place(x=690,y=10,width=660,height=580)

        Right_img=Image.open(r"C:\Users\abhik dey\Desktop\Face recognition system\images\smit.png")
        Right_img=Right_img.resize((660,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(Right_img)

        f_lbl_right=Label(right_frame,image=self.photoimg_right)
        f_lbl_right.place(x=3,y=0,width=650,height=130)

        #------------search system----------------
        search_frame=LabelFrame(right_frame,bd=2, relief=RIDGE,text="Search System",font=("Allcan DEMO",15, "bold"))
        search_frame.place(x=4,y=135,width=650,height=70)

        search_label=Label(search_frame, text="Search by",font=("Allcan DEMO",12, "bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("Allcan DEMO",12, "bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Registration no.","phone no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("Allcan DEMO",12, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("Allcan DEMO",10, "bold"),bg="grey",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("Allcan DEMO",10, "bold"),bg="grey",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # table frame
        table_frame=Frame(right_frame,bd=2, relief=RIDGE)
        table_frame.place(x=4,y=210,width=650,height=340)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","photo","graduation"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll no.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone no.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoStatus")
        self.student_table.heading("graduation",text="Graduation")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.column("graduation",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #-------------------function declaration-------------------------
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dept.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_grad.get()

                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #------------fetch data----------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #----------------get cursor---------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
        self.var_grad.set(data[15])

    #-------------update ------------
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s,Graduation=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_grad.get(),
                                                                                                                                                                                    self.var_std_id.get(),
                                                                                                                                                                                          
                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #--------------------delete------------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Abhik1@1dey",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #--------------reset------------------
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select section")
        self.var_roll.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.var_grad.set("Select graduation")

    #----------------generate data set or take photo samples-----------------------
    def Generate_dataset(self):
        try:
                def generate_dataset():
                    # Get the selected student ID from the dropdown
                    selected_id = student_id_dropdown.get()
                    folder_name = f"data/dataset_student_{selected_id}"
                    os.makedirs(folder_name, exist_ok=True)

                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()

                        if not ret:
                            break
                        if face_cropped(my_frame) is not None:
                            face = cv2.resize(face_cropped(my_frame), (500, 500))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                            #face=cv2.cvtColor(face, cv2.COLOR_BGR2RGB) 

                            file_name_path = f"{folder_name}/user.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("cropped face", face)

                            img_id += 1

                        if cv2.waitKey(1) == 13 or int(img_id) == 200:
                            break

                    cap.release()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Result", f"Generating data sets for student ID {selected_id} completed!!!")


                # Create a function to populate the student ID dropdown
                def populate_student_ids():
                    # Clear any existing values
                    student_id_dropdown['values'] = []

                    # Retrieve student IDs from the database
                    conn = mysql.connector.connect(host="localhost", user="root", password="Abhik1@1dey", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT Student_id FROM student")
                    student_ids = my_cursor.fetchall()

                    # Add student IDs to the dropdown menu
                    student_id_list = [str(student_id[0]) for student_id in student_ids]
                    student_id_dropdown['values'] = student_id_list

                    # Set the default value of the dropdown menu
                    if student_id_list:
                        student_id_dropdown.current(0)
                    



                # Initialize the Tkinter GUI
                root = Tk()
                root.title("Dataset Generation")
                root.geometry("400x200")

                # Create a label for the student ID dropdown
                student_id_label = Label(root, text="Select Student ID:")
                student_id_label.pack()

                # Create a dropdown to select the student ID
                student_id_dropdown = ttk.Combobox(root, width=20, state="readonly")
                student_id_dropdown.pack()
                student_id_dropdown.set("")

                # Populate the student ID dropdown with the student IDs from the database
                populate_student_ids()

                # Create a button to generate the dataset for the selected student ID
                generate_dataset_button = Button(root, text="Generate Dataset", command=generate_dataset)
                generate_dataset_button.pack()

                # Initialize the face classifier
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped


                cap = cv2.VideoCapture(1)

                root.mainloop()
                

        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root= Tk()
    obj = Student(root)
    root.mainloop()