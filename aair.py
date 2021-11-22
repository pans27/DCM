from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import pickle
import main


class AAIRparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aair_parameters()

    def write_aair_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="AAIR Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=125,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.aair.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.aair.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.aair.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.aair.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate : "+str(cUser.aair.getMSR()),font=("Times New Roman",18))
        self.m_s_r.place(x=55,y=210)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",18))
        self.msr.set(cUser.aair.getMSR())
        self.m_s_r_E.place(x=350,y=210)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.aair.getAA()),font=("Times New Roman",18))
        self.a_a.place(x=660,y=210)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",18))
        self.aa.set(cUser.aair.getAA())
        self.a_a_E.place(x=900,y=210)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.aair.getAPW()),font=("Times New Roman",18))
        self.a_p_w.place(x=90,y=260)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",18))
        self.apw.set(cUser.aair.getAPW())
        self.a_p_w_E.place(x=350,y=260)
        #Atrial Sensitivity
        self.a_s=Label(self,text="Atrial Sensitivity : "+str(cUser.aair.getAS()),font=("Times New Roman",18))
        self.a_s.place(x=660,y=260)
        self.ats=StringVar()
        self.a_s_E=Entry(self,textvariable=self.ats,font=("Times New Roman",18))
        self.ats.set(cUser.aair.getAS())
        self.a_s_E.place(x=900,y=260)
        #ARP
        self.a_r_p=Label(self,text="ARP : "+str(cUser.aair.getARP()),font=("Times New Roman",18))
        self.a_r_p.place(x=225,y=310)
        self.arp=StringVar()
        self.a_r_p_E=Entry(self,textvariable=self.arp,font=("Times New Roman",18))
        self.arp.set(cUser.aair.getARP())
        self.a_r_p_E.place(x=350,y=310)
        #PVARP
        self.p_v_a_r_p=Label(self,text="PVARP : "+str(cUser.aair.getPVARP()),font=("Times New Roman",18))
        self.p_v_a_r_p.place(x=745,y=310)
        self.pvarp=StringVar()
        self.p_v_a_r_p_E=Entry(self,textvariable=self.pvarp,font=("Times New Roman",18))
        self.pvarp.set(cUser.aair.getPVARP())
        self.p_v_a_r_p_E.place(x=900,y=310)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis : "+str(cUser.aair.getHYST()),font=("Times New Roman",18))
        self.hysteresis.place(x=170,y=360)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",18))
        self.hys.set(cUser.aair.getHYST())
        self.hysteresis_E.place(x=350,y=360)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing : "+str(cUser.aair.getRS()),font=("Times New Roman",18))
        self.r_s.place(x=670,y=360)
        self.rs_data = ['0 OFF','3','6','9','12','15','18','21','25']
        self.rs = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.rs.set(cUser.aair.getRS())
        self.rs['values'] = self.rs_data
        self.rs.place(x=900,y=360)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold : "+str(cUser.aair.getAT()),font=("Times New Roman",18))
        self.a_t.place(x=90,y=410)
        self.at_data = ['1 V-Low', '2 Low', '3 Med-Low', '4 Med','5 Med-High', '6 High', '7 V-High']
        self.at_roll = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.at_roll['values'] = self.at_data
        self.at_roll.set(self.at_data[cUser.aair.getATV()-1])
        self.at_roll.place(x=350,y=410)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time : "+str(cUser.aair.getREACT()),font=("Times New Roman",18))
        self.r_t.place(x=680,y=410)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",18))
        self.rt.set(cUser.aair.getREACT())
        self.r_t_E.place(x=900,y=410)
        #Response Factor
        self.r_f=Label(self,text="Response Factor : "+str(cUser.aair.getRF()),font=("Times New Roman",18))
        self.r_f.place(x=110,y=460)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",18))
        self.rf.set(cUser.aair.getRF())
        self.r_f_E.place(x=350,y=460)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time : "+str(cUser.aair.getRECOVT()),font=("Times New Roman",18))
        self.recovery_time.place(x=675,y=460)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",18))
        self.ret.set(cUser.aair.getRECOVT())
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
            cUser.aair.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.aair.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.aair.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.aair.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175, and larger than LRL\n"
            errors+=1
            
        try:
            cUser.aair.setMSR(self.msr.get())
            self.m_s_r['text']="Maximum Sensor Rate : "+str(cUser.aair.getMSR())
        except TypeError:
            text=text+"MSR must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"MSR must be between 50 and 175\n"
            errors+=1
            
        try:
            cUser.aair.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.aair.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0.5 and 5.0\n"
            errors+=1
            
        try:
            cUser.aair.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.aair.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
            
        try:
            cUser.aair.setAS(self.ats.get())
            self.a_s['text']="Atrial Sensitivity : "+str(cUser.aair.getAS())
        except TypeError:
            text=text+"AS must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AS must be between 0.0 and 5.0\n"
            errors+=1
            
        try:
            cUser.aair.setARP(self.arp.get())
            self.a_r_p['text']="ARP : "+str(cUser.aair.getARP())
        except TypeError:
            text=text+"ARP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"ARP must be between 150 and 500\n"
            errors+=1
            
        try:
            cUser.aair.setPVARP(self.pvarp.get())
            self.p_v_a_r_p['text']="PVARP : "+str(cUser.aair.getPVARP())
        except TypeError:
            text=text+"PVARP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"PVARP must be between 150 and 500\n"
            errors+=1
            
        try:
            cUser.aair.setHYST(self.hys.get())
            self.hysteresis['text']="Hysteresis : "+str(cUser.aair.getHYST())
        except TypeError:
            text=text+"HYST must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"HYST must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.aair.setRS(self.rs.get().split()[0])
            self.r_s['text']="Rate Smoothing : "+str(cUser.aair.getRS())
        except :
            text=text+"RS not stored\n"
            errors+=1
            
        try:
            cUser.aair.setAT(self.at_roll.get()[0])
            self.a_t['text']="Activity Threshold : "+str(cUser.aair.getAT())
        except :
            text=text+"Activity Threshold not stored\n"
            errors+=1
            
        try:
            cUser.aair.setREACT(self.rt.get())
            self.r_t['text']="Reaction Time : "+str(cUser.aair.getREACT())
        except TypeError:
            text=text+"Reaction Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Reaction Time must be between 10s and 50s\n"
            errors+=1
            
        try:
            cUser.aair.setRF(self.rf.get())
            self.r_f['text']="Response Factor : "+str(cUser.aair.getRF())
        except TypeError:
            text=text+"Response factor must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Response factor must be between 1 and 16\n"
            errors+=1

        try:
            cUser.aair.setRECOVT(self.ret.get())
            self.recovery_time['text']="Recovery Time : "+str(cUser.aair.getRECOVT())
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
                    info=main.serial_Communication(6,cUser.aair.getLRL(),cUser.aair.getAPW(),0,0,cUser.aair.getARP(),0,round(cUser.aair.getAA()*10),cUser.aair.getRECOVT()*60,cUser.aair.getRF(),cUser.aair.getMSR(),0,cUser.aair.getATV(),cUser.aair.getREACT())
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
            self.lrl.set(cUser.aair.getLRL())
            self.url.set(cUser.aair.getURL())
            self.aa.set(cUser.aair.getAA())
            self.apw.set(cUser.aair.getAPW())
            self.arp.set(cUser.aair.getARP())
            self.pvarp.set(cUser.aair.getPVARP())
            self.hys.set(cUser.aair.getHYST())
            self.rates.set(cUser.aair.getRS())
            self.at.set(cUser.aair.getAT())
            self.rt.set(cUser.aair.getREACT())
            self.rf.set(cUser.aair.getRF())
            self.ret.set(cUser.aair.getRECOVT())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
