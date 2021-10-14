from tkinter import *
from tkinter import messagebox
import tkinter
from user import *
import pickle

#get users list
try:
    users=pickle.loads(open('users.dat','rb'))
    count=users.length
except:
    users= []
    count=0

#welcome screeen


class Application(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.welcome()

    def welcome(self):
        self.message=Label(self,text="Welcome",font=("Times New Roman",30))
        self.message.pack()
        self.photo=PhotoImage(file="ch2n8.png")
        self.logo=Label(self,image=self.photo)
        self.logo.pack()
        self.login=Button(self,width=10,height=2)
        self.login["text"]="Login"
        self.login.place(x=200,y=400)
        self.register=Button(self,width=10,height=2)
        self.register["text"]="Register"
        self.register.place(x=420,y=400)

        self.login.bind("<Button-1>",self.loginPressed)
        self.register.bind("<Button-1>",self.registerPressed)
    
    def loginPressed(self,e):
        if(count==0):
            messagebox.showinfo("Message","There aren't any user created, please register")
        else:
            Login(master=self.master)
            self.destroy()

    def registerPressed(self,e):
        if(count==10):
            messagebox.showinfo("Message","There are already 10 users, please login")
        else:
            Register(master=self.master)
            self.destroy()


    def loginW(self):
        self.master.delete("all")

    def registerW(self):
        self.master.delete("all")


class Login(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.login()

    def login(self):
        pass

class Register(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.register()

    def register(self):
        pass


if __name__=='__main__':
    root=Tk()
    root.title("Pacemaker User Terminal")
    root.geometry("720x576+100+100")
    root.resizable(False, False)
    Application(master=root)
    root.mainloop()