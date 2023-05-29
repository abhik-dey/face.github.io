from tkinter import *
from tkinter import messagebox
from main import Face_recognition_system
from face import Face_recognition_system1
import ast

root=Tk()
root.title("Login")
root.geometry("925x500+200+100")
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    file=open("datasheet.txt","r")
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    
    username_prefix=username[:2]


    if username in r.keys() and username_prefix == "20" and password==r[username]:
            new_window=Toplevel(root)
            app=Face_recognition_system(new_window)

    else:
        new_window=Toplevel(root)
        app=Face_recognition_system1(new_window)
#------------------------------------------------------
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry("925x500+200+100")
    window.focus_force()
    window.grab_set()
    window.configure(bg="#fff")
    window.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()

        if password==confirm_password:
            try:
                file=open("datasheet.txt","r+",newline="\n")
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open("datasheet.txt","w",newline="\n")
                w=file.write(str(r))

                messagebox.showinfo("Signup","Succesfully sign up")
                window.destroy()

            except:
                file=open("datasheet.txt","w",newline="\n")
                pp=str({"username":"password"})
                file.write(pp)
                file.close()
        
        else:
            messagebox.showerror("Invalid","Both password should match")

    def sign():
        window.destroy()

    img= PhotoImage(file="signup.png")
    Label(window,image=img,border=0,bg="white").place(x=50,y=90)

    frame= Frame(window,width=350,height=390,bg="white")
    frame.place(x=480,y=50)

    heading=Label(frame,text="Sign Up",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
    heading.place(x=100,y=5)

    #############---------------------

    def on_enter(e):
        user.delete(0,"end")

    def on_leave(e):
        if user.get()=="":
            user.insert(0,"Username")

    user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
    user.place(x=30,y=80)
    user.insert(0,"Username")
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

    #############---------------------

    def on_enter(e):
        code.delete(0,"end")
        code.config(show="•")

    def on_leave(e):
        if code.get()=="":
            code.insert(0,"Password")

    code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
    code.place(x=30,y=150)
    code.insert(0,"Password")
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

    def toggle_pass():
        if code.cget('show') == '•': # password is hidden
            code.config(show='')
            eye_button1.config(image=hide_image1)
        else: # password is visible
            code.config(show='•')
            eye_button1.config(image=show_image1)

    show_image1 = PhotoImage(file="eye.png")
    hide_image1 = PhotoImage(file="hidden.png")
    eye_button1 = Button(frame, image=show_image1, command=toggle_pass,border=0,bg="white")
    eye_button1.place(x=285,y=150)

    #############---------------------

    def on_enter(e):
        confirm_code.delete(0,"end")
        confirm_code.config(show="•")

    def on_leave(e):
        if confirm_code.get()=="":
            confirm_code.insert(0,"Confirm Password")

    confirm_code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0,"Confirm Password")
    confirm_code.bind("<FocusIn>",on_enter)
    confirm_code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)

    def toggle_password():
        if confirm_code.cget('show') == '•': # password is hidden
            confirm_code.config(show='')
            eye_button.config(image=hide_image)
        else: # password is visible
            confirm_code.config(show='•')
            eye_button.config(image=show_image)

    show_image = PhotoImage(file="eye.png")
    hide_image = PhotoImage(file="hidden.png")
    eye_button = Button(frame, image=show_image, command=toggle_password,border=0,bg="white")
    eye_button.place(x=285,y=220)


    #-----------------------------------------

    Button(frame,width=39,pady=7,text="Sign up",bg="#57a1f8",fg="white",border=0,command=signup).place(x=35,y=300)
    label=Label(frame,text="Have an account?",fg="black",bg="white",font=("Microsoft Yahei UI Light",9))
    label.place(x=90,y=360)

    signin=Button(frame,width=6,text="Sign in",border=0,bg="white",fg="#57a1f8",cursor="hand2",command=sign)
    signin.place(x=200,y=360)

    window.mainloop()
#------------------------------------------------------

img=PhotoImage(file="login.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

#------------------------------------

def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")


user= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#------------------------------------

def on_enter(e):
    code.delete(0,"end")
    code.config(show="•")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")


code= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

def toggle_password():
        if code.cget('show') == '•': # password is hidden
            code.config(show='')
            eye_button.config(image=hide_image)
        else: # password is visible
            code.config(show='•')
            eye_button.config(image=show_image)

show_image = PhotoImage(file="eye.png")
hide_image = PhotoImage(file="hidden.png")
eye_button = Button(frame, image=show_image, command=toggle_password,border=0,bg="white")
eye_button.place(x=285,y=150)


############################################

Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=224)
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=290)

sign_up=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=signup_command)
sign_up.place(x=215,y=290)

root.mainloop()