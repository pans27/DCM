from tkinter import *
from tkinter import messagebox
import tkinter
from user import *
#from pacemaker_mode import *
import pickle

#welcome screeen
global count
global users
global cUser
global ifCommu;
global ifApp;


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
        global count
        global users
        uEntered=self.userE.get()
        pwEntered=self.passwordE.get()
        for i in range(count):
            if(uEntered==users[i].getUN()):
                if(pwEntered==users[i].getPW()):
                    global cUser
                    cUser=users[i]
                    messagebox.showinfo("Message","logged in")
                    Modes(master=self.master)
                    self.destroy()
            else:
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
        if(self.passwordCE.get()==(self.passwordE.get())):
            check=FALSE
            global count
            for i in range(count):
                if(self.userE.get()==users[i].getUN()):
                    messagebox.showinfo("Message","Username already exist")
                    check=TRUE
                    break
            if(check==FALSE):
                cUser=User(self.userE.get(),self.passwordE.get())
                users.append(cUser)
                storeD()
                count+=1
                prompt=messagebox.askquestion("Message","User created, log in?")
                if(prompt=="yes"):
                    Modes(master=self.master)
                    self.destroy()


class Modes(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
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
        # self.DOO.bind("<Button-1>",self.DOOPressed)
        # self.VOOR.bind("<Button-1>",self.VOORPressed)
        # self.AOOR.bind("<Button-1>",self.AOORPressed)
        # self.AAIR.bind("<Button-1>",self.AAIRPressed)
        # self.VVIR.bind("<Button-1>",self.VVIRPressed)
        # self.DOOR.bind("<Button-1>",self.DOORPressed)
    
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
    
    # def DOOPressed(self,e):
    #     DOOparameter(master=self.master)
    #     self.destroy()

    # def VOORPressed(self,e):
    #     VOORparameter(master=self.master)
    #     self.destroy() 
    
    # def AOORPressed(self,e):
    #     AOORparameter(master=self.master)
    #     self.destroy() 
    
    # def AAIRPressed(self,e):
    #     AAIRparameter(master=self.master)
    #     self.destroy() 
    
    # def VVIRPressed(self,e):
    #     VVIRparameter(master=self.master)
    #     self.destroy() 
    
    # def DOORPressed(self,e):
    #     VOORparameter(master=self.master)
    #     self.destroy() 
    
class AOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.write_aoo_parameters()

    def write_aoo_parameters(self):
        global cUser
        self.message=Label(self,text="AOO Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aoo.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aoo.getURL())
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aoo.getAA())
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aoo.getAPW())
        self.a_p_w_E.place(x=350,y=280)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=420,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=220,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        try:
            cUser.aoo.setLRL(self.lrl.get())
            cUser.aoo.setURL(self.url.get())
            cUser.aoo.setAA(self.aa.get())
            cUser.aoo.setAPW(self.apw.get())
            storeD()
            messagebox.showinfo("Message","Changes saved")
        except TypeError:
            messagebox.showerror("Error","All terms must be numbers")
        except IndexError:
            messagebox.showerror("Error","All terms must be inside of boundaries")

    
    def clearPressed(self,e):
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.aoo.getLRL())
            self.url.set(cUser.aoo.getURL())
            self.aa.set(cUser.aoo.getAA())
            self.apw.set(cUser.aoo.getAPW())

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
        

        
class VOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.write_voo_parameters()

    def write_voo_parameters(self):
        self.message=Label(self,text="VOO Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.voo.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.voo.getURL())
        self.u_r_l_E.place(x=350,y=200)
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=240)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.voo.getVA())
        self.v_a_E.place(x=350,y=240)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=280)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.voo.getVPW())
        self.v_p_w_E.place(x=350,y=280)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=420,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=220,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        try:
            cUser.voo.setLRL(self.lrl.get())
            cUser.voo.setURL(self.url.get())
            cUser.voo.setVA(self.va.get())
            cUser.voo.setVPW(self.vpw.get())
            storeD()
            messagebox.showinfo("Message","Changes saved")
        except TypeError:
            messagebox.showerror("Error","All terms must be numbers")
        except IndexError:
            messagebox.showerror("Error","All terms must be inside of boundaries")

    
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
        self.place(relheight=1,relwidth=1)
        self.write_vvi_parameters()

    def write_vvi_parameters(self):
        self.message=Label(self,text="VVI Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.vvi.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.vvi.getURL())
        self.u_r_l_E.place(x=350,y=200)
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=240)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=350,y=240)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=280)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=350,y=280)
        self.v_r_p=Label(self,text="VRP :",font=("Times New Roman",14))
        self.v_r_p.place(x=100,y=320)
        self.vrp=StringVar()
        self.vrp_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",14))
        self.vrp.set(cUser.vvi.getVRP())
        self.vrp_E.place(x=350,y=320)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=420,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=220,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        try:
            cUser.vvi.setLRL(self.lrl.get())
            cUser.vvi.setURL(self.url.get())
            cUser.vvi.setVA(self.va.get())
            cUser.vvi.setVPW(self.vpw.get())
            cUser.vvi.setVRP(self.vrp.get())
            storeD()
            messagebox.showinfo("Message","Changes saved")
        except TypeError:
            messagebox.showerror("Error","All terms must be numbers")
        except IndexError:
            messagebox.showerror("Error","All terms must be inside of boundaries")

    
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
        self.place(relheight=1,relwidth=1)
        self.write_aai_parameters()

    def write_aai_parameters(self):
        self.message=Label(self,text="AAI Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=350,y=280)
        self.a_r_p=Label(self,text="ARP :",font=("Times New Roman",14))
        self.a_r_p.place(x=100,y=320)
        self.arp=StringVar()
        self.arp_E=Entry(self,textvariable=self.arp,font=("Times New Roman",14))
        self.arp.set(cUser.aai.getARP())
        self.arp_E.place(x=350,y=320)


        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=420,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=220,y=450)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        try:
            cUser.aai.setLRL(self.lrl.get())
            cUser.aai.setURL(self.url.get())
            cUser.aai.setAA(self.aa.get())
            cUser.aai.setAPW(self.apw.get())
            cUser.aai.setARP(self.arp.get())
            storeD()
            messagebox.showinfo("Message","Changes saved")
        except TypeError:
            messagebox.showerror("Error","All terms must be numbers")
        except IndexError:
            messagebox.showerror("Error","All terms must be inside of boundaries")

    
    def clearPressed(self,e):
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.aai.getLRL())
            self.url.set(cUser.aai.getURL())
            self.aa.set(cUser.aai.getAA())
            self.apw.set(cUser.aai.getAPW())
            self.arp.set(cUser.aai.getARP())

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()


def serial_Communication():
	if(ifCommu == true):
		messagebox.showinfo("The pacemaker is successfully connected");
	else:
		messagebox.showinfo("Connection failed, please try again");

def is_Approach(self):
	if(ifApp == true):
		messagebox.showinfo("A different pacemaker is approached than was previously interrogated");

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
