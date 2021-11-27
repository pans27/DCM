from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
import main
import egram

class AOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aoo_parameters()

    def write_aoo_parameters(self): #creating labels and entry fields
        from global_ import cUser
        self.title=Label(self,text="AOO Parameters",font=("Times New Roman",30))
        self.title.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=425,y=120)
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.aoo.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=400,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.aoo.getLRL())
        self.l_r_l_E.place(x=650,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.aoo.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=400,y=220)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.aoo.getURL())
        self.u_r_l_E.place(x=650,y=220)
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.aoo.getAA()),font=("Times New Roman",18))
        self.a_a.place(x=410,y=280)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",18))
        self.aa.set(cUser.aoo.getAA())
        self.a_a_E.place(x=650,y=280)
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.aoo.getAPW()),font=("Times New Roman",18))
        self.a_p_w.place(x=395,y=340)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",18))
        self.apw.set(cUser.aoo.getAPW())
        self.a_p_w_E.place(x=650,y=340)

        self.comfirmB=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=565,y=550)
        self.clearB=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=335,y=550)
        self.egramB=Button(self,width=15,height=3,font=("Times New Roman",14))
        self.egramB["text"]="Egram"
        self.egramB.place(x=795,y=550)
        self.clearB.bind("<Button-1>",self.clearPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.egramB.bind("<Button-1>",self.egramPressed)
        self.back=Button(self,width=10,height=2,font=("Times New Roman",14))
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e): # check each parameter to see if there is an error, keep track of the errors
        from global_ import cUser
        from global_ import Commu
        prompt=messagebox.askquestion("Message","Values that does not match the specified increment may be rounded, save?")
        if(prompt=="no"):
            return
        errors=0
        text=""
        try:
            cUser.aoo.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.aoo.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.aoo.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.aoo.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175, and larger than LRL\n"
            errors+=1
        try:
            cUser.aoo.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.aoo.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.aoo.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.aoo.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
        if(errors==0): #print out errors ifthere are any, store the changes without error to hard drive
            main.storeD()
            if(Commu):
                prompt=messagebox.askquestion("Message","Changes saved, Send to connected pacemaker?")
                if(prompt=="yes"):
                    info=main.serial_Communication(0,cUser.aoo.getLRL(),cUser.aoo.getAPW(),0,0,0,0,cUser.aoo.getAA(),0,0,0,0,7,0)
                    messagebox.showinfo("Message",info)
            else:
                messagebox.showinfo("Message","Changes saved")
        else:
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Values may not be saved")
            main.storeD()


    def clearPressed(self,e):
        from global_ import cUser
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?") # set all entry field to show the parameter stored
        if(prompt=='yes'):
            self.lrl.set(cUser.aoo.getLRL())
            self.url.set(cUser.aoo.getURL())
            self.aa.set(cUser.aoo.getAA())
            self.apw.set(cUser.aoo.getAPW())

    def egramPressed(self,e):
        egram.Egram()

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()