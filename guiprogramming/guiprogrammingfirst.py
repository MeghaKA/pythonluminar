#tkinter
from tkinter import *

root=Tk()
root.title("main window")
label1=Label(root,text="username")
label2=Label(root,text="emailaddress")
label3=Label(root,text="password")
entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
root.mainloop()
#puropose-


#code for tkinter install
#sudo apt-get install python3-tk