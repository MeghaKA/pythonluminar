from tkinter import *
def init():
    root=Tk()
    tFrame=Frame(root)
    bFrame=Frame(root)

    tFrame.pack()
    bFrame.pack(side=BOTTOM)

    btn1=Button(tFrame,text="FirstButton",fg="green")
    btn2=Button(tFrame,text="SecondButton",fg="blue")
    btn3=Button(tFrame,text="ThirdButton",fg="yellow")
    btn4=Button(bFrame,text="FourthButton",fg="cyan")
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=BOTTOM)
    root.mainloop()