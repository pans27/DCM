from tkinter import *
from tkinter import messagebox
import tkinter
from user import *
import pickle
import global_
import aoo
import voo
import aai
import vvi
import doo
import voor
import aoor
import aair
import vvir
import door
import serial
import struct
#Oct 31, 2021
#Author: Group 5
#3k04 DCM assignment 1 main program

global_.Commu=False

#welcome screeens
class Application(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.welcome()

    def welcome(self):                                                     #add in labels and buttons
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
    
    def loginPressed(self,e):                   #if there are accounts found on drive, go to login
        global count
        if(global_.count==0):
            messagebox.showinfo("Message","There aren't any user created, please register")
        else:
            Login(master=self.master)
            self.destroy()

    def registerPressed(self,e): #if there are less than 10 users, go to register
        global count
        if(global_.count==10):
            messagebox.showinfo("Message","There are already 10 users, please login")
        else:
            Register(master=self.master)
            self.destroy()

#login
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
        check=False #flag to see if a user was found
        uEntered=self.userE.get() #get username and password entered
        pwEntered=self.passwordE.get()
        for i in range(global_.count):  #check if the username match with the stored user
            if(uEntered==global_.users[i].getUN()): #if username found, check if password is correct
                if(pwEntered==global_.users[i].getPW()): #if correct, go to modes
                    global_.cUser=global_.users[i]
                    check=True
                    messagebox.showinfo("Message","logged in")
                    Connect(master=self.master)
                    Modes(master=self.master)
                    self.destroy()
        if(check==False):
            messagebox.showinfo("Message","The username or password is incorrect")

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
        if(self.userE.get()!="" and self.passwordE.get!=""):
            if(self.passwordCE.get()==(self.passwordE.get())): # check if confirm password and password matches
                check=FALSE
                if(global_.count==10):
                    messagebox.showinfo("Message","There are already 10 users, please login")
                else:
                    for i in range(global_.count): #check if the username already exist
                        if(self.userE.get()==global_.users[i].getUN()):
                            messagebox.showinfo("Message","Username already exist")
                            check=TRUE
                            break
                    if(check==FALSE and self.passwordE.get()==self.passwordCE.get()):
                        global_.cUser=User(self.userE.get(),self.passwordE.get())
                        global_.users.append(global_.cUser)
                        storeD()
                        global_.count+=1
                        prompt=messagebox.askquestion("Message","User created, log in?")
                        if(prompt=="yes"):
                            Connect(master=self.master)
                            Modes(master=self.master)
                            self.destroy()
            else:       
                messagebox.showinfo("Message","password does not match")
        else:
            messagebox.showinfo("Message","Fields cannot be empty")

#modes selection
class Modes(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.displaymodes()

    def displaymodes(self):
        self.AOO=Button(self,text="AOO",width=10,height=2)
        self.AOO.place(x=200,y=100)
        self.AAI=Button(self,text="AAI",width=10,height=2)
        self.AAI.place(x=420,y=100)
        self.VOO=Button(self,text="VOO",width=10,height=2)
        self.VOO.place(x=200,y=180)
        self.VVI=Button(self,text="VVI",width=10,height=2)
        self.VVI.place(x=420,y=180)
        self.DOO=Button(self,text="DOO",width=10,height=2)
        self.DOO.place(x=200,y=260)
        self.VOOR=Button(self,text="VOOR",width=10,height=2)
        self.VOOR.place(x=420,y=260)
        self.AOOR=Button(self,text="AOOR",width=10,height=2)
        self.AOOR.place(x=200,y=340)
        self.AAIR=Button(self,text="AAIR",width=10,height=2)
        self.AAIR.place(x=420,y=340)
        self.VVIR=Button(self,text="VVIR",width=10,height=2)
        self.VVIR.place(x=200,y=420)
        self.DOOR=Button(self,text="DOOR",width=10,height=2)
        self.DOOR.place(x=420,y=420)
        self.AOO.bind("<Button-1>",self.AOOPressed)
        self.AAI.bind("<Button-1>",self.AAIPressed)
        self.VOO.bind("<Button-1>",self.VOOPressed)
        self.VVI.bind("<Button-1>",self.VVIPressed)
        self.DOO.bind("<Button-1>",self.DOOPressed)
        self.VOOR.bind("<Button-1>",self.VOORPressed)
        self.AOOR.bind("<Button-1>",self.AOORPressed)
        self.AAIR.bind("<Button-1>",self.AAIRPressed)
        self.VVIR.bind("<Button-1>",self.VVIRPressed)
        self.DOOR.bind("<Button-1>",self.DOORPressed)
    
    def AOOPressed(self,e):
        aoo.AOOparameter(master=self.master)
        self.destroy()

    def AAIPressed(self,e):
        aai.AAIparameter(master=self.master)
        self.destroy() 
    
    def VOOPressed(self,e):
        voo.VOOparameter(master=self.master)
        self.destroy() 
    
    def VVIPressed(self,e):
        vvi.VVIparameter(master=self.master)
        self.destroy() 
    
    def DOOPressed(self,e):
        doo.DOOparameter(master=self.master)
        self.destroy()

    def VOORPressed(self,e):
        voor.VOORparameter(master=self.master)
        self.destroy() 
    
    def AOORPressed(self,e):
        aoor.AOORparameter(master=self.master)
        self.destroy() 
    
    def AAIRPressed(self,e):
        aair.AAIRparameter(master=self.master)
        self.destroy() 
    
    def VVIRPressed(self,e):
        vvir.VVIRparameter(master=self.master)
        self.destroy() 
    
    def DOORPressed(self,e):
        door.DOORparameter(master=self.master)
        self.destroy() 




class Connect(tkinter.Frame): # connect frame to be further implemented with serial communication
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=0,relheight=0.1,relwidth=1)
        self.connect()

    def connect(self):
        global_.Commu = checkConnect()

        self.stat=Label(self,text="Pacemaker Connection: port"+str(global_.Commu),font=("Times New Roman",12))
        self.stat.place(x=10,y=0)
        
def serial_Communication(mode, Lower_Rate, MSR, AV_Delay, ATR_Amplitude, VENT_Amplitude, ATR_Width,VENT_Width,VENT_Refractory, ATR_Refractory, Activity_Threshold,Reaction_Time, Response_Factor,Recovery_Time):
    if checkConnect() == 3:
        ser = serial.Serial(port="COM3", baudrate=115200)
    elif checkConnect() == 4:
        ser = serial.Serial(port="COM4", baudrate=115200)
    elif checkConnect() == 5:
        ser = serial.Serial(port="COM5", baudrate=115200)
    Header = '<2B14H'
    spk = struct.pack(Header,0x16,0x55,mode,Lower_Rate,ATR_Amplitude,VENT_Amplitude,ATR_Width,VENT_Width,
                      ATR_Refractory,VENT_Refractory,MSR,Reaction_Time,
                      Recovery_Time,Activity_Threshold,AV_Delay,Response_Factor)
    ser.write(spk)
    serialdata=ser.read()
    modeV=serialdata[0]
    LRV = serialdata[1:3]
    ATR_AV = serialdata[3:5]
    VENT_AV = serialdata[5:7]
    ATR_WV = serialdata[7:9]
    VENT_WV = serialdata[9:11]
    ATR_RV = serialdata[11:13]
    VENT_RV = serialdata[13:15]
    MSRV = serialdata[15:17]
    ReactionTV = serialdata[17:19]
    RecoveryTV = serialdata[19:21]
    ActTV = serialdata[21:23]
    AV_DV = serialdata[23:25]
    Response_FV = serialdata[25:27]
    

 #check if the DCM is connected to pacemaker   
def checkConnect():
    try:
        ser = serial.Serial(port="COM3", baudrate=115200)
        return 3
    except:
        try:
            ser = serial.Serial(port="COM5", baudrate=115200)
            return 5
        except:
            try:
                ser = serial.Serial(port="COM4", baudrate=115200)
                return 4
            except:
                return 0 # not connected

def storeD():
    pickle.dump(global_.users,open('users.dat','wb')) #store the list of users in user.dat
    
if __name__=='__main__':
    #get users list
    try:
        global_.users=pickle.load(open('users.dat','rb')) # read the file of users, if the file does not exist create empty list and the number of users=0
        global_.count=len(global_.users)
    except:
        global_.users= []
        global_.count=0
    print(global_.count)
    root=Tk()
    root.title("Pacemaker User Terminal") # create gui window and call application to display the welcome screen
    root.geometry("720x576+100+100")
    root.resizable(False, False)
    Application(master=root)
    root.mainloop()
