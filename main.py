from tkinter import *
from tkinter import messagebox
import tkinter
from user import *
import pickle

#welcome screeen
global count
global users
global cUser

class Application(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.welcome()

    def welcome(self):
        self.message=Label(self,text="Welcome",font=("Times New Roman",30))
        self.message.place(x=400,y=100)
        self.photo=PhotoImage(file="ch2n8.png")
        self.logo=Label(self,image=self.photo)
        self.logo.place(x=100,y=30)
        self.login=Button(self,width=10,height=2)
        self.login["text"]="Login"
        self.login.place(x=200,y=350)
        self.register=Button(self,width=10,height=2)
        self.register["text"]="Register"
        self.register.place(x=420,y=350)
        self.login.bind("<Button-1>",self.loginPressed)
        self.register.bind("<Button-1>",self.registerPressed)
    
    def loginPressed(self,e):
        global count
        if(count==0):
            messagebox.showinfo("Message","There aren't any user created, please register")
        else:
            Login(master=self.master)
            self.destroy()

    def registerPressed(self,e):
        global count
        if(count==10):
            messagebox.showinfo("Message","There are already 10 users, please login")
        else:
            Register(master=self.master)
            self.destroy()

class Login(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.login()

    def login(self):
        self.user=Label(self,text="username:",font=("Times New Roman",18))
        self.user.place(x=200,y=200)
        self.userE=Entry(self,font=("Times New Roman",18))
        self.userE.place(x=300,y=200)
        self.password=Label(self,text="password:",font=("Times New Roman",18))
        self.password.place(x=200,y=270)
        self.passwordE=Entry(self,font=("Times New Roman",18),show="*")
        self.passwordE.place(x=300,y=270)
        self.loginB=Button(self,width=10,height=2)
        self.loginB["text"]="Login"
        self.loginB.place(x=320,y=400)
        self.loginB.bind("<Button-1>",self.loginPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def loginPressed(self,e):
        uEntered=self.userE.get()
        pwEntered=self.passwordE.get()
        for i in range(count):
            if(uEntered==users[i].getUN()):
                if(pwEntered==users[i].getPW()):
                    global cUser
                    cUser=users[i]
                    messagebox.showinfo("Message","logged in")

    def backPressed(self,e):
        Application(master=self.master)
        self.destroy()
        
class Register(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.register()

    def register(self):
        self.user=Label(self,text="username:",font=("Times New Roman",18))
        self.user.place(x=200,y=200)
        self.userE=Entry(self,font=("Times New Roman",18))
        self.userE.place(x=300,y=200)
        self.password=Label(self,text="password:",font=("Times New Roman",18))
        self.password.place(x=200,y=270)
        self.passwordE=Entry(self,font=("Times New Roman",18),show="*")
        self.passwordE.place(x=300,y=270)
        self.passwordC=Label(self,text="confirm password:",font=("Times New Roman",18))
        self.passwordC.place(x=120,y=340)
        self.passwordCE=Entry(self,font=("Times New Roman",18),show="*")
        self.passwordCE.place(x=300,y=340)
        self.registerB=Button(self,width=10,height=2)
        self.registerB["text"]="Register"
        self.registerB.place(x=320,y=400)
        self.registerB.bind("<Button-1>",self.registerPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
        
    def backPressed(self,e):
        Application(master=self.master)
        self.destroy()
    
    def registerPressed(self,e):
        if(self.passwordCE.get()==(self.passwordE.get())):
            cUser=User(self.userE.get(),self.passwordE.get())
            users.append(cUser)
            storeD()
            global count
            count+=1
            messagebox.showinfo("Message","User created")
    


def storeD():
    pickle.dump(users,open('users.dat','wb'))
    
if __name__=='__main__':
    #get users list
    try:
        users=pickle.load(open('users.dat','rb'))
        count=len(users)
    except:
        users= []
        count=0
    print(count)
    root=Tk()
    root.title("Pacemaker User Terminal")
    root.geometry("720x576+100+100")
    root.resizable(False, False)
    Application(master=root)
    root.mainloop()