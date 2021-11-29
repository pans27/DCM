from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import main
import egram
class DOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_door_parameters()

    def write_door_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="DOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=125,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.door.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.door.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.door.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.door.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate : "+str(cUser.door.getMSR()),font=("Times New Roman",18))
        self.m_s_r.place(x=55,y=220)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",18))
        self.msr.set(cUser.door.getMSR())
        self.m_s_r_E.place(x=350,y=220)
        #Fixed AV Dealy
        self.fixed_AV_delay=Label(self,text="Fixed AV Dealy : "+str(cUser.door.getFAVD()),font=("Times New Roman",18))
        self.fixed_AV_delay.place(x=665,y=220)
        self.fad=StringVar()
        self.fixed_AV_delay_E=Entry(self,textvariable=self.fad,font=("Times New Roman",18))
        self.fad.set(cUser.door.getFAVD())
        self.fixed_AV_delay_E.place(x=900,y=220)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.door.getAA()),font=("Times New Roman",18))
        self.a_a.place(x=110,y=280)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",18))
        self.aa.set(cUser.door.getAA())
        self.a_a_E.place(x=350,y=280)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude : "+str(cUser.door.getVA()),font=("Times New Roman",18))
        self.v_a.place(x=605,y=280)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",18))
        self.va.set(cUser.door.getVA())
        self.v_a_E.place(x=900,y=280)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.door.getAPW()),font=("Times New Roman",18))
        self.a_p_w.place(x=95,y=340)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",18))
        self.apw.set(cUser.door.getAPW())
        self.a_p_w_E.place(x=350,y=340)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width : "+str(cUser.door.getVPW()),font=("Times New Roman",18))
        self.v_p_w.place(x=590,y=340)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",18))
        self.vpw.set(cUser.door.getVPW())
        self.v_p_w_E.place(x=900,y=340)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold : "+str(cUser.door.getAT()),font=("Times New Roman",18))
        self.a_t.place(x=90,y=400)
        self.at_data = ['1.13 V-Low', '1.25 Low', '1.4 Med-Low', '1.6 Med','2 Med-High', '2.4 High', '3 V-High']
        self.at_roll = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.at_roll['values'] = self.at_data
        self.at_roll.set(cUser.door.getATV())
        self.at_roll.place(x=350,y=400)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time : "+str(cUser.door.getREACT()),font=("Times New Roman",18))
        self.r_t.place(x=680,y=400)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",18))
        self.rt.set(cUser.door.getREACT())
        self.r_t_E.place(x=900,y=400)
        #Response Factor
        self.r_f=Label(self,text="Response Factor : "+str(cUser.door.getRF()),font=("Times New Roman",18))
        self.r_f.place(x=110,y=460)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",18))
        self.rf.set(cUser.door.getRF())
        self.r_f_E.place(x=350,y=460)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time : "+str(cUser.door.getRECOVT()),font=("Times New Roman",18))
        self.recovery_time.place(x=675,y=460)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",18))
        self.ret.set(cUser.door.getRECOVT())
        self.recovery_time_E.place(x=900,y=460)

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
        self.egramB.bind("<Button-1>",self.egramPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2,font=("Times New Roman",14))
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    def confirmPressed(self,e):
        from global_ import cUser
        from global_ import Commu
        prompt=messagebox.askquestion("Message","Values that does not match the specified increment may be rounded, save?")
        if(prompt=="no"):
            return
        errors=0
        text=""
        try:
            if(float(self.url.get())<float(self.lrl.get()) and float(self.msr.get())<float(self.lrl.get()) and float(self.url.get())<float(self.msr.get())):
                errors+=1
                text=text+"LRL, URL, and MSR are conflictd\n"
            else:
                try:
                    cUser.doo.setLRL(self.lrl.get())
                    self.l_r_l['text']="Lower Rate Limit : "+str(cUser.doo.getLRL())
                except TypeError:
                    text=text+"LRL must be numeric\n"
                    errors+=1
                except IndexError:
                    text=text+"LRL must be between 30 and 175, and smaller than URL\n"
                    errors+=1
                try:
                    cUser.doo.setURL(self.url.get())
                    self.u_r_l['text']="Upper Rate Limit : "+str(cUser.doo.getURL())
                except TypeError:
                    text=text+"URL must be numeric\n"
                    errors+=1
                except IndexError:
                    text=text+"URL must be between 50 and 175, and larger than LRL\n"
                    errors+=1
                try:
                    cUser.door.setMSR(self.msr.get())
                    self.m_s_r['text']="Maximum Sensor Rate : "+str(cUser.door.getMSR())
                except TypeError:
                    text=text+"MSR must be numeric\n"
                    errors+=1
                except IndexError:
                    text=text+"MSR must be between 50 and 175, and larger than LRL, smaller than URL\n"
                    errors+=1
        except:
            text=text+"LRL, URL, and MSR must be numeric\n"
            errors+=1
        try:
            cUser.door.setFAVD(self.fad.get())
            self.a_a['text']="Fixed AV Delay : "+str(cUser.door.getFAVD())
        except TypeError:
            text=text+"FAVD must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"FAVD must be between 70 and 300\n"
            errors+=1
        try:
            cUser.door.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.door.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.door.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.door.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
        try:
            cUser.door.setVA(self.va.get())
            self.v_a['text']="Ventricular Amplitude : "+str(cUser.door.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.door.setVPW(self.vpw.get())
            self.v_p_w['text']="Ventricular Pulse Width : "+str(cUser.door.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        try:
            cUser.door.setAT(self.at_roll.get().split()[0])
            self.a_t['text']="Activity Threshold : "+str(cUser.door.getAT())
        except :
            text=text+"Activity Threshold not stored\n"
            errors+=1
        try:
            cUser.voor.setREACT(self.rt.get())
            self.r_t['text']="Reaction Time : "+str(cUser.voor.getREACT())
        except TypeError:
            text=text+"Reaction Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Reaction Time must be between 10s and 50s\n"
            errors+=1
            
        try:
            cUser.voor.setRF(self.rf.get())
            self.r_f['text']="Response Factor : "+str(cUser.voor.getRF())
        except TypeError:
            text=text+"Response factor must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Response factor must be between 1 and 16\n"
            errors+=1

        try:
            cUser.voor.setRECOVT(self.ret.get())
            self.recovery_time['text']="Recovery Time : "+str(cUser.voor.getRECOVT())
        except TypeError:
            text=text+"Recovery Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Recovery Time must be between 1 and 16\n"
            errors+=1
        if(errors==0):
            main.storeD()
            if(Commu):
                prompt=messagebox.askquestion("Message","Changes saved, Send to connected pacemaker?")
                if(prompt=="yes"):
                    info=main.serial_Communication(9,cUser.door.getLRL(),cUser.door.getAPW(),cUser.door.getVPW(),cUser.door.getVA(),0,0,cUser.door.getAA(),cUser.door.getRECOVT()*60,cUser.door.getRF(),cUser.door.getMSR(),cUser.door.getFAVD(),cUser.door.getATV(),cUser.door.getREACT(),0,0)
                    messagebox.showinfo("Message",info)
            else:
                messagebox.showinfo("Message","Changes saved")
        else:
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Values may not be saved")
            main.storeD()
    
    def clearPressed(self,e):
        from global_ import cUser
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.door.getLRL())
            self.url.set(cUser.door.getURL())
            self.msr.set(cUser.door.getMSR())
            self.fad.set(cUser.door.getFAVD())
            self.aa.set(cUser.door.getAA())
            self.apw.set(cUser.door.getAPW())
            self.va.set(cUser.door.getVA())
            self.vpw.set(cUser.door.getVPW())
            self.at_roll.set(cUser.door.getATV())
            self.rt.set(cUser.door.getREACT())
            self.rf.set(cUser.door.getRF())
            self.ret.set(cUser.door.getRECOVT())

    def egramPressed(self,e):
        from global_ import Commu
        if(Commu!=0):
            egram.Egram()
        else:
            messagebox.showinfo("Message","Pacemaker not connected")
            

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
