from tkinter import *
from tkinter import messagebox
import tkinter

from serial.serialutil import PortNotOpenError
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
#3k04 DCM assignment 2 main program

global_.Commu=False

#welcome screeens
class Application(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.welcome()

    def welcome(self):                                                     #add in labels and buttons
        self.message=Label(self,text="Welcome",font=("Times New Roman",60))
        self.message.place(x=640,y=200)
        self.photo=PhotoImage(file="ch2n8.png")
        self.logo=Label(self,image=self.photo)
        self.logo.place(x=380,y=90)
        self.login=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.login["text"]="Login"
        self.login.place(x=400,y=500)
        self.register=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.register["text"]="Register"
        self.register.place(x=730,y=500)
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
        self.user=Label(self,text="username:",font=("Times New Roman",24))
        self.user.place(x=450,y=300)
        self.userE=Entry(self,font=("Times New Roman",24))
        self.userE.place(x=590,y=300)
        self.password=Label(self,text="password:",font=("Times New Roman",24))
        self.password.place(x=450,y=370)
        self.passwordE=Entry(self,font=("Times New Roman",24),show="*")
        self.passwordE.place(x=590,y=370)
        self.loginB=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.loginB["text"]="Login"
        self.loginB.place(x=565,y=550)
        self.loginB.bind("<Button-1>",self.loginPressed)
        self.back=Button(self,width=10,height=2,font=("Times New Roman",14))
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
        self.user=Label(self,text="username:",font=("Times New Roman",24))
        self.user.place(x=450,y=300)
        self.userE=Entry(self,font=("Times New Roman",24))
        self.userE.place(x=590,y=300)
        self.password=Label(self,text="password:",font=("Times New Roman",24))
        self.password.place(x=450,y=370)
        self.passwordE=Entry(self,font=("Times New Roman",24),show="*")
        self.passwordE.place(x=590,y=370)
        self.passwordC=Label(self,text="confirm password:",font=("Times New Roman",24))
        self.passwordC.place(x=340,y=440)
        self.passwordCE=Entry(self,font=("Times New Roman",24),show="*")
        self.passwordCE.place(x=590,y=440)
        self.registerB=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.registerB["text"]="Register"
        self.registerB.place(x=565,y=550)
        self.registerB.bind("<Button-1>",self.registerPressed)
        self.back=Button(self,width=10,height=2,font=("Times New Roman",14))
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
        self.AOO=Button(self,text="AOO",width=15,height=3,font=("Times New Roman",14))
        self.AOO.place(x=420,y=60)
        self.AAI=Button(self,text="AAI",width=15,height=3,font=("Times New Roman",14))
        self.AAI.place(x=710,y=60)
        self.VOO=Button(self,text="VOO",width=15,height=3,font=("Times New Roman",14))
        self.VOO.place(x=420,y=160)
        self.VVI=Button(self,text="VVI",width=15,height=3,font=("Times New Roman",14))
        self.VVI.place(x=710,y=160)
        self.DOO=Button(self,text="DOO",width=15,height=3,font=("Times New Roman",14))
        self.DOO.place(x=420,y=260)
        self.VOOR=Button(self,text="VOOR",width=15,height=3,font=("Times New Roman",14))
        self.VOOR.place(x=710,y=260)
        self.AOOR=Button(self,text="AOOR",width=15,height=3,font=("Times New Roman",14))
        self.AOOR.place(x=420,y=360)
        self.AAIR=Button(self,text="AAIR",width=15,height=3,font=("Times New Roman",14))
        self.AAIR.place(x=710,y=360)
        self.VVIR=Button(self,text="VVIR",width=15,height=3,font=("Times New Roman",14))
        self.VVIR.place(x=420,y=460)
        self.DOOR=Button(self,text="DOOR",width=15,height=3,font=("Times New Roman",14))
        self.DOOR.place(x=710,y=460)
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
        self.stat=Label(self,font=("Times New Roman",12))
        if(global_.Commu==0):
            self.stat['text']="Pacemaker Connection: not connected"
        else:
            self.stat['text']="Pacemaker Connection: COM"+str(global_.Commu)
        self.refresh=Button(self,text="Refresh",font=("Times New Roman",12))
        self.refresh.place(x=10,y=20)
        self.refresh.bind("<Button-1>",self.refreshPressed)
        self.stat.place(x=10,y=0)
    
    def refreshPressed(self,e):
        global_.Commu = checkConnect()
        if(global_.Commu==0):
            self.stat['text']="Pacemaker Connection: not connected"
        else:
            self.stat['text']="Pacemaker Connection: COM"+str(global_.Commu)

        
def serial_Communication(mode,LR,APW,VPW,VA,ARP,VRP,AA,RECOVT,RF,MSR,AVD,AT,REACT):
    if global_.Commu  == 3:
        ser = serial.Serial(port="COM3", baudrate=115200)
    elif global_.Commu  == 4:
        ser = serial.Serial(port="COM4", baudrate=115200)
    elif global_.Commu  == 5:
        ser = serial.Serial(port="COM5", baudrate=115200)
    else:
        raise PortNotOpenError
    Header = '<2B14H'
    if(AA=='OFF'):
        AA=0
    if(VA=='OFF'):
        VA=0
    sp = struct.pack(Header,0x16,0x55,mode,LR,APW,VPW,VA,ARP,VRP,AA,RECOVT,RF,MSR,AVD,AT,REACT)
    ser.write(sp)
    serialdata=ser.read(28)
    modeV=struct.unpack('H',serialdata[0:2])
    LRV = struct.unpack('H',serialdata[2:4])
    APWV = struct.unpack('H',serialdata[4:6])
    VPWV = struct.unpack('H',serialdata[6:8])
    VAV = struct.unpack('H',serialdata[8:10])
    ARPV = struct.unpack('H',serialdata[10:12])
    VRPV = struct.unpack('H',serialdata[12:14])
    AAV = struct.unpack('H',serialdata[14:16])
    RECOVTV = struct.unpack('H',serialdata[16:18])
    RFV = struct.unpack('H',serialdata[18:20])
    MSRV = struct.unpack('H',serialdata[20:22])
    AVDV = struct.unpack('H',serialdata[22:24])
    ATV = struct.unpack('H',serialdata[24:26])
    REACTV = struct.unpack('H',serialdata[26:28])
    if(modeV[0]==mode and LRV[0]==LR and APWV[0]==APW and VPWV[0]==VPW and VAV[0]==VAV and ARPV[0]==ARP and VRPV[0]==VRP 
       and AAV[0]==AA and RECOVTV[0]==RECOVT and RFV[0]==RF and MSRV[0]==MSR and AVDV[0]==AVD and ATV[0]==AT and REACTV[0]==REACT):
       return "Parameter set and store successfully"
    else:
        return "Some or all parameters did not store properly, check pacemaker version compatibility"
    

 #check if the DCM is connected to pacemaker   
def checkConnect():
    try:
        ser = serial.Serial(port="COM3", baudrate=115200)
        return 3
    except:
        try:
            ser = serial.Serial(port="COM4", baudrate=115200)
            return 4
        except:
            try:
                ser = serial.Serial(port="COM5", baudrate=115200)
                return 5
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
    root.geometry("1280x720+50+50")
    root.resizable(False, False)
    global_.cUser=global_.users[0]
    voo.VOOparameter(master=root)
    #Application(master=root)
    root.mainloop()
