from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
import main


class DOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_doo_parameters()

    def write_doo_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="DOO Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",16))
        self.current.place(x=100,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.doo.getLRL()),font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.doo.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.doo.getURL()),font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.doo.getURL())
        self.u_r_l_E.place(x=350,y=200)
        #Fixed AV Dealy
        self.fixed_AV_delay=Label(self,text="Fixed AV Delay : "+str(cUser.doo.getFAVD()),font=("Times New Roman",14))
        self.fixed_AV_delay.place(x=100,y=240)
        self.fad=StringVar()
        self.fixed_AV_delay_E=Entry(self,textvariable=self.fad,font=("Times New Roman",14))
        self.fad.set(cUser.doo.getAA())
        self.fixed_AV_delay_E.place(x=350,y=240)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.doo.getAA()),font=("Times New Roman",14))
        self.a_a.place(x=100,y=280)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.doo.getAA())
        self.a_a_E.place(x=350,y=280)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude : "+str(cUser.doo.getVA()),font=("Times New Roman",14))
        self.v_a.place(x=100,y=320)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.doo.getVA())
        self.v_a_E.place(x=350,y=320)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.doo.getAPW()),font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=360)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.doo.getAPW())
        self.a_p_w_E.place(x=350,y=360)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width : "+str(cUser.doo.getVPW()),font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=400)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.doo.getVPW())
        self.v_p_w_E.place(x=350,y=400)

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
        from global_ import cUser
        prompt=messagebox.askquestion("Message","Values that does not match the specified increment may be rounded, save?")
        if(prompt=="no"):
            return
        errors=0
        text=""
        try:
            cUser.doo.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.doo.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.doo.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.doo.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.doo.setFAVD(self.aa.get())
            self.a_a['text']="Fixed AV Delay : "+str(cUser.doo.getFAVD())
        except TypeError:
            text=text+"FAVD must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"FAVD must be between 70 and 300\n"
            errors+=1
        try:
            cUser.doo.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.doo.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.doo.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.doo.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
        try:
            cUser.doo.setVA(self.va.get())
            self.v_a['text']="Ventricular Amplitude : "+str(cUser.doo.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.doo.setVPW(self.vpw.get())
            self.v_p_w['text']="Ventricular Pulse Width : "+str(cUser.doo.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        if(errors==0):
            messagebox.showinfo("Message","Changes saved")
            main.storeD()
        elif(errors):
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Other values are saved")
            main.storeD()
    
    def clearPressed(self,e):
        from global_ import cUser
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.doo.getLRL())
            self.url.set(cUser.doo.getURL())
            self.va.set(cUser.doo.getVA())
            self.vpw.set(cUser.doo.getVPW())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()