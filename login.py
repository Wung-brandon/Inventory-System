from tkinter import *
from tkinter import messagebox
import mysql.connector
#from PIL import ImageTk


root = Tk()
root.title("Login Page")
root.geometry('400x600')
root.config(bg='firebrick2')
#bgimage = ImageTk.PhotoImage(file=r"C:\Users\WK. BRANDON\Desktop\images\data3.jpg")
#bglabel = Label(root,image=bgimage)
#bglabel.pack()
#def enter(event):
 #   if user_entry.get() == 'Username':
   #     user_entry.delete(0,END)

def forgot():
    def submit():
        if userlabel_entry.get() == '' or newpasswordlabel_entry.get() == '' or confirmpasswordlabel_entry.get() == '':
            messagebox.showerror('Error','All fields are required',parent=top)
        elif newpasswordlabel_entry.get() != confirmpasswordlabel_entry.get():
            messagebox.showerror('Error','Password mismatch',parent=top)
        else:
            mydb = mysql.connector.connect(host='localhost', user='root', password='Cwbetrand29',database='userdata')
            mycursor = mydb.cursor()
            query = 'select * from data where Username=%s'
            mycursor.execute(query,(userlabel_entry.get(),))
            #fetching each row to check if the user is already in the database
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error',"User doesn't exists ",parent=top)
                #update password and alse change it in the database
            else:
                query = 'update data set Password=%s where username=%s'  #must put the where username=%s if not all the records will be updated
                mycursor.execute(query,(newpasswordlabel_entry.get(),userlabel_entry.get()))
                mydb.commit()
                mydb.close()
                messagebox.showinfo('Success','Password is reset successfully. Please login with your new password',parent=top)
                top.destroy()
                
    top = Toplevel()
    top.title("Change Password")
    top.geometry('400x600')
    top.config(bg='firebrick2')
    
    reset = Label(top,text="RESET PASSWORD",font=('ariel',15,'bold'),bg='firebrick2',fg='white')
    reset.pack()
    
    usernamelabel = Label(top,text='Username:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
    usernamelabel.place(x=10,y=80)
    userlabel_entry = Entry(top,width=40,fg='magenta2',font=('ariel',12,'bold'),bd=0)
    userlabel_entry.place(x=15,y=120)
          
    newpasswordlabel = Label(top,text='New Password:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
    newpasswordlabel.place(x=10,y=170)
    newpasswordlabel_entry = Entry(top,width=40,fg='magenta2',font=('ariel',12,'bold'),bd=0)
    newpasswordlabel_entry.place(x=15,y=210)
    
    confirmpasswordlabel = Label(top,text='Confirm Password:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
    confirmpasswordlabel.place(x=10,y=260)
    confirmpasswordlabel_entry = Entry(top,width=40,fg='magenta2',font=('ariel',12,'bold'),bd=0)
    confirmpasswordlabel_entry.place(x=14,y=300)
    
    submitbtn = Button(top,text="Submit",bg='white',activebackground='white',command=submit,
                   fg='firebrick2',height=2,bd=0,activeforeground='firebrick2',width=15,cursor='hand2',font=('Arial',15,'bold'))
    submitbtn.place(x=110,y=410)
    
    
    top.mainloop()    
       
def my_show():
    if showvariable.get() == 1:
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

def signin():
    root.destroy()
    import signIn

def log_in():
    if user_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('error','All fields are required')
        return
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='Cwbetrand29',database='userdata')
            mycursor = mydb.cursor()
            
        except:
            messagebox.showerror('Error','Connection error. Please try again')
            return
        
    query = 'use userdata'
    mycursor.execute(query)
    query = 'select * from data where username=%s and password=%s'
    mycursor.execute(query,(user_entry.get(),password_entry.get()))
    row = mycursor.fetchone()
    #checking if the user used the same password and username in the signin and login page if not display an error message
    if row == None:
        messagebox.showerror('Error','Invalid user or password')
    else:
        messagebox.showinfo('Success','Login successful')
        root.destroy()
        import inventory
             
login_label = Label(root,text='Login',font=('ariel',20,'bold'),fg='white',bg='firebrick2')
login_label.place(x=160,y=70)

username_label = Label(root,text='Username:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
username_label.place(x=10,y=140)

user_entry = Entry(root,font=('times new roman',15,'bold'),width=35)
user_entry.place(x=15,y=170)

#user_entry.insert(0,'Username')
#user_entry.bind('<FocusIn>',enter)

password_label = Label(root,text='Password:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
password_label.place(x=10,y=220)

passwordVar = StringVar()
password_entry = Entry(root,show='*',textvariable=passwordVar,font=('times new roman',15,'bold'),width=35)
password_entry.place(x=15,y=250)

showvariable = IntVar(value=0)
showcheck = Checkbutton(root,bd=0,bg='firebrick2',activebackground='firebrick2',
                        variable=showvariable,onvalue=1,offvalue=0,command=my_show)
showcheck.place(x=15,y=295)
showpassword = Label(root,text='Show Password',font=10,fg='white',bg='firebrick2')
showpassword.place(x=36,y=293)

#loginbtn = Button(root,text='Login',font=('arial',15,'bold'),fg='firebrick2',bg='white',cursor='hand2',bd=5,relief=SUNKEN,
 #                 activebackground='firebrick2',width=7,height=2,activeforeground='white')
#loginbtn.place(x=150,y=380)
loginbtn = Button(root,text="Login",bg='white',activebackground='white',
                   fg='firebrick2',command=log_in,height=2,bd=0,activeforeground='firebrick2',width=15,cursor='hand2',font=('Arial',15,'bold'))
loginbtn.place(x=110,y=380)

forgetbtn = Button(root,text='Forgot Password?',fg='blue',bg='firebrick2',
                  activebackground='firebrick2',command=forgot,activeforeground='white',cursor='hand2',
                   font=('ariel',10),bd=0)
forgetbtn.place(x=270,y=293)

signuplabel = Label(root,text="Don't Have An Account?",fg='white',
                    bg='firebrick2',font=('arial',10))
signuplabel.place(x=90,y=490)

newaccountlabel = Button(root,text="Create New One",font=('ariel',10,'bold underline'),fg='blue',cursor='hand2',
                    bg='firebrick2',command=signin,activeforeground='blue',bd=0,activebackground='firebrick2')
newaccountlabel.place(x=240,y=490)

root.mainloop()