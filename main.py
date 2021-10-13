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
welcome.geometry("500x300+100+100")
login=Button(welcome)
login["text"]="Login"
login.pack()
register=Button(welcome)
register["text"]="Register"
register.pack()

login.bind("<Button-1>",loginPressed)
register.bind("<Button-1>",registerPressed)
welcome.mainloop()


def loginW():
    pass

def registerW():
    pass
