from tkinter import messagebox
from tkinter import *
# from .frame_pg import *
root=Tk()
import mysql.connector
from dbconnectpgm.dbconnect import get_connection
def db_connect(username,password):
     print("inside..........")
     db=get_connection()
     cursor=db.cursor()
     try:

         cursor.execute(("select * from users where username=%s and password=%s"),(username,password))
         user=cursor.fetchone()
         return user
         # print(user)
         # id="1001"
         # name="test1"
         # usertest="test1"
         # userpwd="test2"
         # sql="insert into users(id,name,username,password)values('%s','%s','%s','%s')"% \
         #      (id,name,usertest,userpwd)
         # cursor.execute(sql)
         # db.commit()
     except Exception as e:
         print(e.args)



def authenticate_user():
       # print(uentry.get())
     # print("inside authenticate user")
    uname=uentry.get()
    pwd=pentry.get()
    user=db_connect(uname,pwd)
    if (user==None):
        messagebox.showerror("invalid user","Error")
    # print(uname,pwd)
    else:
        messagebox.showinfo("user successfully logged","User successfully logged")
        # init()
ulabel=Label(root,text="username")
plabel=Label(root,text="Password")
uentry=Entry(root)
pentry=Entry(root)
btn=Button(root,text="Login",command=authenticate_user)
ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(columnspan=2)
root.mainloop()




# select course from students groupby course having count(*)<1;