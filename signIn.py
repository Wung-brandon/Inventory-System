from tkinter import *
from tkinter import messagebox
import mysql.connector



def login():
    root.destroy()
    import login
#function to clear all entry fields after registration
def clear():
    email_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    confirm_password_entry.delete(0,END)
    check.set(0)
    
def connect_database():
    if username_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '' or confirm_password_entry.get() == '':
        messagebox.showerror('Error','All fields are required')
    elif password_entry.get() != confirm_password_entry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif '@' not in email_entry.get() or 'gmail.com' not in email_entry.get():
        messagebox.showerror('Error','Invalid email address')
    #elif 'gmail.com' not in email_entry.get():
     #   messagebox.showerror('Error','Invalid email address')
    elif check.get() == 0:
        messagebox.showerror('Error','Please accept terms and conditions')
    #if this conditions are met then connect to the database
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='Cwbetrand29',database='userdata')
            mycursor = mydb.cursor()
        except:
            messagebox.showerror('Error','Connection error. Please try again')
            return
        
        try:
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data (id int auto_increment primary key not null,Email varchar(50),Username varchar(100),Password varchar(100),Confirm Password varchar(100))'
            mycursor.execute(query)
         #database already created in the try block statement sso we use the database userdata already created above
        except:
            mycursor.execute('use userdata')
            #query = 'SELECT * FROM data WHERE Email=%s and Username=%s and Password=%s '
        
        query = 'select * from data where Username=%s'
        mycursor.execute(query,(username_entry.get(),))
        #row = mycursor.fetchone()
        #checking if username already exists in the database then display an error
        if mycursor.fetchall():
            messagebox.showerror('Error','User already exists')
        else:
            #%s will be replaced by the entry field of the following email,username,password
            query = 'insert into data (Email, Username, Password) values (%s,%s,%s)'
            mycursor.execute(query,(email_entry.get(),username_entry.get(),password_entry.get()))
            #when inserting,updating or deleting data from the database we need to commit it to the database
            mydb.commit()
            mydb.close() # close the database connection after we commit
            messagebox.showinfo('Success','Registration is successfull')
            clear() #calling the function to clear all entries after registration is successful
            root.destroy()
            import login
            

            


root = Tk()
root.title("SignUp Page")
root.geometry('400x600')
root.config(bg='firebrick2')

accountlabel = Label(root,text="Create An Account",bg='firebrick2',activebackground='firebrick2',
                     font=('ariel',20,'bold'),activeforeground='white',fg='white')
accountlabel.pack(pady=5)

emailvar = StringVar()
email_label = Label(root,text='Email:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
email_label.place(x=10,y=90)
email_entry = Entry(root,textvariable=emailvar,font=('times new roman',15,'bold'),width=35)
email_entry.place(x=15,y=120)

usernamelabel = Label(root,text='Username:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
usernamelabel.place(x=10,y=160)
username_entry = Entry(root,font=('times new roman',15,'bold'),width=35)
username_entry.place(x=15,y=190)

password_label = Label(root,text='Password:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
password_label.place(x=10,y=230)
password_entry = Entry(root,font=('times new roman',15,'bold'),width=35)
password_entry.place(x=15,y=260)

confirm_password_label = Label(root,text='Confirm Password:',font=('ariel',15,'bold'),fg='white',bg='firebrick2')
confirm_password_label.place(x=10,y=300)
confirm_password_entry = Entry(root,font=('times new roman',15,'bold'),width=35)
confirm_password_entry.place(x=15,y=330)

check = IntVar()
#agree = Checkbutton(root,fg='white',bg='firebrick2',
 #                   activebackground='firebrick2',variable=check,activeforeground='white')
#agree.place(x=15,y=370)
agree = Checkbutton(root,bd=0,bg='firebrick2',activebackground='firebrick2',
                        variable=check)
agree.place(x=15,y=370)

terms = Label(root,text='I Agree To Terms & Conditions',fg='white',bg='firebrick2')
terms.place(x=35,y=370)

signupbtn = Button(root,text="Signup",bg='white',activebackground='white',command=connect_database,
                   fg='firebrick2',height=2,bd=0,activeforeground='firebrick2',width=15,cursor='hand2',font=('Arial',15,'bold'))
signupbtn.place(x=110,y=440)


already_label = Label(root,text="Already Have An Account?",fg='white',
                    bg='firebrick2',font=('arial',10))
already_label.place(x=90,y=540)

loglabel = Button(root,text="Login",font=('ariel',10,'bold underline'),fg='blue',cursor='hand2',
                    bg='firebrick2',command=login,activeforeground='blue',bd=0,activebackground='firebrick2')
loglabel.place(x=255,y=540)



root.mainloop()