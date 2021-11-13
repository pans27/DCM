from tkinter import *
from tkinter import messagebox
import tkinter
from user import *
import pickle
#Oct 31, 2021
#Author: Group 5
#3k04 DCM assignment 1 main program

global count #number of users
global users #list of users
global cUser #the current user that logged in
global Commu #pacemaker connection
Commu=False

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
        if(count==0):
            messagebox.showinfo("Message","There aren't any user created, please register")
        else:
            Login(master=self.master)
            self.destroy()

    def registerPressed(self,e): #if there are less than 10 users, go to register
        global count
        if(count==10):
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
        global count
        global users
        check=False #flag to see if a user was found
        uEntered=self.userE.get() #get username and password entered
        pwEntered=self.passwordE.get()
        for i in range(count):  #check if the username match with the stored user
            if(uEntered==users[i].getUN()): #if username found, check if password is correct
                if(pwEntered==users[i].getPW()): #if correct, go to modes
                    global cUser
                    cUser=users[i]
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
        if(self.passwordCE.get()==(self.passwordE.get())): # check if confirm password and password matches
            check=FALSE
            global count
            if(count==10):
                messagebox.showinfo("Message","There are already 10 users, please login")
            else:
                for i in range(count): #check if the username already exist
                    if(self.userE.get()==users[i].getUN()):
                        messagebox.showinfo("Message","Username already exist")
                        check=TRUE
                        break
                if(check==FALSE and self.passwordE.get()==self.passwordCE.get()):
                    global cUser
                    cUser=User(self.userE.get(),self.passwordE.get())
                    users.append(cUser)
                    storeD()
                    count+=1
                    prompt=messagebox.askquestion("Message","User created, log in?")
                    if(prompt=="yes"):
                        Connect(master=self.master)
                        Modes(master=self.master)
                        self.destroy()
        else:       
            messagebox.showinfo("Message","password does not match")

<<<<<<< Updated upstream
#modes selection
=======
# Display pacemaker modes
>>>>>>> Stashed changes
class Modes(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1) # create new window
        self.displaymodes() 

# display buttons of pacemaker modes
    def displaymodes(self):
        self.AOO=Button(self,text="AOO",width=10,height=2)
        self.AOO.place(x=420,y=100)
        self.AAI=Button(self,text="AAI",width=10,height=2)
        self.AAI.place(x=620,y=100)
        self.VOO=Button(self,text="VOO",width=10,height=2)
        self.VOO.place(x=420,y=180)
        self.VVI=Button(self,text="VVI",width=10,height=2)
        self.VVI.place(x=620,y=180)
        self.DOO=Button(self,text="DOO",width=10,height=2)
        self.DOO.place(x=420,y=260)
        self.VOOR=Button(self,text="VOOR",width=10,height=2)
        self.VOOR.place(x=620,y=260)
        self.AOOR=Button(self,text="AOOR",width=10,height=2)
        self.AOOR.place(x=420,y=340)
        self.AAIR=Button(self,text="AAIR",width=10,height=2)
        self.AAIR.place(x=620,y=340)
        self.VVIR=Button(self,text="VVIR",width=10,height=2)
        self.VVIR.place(x=420,y=420)
        self.DOOR=Button(self,text="DOOR",width=10,height=2)
        self.DOOR.place(x=620,y=420)
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
    
    # handle the case when AOO button is pressed
    def AOOPressed(self,e):
        AOOparameter(master=self.master)
        self.destroy()

    def AAIPressed(self,e):
        AAIparameter(master=self.master)
        self.destroy() 
    
    def VOOPressed(self,e):
        VOOparameter(master=self.master)
        self.destroy() 
    
    def VVIPressed(self,e):
        VVIparameter(master=self.master)
        self.destroy() 
    
    def DOOPressed(self,e):
         DOOparameter(master=self.master)
         self.destroy()

    def VOORPressed(self,e):
         VOORparameter(master=self.master)
         self.destroy() 
    
    def AOORPressed(self,e):
         AOORparameter(master=self.master)
         self.destroy() 
    
    def AAIRPressed(self,e):
         AAIRparameter(master=self.master)
         self.destroy() 
    
    def VVIRPressed(self,e):
         VVIRparameter(master=self.master)
         self.destroy() 
    
    def DOORPressed(self,e):
         DOORparameter(master=self.master)
         self.destroy() 

 # diplay the page to change AOO parameters   
class AOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1) # display new window
        self.write_aoo_parameters()

<<<<<<< Updated upstream
    def write_aoo_parameters(self): #creating labels and entry fields
=======
# add buttons and enter box
    def write_aoo_parameters(self):
>>>>>>> Stashed changes
        global cUser
        self.message=Label(self,text="AOO Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=380,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aoo.getLRL())
        self.l_r_l_E.place(x=630,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=380,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aoo.getURL())
        self.u_r_l_E.place(x=630,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=380,y=240)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aoo.getAA())
        self.a_a_E.place(x=630,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=380,y=280)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aoo.getAPW())
        self.a_p_w_E.place(x=630,y=280)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
<<<<<<< Updated upstream
    
    def confirmPressed(self,e): # check each parameter to see if there is an error, keep track of the errors
=======

 # click to save current parameter data and check if the data type is right 
 # and is in the acceptable range   
    def confirmPressed(self,e):
>>>>>>> Stashed changes
        errors=0
        text=""
        try:
            cUser.aoo.setLRL(self.lrl.get())
            self.lrl.set(cUser.aoo.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.aoo.setURL(self.url.get())
            self.url.set(cUser.aoo.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.aoo.setAA(self.aa.get())
            self.aa.set(cUser.aoo.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0.5 and 7.0\n"
            errors+=1
        try:
            cUser.aoo.setAPW(self.apw.get())
            self.apw.set(cUser.aoo.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 0.1 and 1.9\n"
            errors+=1
        if(errors==0): #print out errors ifthere are any, store the changes without error to hard drive
            messagebox.showinfo("Message","Changes saved")
            storeD()
        elif(errors<4):
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Other values are saved")
            storeD()
        else:
            messagebox.showinfo("Message","There are "+str(errors)+" error(S):\n"+text)

# clear all the data in the enter box
    def clearPressed(self,e):
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?") # set all entry field to show the parameter stored
        if(prompt=='yes'):
            self.lrl.set(cUser.aoo.getLRL())
            self.url.set(cUser.aoo.getURL())
            self.aa.set(cUser.aoo.getAA())
            self.apw.set(cUser.aoo.getAPW())

# back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
              
class VOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_voo_parameters()

    def write_voo_parameters(self):
        self.message=Label(self,text="VOO Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=380,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.voo.getLRL())
        self.l_r_l_E.place(x=630,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=380,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.voo.getURL())
        self.u_r_l_E.place(x=630,y=200)
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=380,y=240)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.voo.getVA())
        self.v_a_E.place(x=630,y=240)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=380,y=280)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.voo.getVPW())
        self.v_p_w_E.place(x=630,y=280)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        errors=0
        text=""
        try:
            cUser.voo.setLRL(self.lrl.get())
            self.lrl.set(cUser.voo.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.voo.setURL(self.url.get())
            self.url.set(cUser.voo.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.voo.setVA(self.va.get())
            self.va.set(cUser.voo.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0.5 and 7.0\n"
            errors+=1
        try:
            cUser.voo.setVPW(self.vpw.get())
            self.vpw.set(cUser.voo.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        if(errors==0):
            messagebox.showinfo("Message","Changes saved")
            storeD()
        elif(errors<4):
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Other values are saved")
            storeD()
        else:
            messagebox.showinfo("Message","There are "+str(errors)+" error(S):\n"+text)
    
    def clearPressed(self,e):
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.voo.getLRL())
            self.url.set(cUser.voo.getURL())
            self.va.set(cUser.voo.getVA())
            self.vpw.set(cUser.voo.getVPW())

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
        
class VVIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_vvi_parameters()

    def write_vvi_parameters(self):
        self.message=Label(self,text="VVI Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)

        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.vvi.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()

        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.vvi.getURL())
        self.u_r_l_E.place(x=900,y=160)

        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=200)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=350,y=200)

        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=650,y=200)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=900,y=200)

        #Ventricular Sensitivity
        self.v_s=Label(self,text="Ventricular Sensitivity :",font=("Times New Roman",14))
        self.v_s.place(x=100,y=240)
        self.vs=StringVar()
        self.v_s_E=Entry(self,textvariable=self.vs,font=("Times New Roman",14))
        self.vs.set(cUser.vvi.getVRP())
        self.v_s_E.place(x=350,y=240)

        self.v_r_p=Label(self,text="VRP :",font=("Times New Roman",14))
        self.v_r_p.place(x=650,y=240)
        self.vrp=StringVar()
        self.vrp_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",14))
        self.vrp.set(cUser.vvi.getVRP())
        self.vrp_E.place(x=900,y=240)
         #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis :",font=("Times New Roman",14))
        self.hysteresis.place(x=100,y=280)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",14))
        self.hys.set(cUser.aai.getARP())
        self.hysteresis_E.place(x=350,y=280)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing :",font=("Times New Roman",14))
        self.r_s.place(x=650,y=280)
        self.rates=StringVar()
        self.r_s_E=Entry(self,textvariable=self.rates,font=("Times New Roman",14))
        self.rates.set(cUser.aai.getARP())
        self.r_s_E.place(x=900,y=280)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        errors=0
        text=""
        try:
            cUser.vvi.setLRL(self.lrl.get())
            self.lrl.set(cUser.vvi.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.vvi.setURL(self.url.get())
            self.url.set(cUser.vvi.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.vvi.setVA(self.va.get())
            self.va.set(cUser.vvi.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0.5 and 7.0\n"
            errors+=1
        try:
            cUser.vvi.setVPW(self.vpw.get())
            self.vpw.set(cUser.vvi.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        try:
            cUser.vvi.setVRP(self.vrp.get())
            self.vrp.set(cUser.vvi.getVRP())
        except TypeError:
            text=text+"VRP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VRP must be between 150 and 500\n"
            errors+=1    
        if(errors==0):
            messagebox.showinfo("Message","Changes saved")
            storeD()
        elif(errors<5):
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Other values are saved")
            storeD()
        else:
            messagebox.showinfo("Message","There are "+str(errors)+" error(S):\n"+text)

    
    def clearPressed(self,e):
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.vvi.getLRL())
            self.url.set(cUser.vvi.getURL())
            self.va.set(cUser.vvi.getVA())
            self.vpw.set(cUser.vvi.getVPW())
            self.vrp.set(cUser.vvi.getVRP())

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
             
class AAIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aai_parameters()

    def write_aai_parameters(self):
        self.message=Label(self,text="AAI Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)

        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)

        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)

        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=200)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=350,y=200)

        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=650,y=200)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=900,y=200)

        self.a_r_p=Label(self,text="ARP :",font=("Times New Roman",14))
        self.a_r_p.place(x=100,y=240)
        self.arp=StringVar()
        self.arp_E=Entry(self,textvariable=self.arp,font=("Times New Roman",14))
        self.arp.set(cUser.aai.getARP())
        self.arp_E.place(x=350,y=240)

        #PVARP
        self.p_v_a_r_p=Label(self,text="PVARP :",font=("Times New Roman",14))
        self.p_v_a_r_p.place(x=650,y=240)
        self.pvarp=StringVar()
        self.p_v_a_r_p_E=Entry(self,textvariable=self.pvarp,font=("Times New Roman",14))
        self.pvarp.set(cUser.aai.getARP())
        self.p_v_a_r_p_E.place(x=900,y=240)

         #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis :",font=("Times New Roman",14))
        self.hysteresis.place(x=100,y=280)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",14))
        self.hys.set(cUser.aai.getARP())
        self.hysteresis_E.place(x=350,y=280)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing :",font=("Times New Roman",14))
        self.r_s.place(x=650,y=280)
        self.rates=StringVar()
        self.r_s_E=Entry(self,textvariable=self.rates,font=("Times New Roman",14))
        self.rates.set(cUser.aai.getARP())
        self.r_s_E.place(x=900,y=280)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()

class DOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_doo_parameters()

    def write_doo_parameters(self):
        self.message=Label(self,text="DOO Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=380,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=630,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=380,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=630,y=200)
        #Fixed AV Dealy
        self.fixed_AV_delay=Label(self,text="Fixed AV Dealy :",font=("Times New Roman",14))
        self.fixed_AV_delay.place(x=380,y=240)
        self.fad=StringVar()
        self.fixed_AV_delay_E=Entry(self,textvariable=self.fad,font=("Times New Roman",14))
        self.fad.set(cUser.aai.getAA())
        self.fixed_AV_delay_E.place(x=630,y=240)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=380,y=280)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=630,y=280)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=380,y=320)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=630,y=320)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=380,y=360)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=630,y=360)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=380,y=400)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=630,y=400)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()

<<<<<<< Updated upstream
class Connect(tkinter.Frame): # connect frame to be further implemented with serial communication
=======
class VOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_voor_parameters()

    def write_voor_parameters(self):
        self.message=Label(self,text="VOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=200)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aai.getAA())
        self.m_s_r_E.place(x=350,y=200)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=650,y=200)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=900,y=200)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=240)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=350,y=240)
         #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=650,y=240)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvi.getVPW())
        self.a_t_E.place(x=900,y=240)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=100,y=280)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvi.getVPW())
        self.r_t_E.place(x=350,y=280)
        #Response Factor
        self.r_f=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_f.place(x=650,y=280)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvi.getVPW())
        self.r_f_E.place(x=900,y=280)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=100,y=320)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvi.getVPW())
        self.recovery_time_E.place(x=350,y=320)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()

class AOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aoor_parameters()

    def write_aoor_parameters(self):
        self.message=Label(self,text="AOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=200)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aai.getAA())
        self.m_s_r_E.place(x=350,y=200)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=650,y=200)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=900,y=200)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=240)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=350,y=240)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=650,y=240)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvi.getVPW())
        self.a_t_E.place(x=900,y=240)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=100,y=280)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvi.getVPW())
        self.r_t_E.place(x=350,y=280)
        #Response Factor
        self.r_f=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_f.place(x=650,y=280)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvi.getVPW())
        self.r_f_E.place(x=900,y=280)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=100,y=320)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvi.getVPW())
        self.recovery_time_E.place(x=350,y=320)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()

class AAIRparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aair_parameters()

    def write_aair_parameters(self):
        self.message=Label(self,text="AAIR Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=120)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=120)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=120)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=120)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=160)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aai.getAA())
        self.m_s_r_E.place(x=350,y=160)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=650,y=160)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=900,y=160)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=200)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=350,y=200)
        #Atrial Sensitivity
        self.a_s=Label(self,text="Atrial Sensitivity :",font=("Times New Roman",14))
        self.a_s.place(x=650,y=200)
        self.ats=StringVar()
        self.a_s_E=Entry(self,textvariable=self.ats,font=("Times New Roman",14))
        self.ats.set(cUser.aai.getARP())
        self.a_s_E.place(x=900,y=200)
        #ARP
        self.a_r_p=Label(self,text="ARP :",font=("Times New Roman",14))
        self.a_r_p.place(x=100,y=240)
        self.arp=StringVar()
        self.a_r_p_E=Entry(self,textvariable=self.arp,font=("Times New Roman",14))
        self.arp.set(cUser.aai.getARP())
        self.a_r_p_E.place(x=350,y=240)
        #PVARP
        self.p_v_a_r_p=Label(self,text="PVARP :",font=("Times New Roman",14))
        self.p_v_a_r_p.place(x=650,y=240)
        self.pvarp=StringVar()
        self.p_v_a_r_p_E=Entry(self,textvariable=self.pvarp,font=("Times New Roman",14))
        self.pvarp.set(cUser.aai.getARP())
        self.p_v_a_r_p_E.place(x=900,y=240)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis :",font=("Times New Roman",14))
        self.hysteresis.place(x=100,y=280)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",14))
        self.hys.set(cUser.aai.getARP())
        self.hysteresis_E.place(x=350,y=280)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing :",font=("Times New Roman",14))
        self.r_s.place(x=650,y=280)
        self.rates=StringVar()
        self.r_s_E=Entry(self,textvariable=self.rates,font=("Times New Roman",14))
        self.rates.set(cUser.aai.getARP())
        self.r_s_E.place(x=900,y=280)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=100,y=320)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvi.getVPW())
        self.a_t_E.place(x=350,y=320)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=650,y=320)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvi.getVPW())
        self.r_t_E.place(x=900,y=320)
        #Response Factor
        self.r_f=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_f.place(x=100,y=360)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvi.getVPW())
        self.r_f_E.place(x=350,y=360)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=650,y=360)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvi.getVPW())
        self.recovery_time_E.place(x=900,y=360)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()


class VVIRparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_vvir_parameters()

    def write_vvir_parameters(self):
        self.message=Label(self,text="VVIR Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=200)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aai.getAA())
        self.m_s_r_E.place(x=350,y=200)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=650,y=200)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=900,y=200)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=240)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=350,y=240)
        #Ventricular Sensitivity
        self.v_s=Label(self,text="Ventricular Sensitivity :",font=("Times New Roman",14))
        self.v_s.place(x=650,y=240)
        self.vs=StringVar()
        self.v_s_E=Entry(self,textvariable=self.vs,font=("Times New Roman",14))
        self.vs.set(cUser.vvi.getVRP())
        self.v_s_E.place(x=900,y=240)
        #VRP
        self.v_r_p=Label(self,text="VRP :",font=("Times New Roman",14))
        self.v_r_p.place(x=100,y=280)
        self.vrp=StringVar()
        self.vrp_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",14))
        self.vrp.set(cUser.vvi.getVRP())
        self.vrp_E.place(x=350,y=280)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis :",font=("Times New Roman",14))
        self.hysteresis.place(x=650,y=280)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",14))
        self.hys.set(cUser.aai.getARP())
        self.hysteresis_E.place(x=900,y=280)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing :",font=("Times New Roman",14))
        self.r_s.place(x=100,y=320)
        self.rates=StringVar()
        self.r_s_E=Entry(self,textvariable=self.rates,font=("Times New Roman",14))
        self.rates.set(cUser.aai.getARP())
        self.r_s_E.place(x=350,y=320)
         #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=650,y=320)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvi.getVPW())
        self.a_t_E.place(x=900,y=320)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=100,y=360)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvi.getVPW())
        self.r_t_E.place(x=350,y=360)
        #Response Factor
        self.r_f=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_f.place(x=650,y=360)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvi.getVPW())
        self.r_f_E.place(x=900,y=360)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=100,y=400)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvi.getVPW())
        self.recovery_time_E.place(x=350,y=400)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()

class DOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_door_parameters()

    def write_door_parameters(self):
        self.message=Label(self,text="DOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=200)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aai.getAA())
        self.m_s_r_E.place(x=350,y=200)
        #Fixed AV Dealy
        self.fixed_AV_delay=Label(self,text="Fixed AV Dealy :",font=("Times New Roman",14))
        self.fixed_AV_delay.place(x=650,y=200)
        self.fad=StringVar()
        self.fixed_AV_delay_E=Entry(self,textvariable=self.fad,font=("Times New Roman",14))
        self.fad.set(cUser.aai.getAA())
        self.fixed_AV_delay_E.place(x=900,y=200)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=350,y=240)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=650,y=240)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=900,y=240)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=350,y=280)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=650,y=280)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=900,y=280)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=100,y=320)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvi.getVPW())
        self.a_t_E.place(x=350,y=320)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=650,y=320)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvi.getVPW())
        self.r_t_E.place(x=900,y=320)
        #Response Factor
        self.r_f=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_f.place(x=100,y=360)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvi.getVPW())
        self.r_f_E.place(x=350,y=360)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=650,y=360)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvi.getVPW())
        self.recovery_time_E.place(x=900,y=360)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
class Connect(tkinter.Frame):
>>>>>>> Stashed changes
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=0,relheight=0.1,relwidth=1)
        self.connect()

    def connect(self):
        global Commu
        self.stat=Label(self,text="Pacemaker Connection: "+str(Commu),font=("Times New Roman",12))
        self.stat.place(x=10,y=0)
        self.num=Label(self,text="Pacemaker Number:",font=("Times New Roman",12))
        self.num.place(x=10,y=20)
    
# def serial_Communication():
# 	if(Commu == true):
# 		messagebox.showinfo("The pacemaker is successfully connected")
# 	else:
# 		messagebox.showinfo("Connection failed, please try again")

def storeD():
    pickle.dump(users,open('users.dat','wb')) #store the list of users in user.dat
    
if __name__=='__main__':
    #get users list
    try:
        users=pickle.load(open('users.dat','rb')) # read the file of users, if the file does not exist create empty list and the number of users=0
        count=len(users)
    except:
        users= []
        count=0
    print(count)
    root=Tk()
<<<<<<< Updated upstream
    root.title("Pacemaker User Terminal") # create gui window and call application to display the welcome screen
    root.geometry("720x576+100+100")
=======
    root.title("Pacemaker User Terminal")
    root.geometry("1200x576+100+100")
>>>>>>> Stashed changes
    root.resizable(False, False)
    Application(master=root)
    root.mainloop()
