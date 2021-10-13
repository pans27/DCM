from tkinter import *
from tkinter import messagebox
from user import *
import pickle

def loginPressed(e):
    if(count==0):
        messagebox.showinfo("Message","There aren't any user created, please register")
    else:
        loginW()

def registerPressed(e):
    if(count==10):
        messagebox.showinfo("Message","There are already 10 users, please login")
    else:
        registerW()


#get users list
try:
    users=pickle.loads(open('users.dat','rb'))
    count=users.length
except:
    users= []
    count=0

#welcome screeen
welcome=Tk()
welcome.title("Pacemaker User Terminal")
welcome.geometry("500x400+100+100")
message=Label(welcome,text="Welcome",font=("Times New Roman",30))
message.pack()
global photo 
photo=PhotoImage(file="ch2n8.png")
logo=Label(welcome,image=photo)
logo.pack()
login=Button(welcome,width=10,height=2)
login["text"]="Login"
login.pack()
register=Button(welcome,width=10,height=2)
register["text"]="Register"
register.pack()

login.bind("<Button-1>",loginPressed)
register.bind("<Button-1>",registerPressed)
welcome.mainloop()


def loginW():
    pass

def registerW():
    pass
