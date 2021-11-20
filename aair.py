from tkinter import *
from tkinter import messagebox
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
        self.message.place(x=420,y=40)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=120)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aair.getLRL())
        self.l_r_l_E.place(x=350,y=120)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=120)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aair.getURL())
        self.u_r_l_E.place(x=900,y=120)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=160)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aair.getMSR())
        self.m_s_r_E.place(x=350,y=160)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=650,y=160)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aair.getAA())
        self.a_a_E.place(x=900,y=160)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=200)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aair.getAPW())
        self.a_p_w_E.place(x=350,y=200)
        #Atrial Sensitivity
        self.a_s=Label(self,text="Atrial Sensitivity :",font=("Times New Roman",14))
        self.a_s.place(x=650,y=200)
        self.ats=StringVar()
        self.a_s_E=Entry(self,textvariable=self.ats,font=("Times New Roman",14))
        self.ats.set(cUser.aair.getAS())
        self.a_s_E.place(x=900,y=200)
        #ARP
        self.a_r_p=Label(self,text="ARP :",font=("Times New Roman",14))
        self.a_r_p.place(x=100,y=240)
        self.arp=StringVar()
        self.a_r_p_E=Entry(self,textvariable=self.arp,font=("Times New Roman",14))
        self.arp.set(cUser.aair.getARP())
        self.a_r_p_E.place(x=350,y=240)
        #PVARP
        self.p_v_a_r_p=Label(self,text="PVARP :",font=("Times New Roman",14))
        self.p_v_a_r_p.place(x=650,y=240)
        self.pvarp=StringVar()
        self.p_v_a_r_p_E=Entry(self,textvariable=self.pvarp,font=("Times New Roman",14))
        self.pvarp.set(cUser.aair.getPVARP())
        self.p_v_a_r_p_E.place(x=900,y=240)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis :",font=("Times New Roman",14))
        self.hysteresis.place(x=100,y=280)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",14))
        self.hys.set(cUser.aair.getHYST())
        self.hysteresis_E.place(x=350,y=280)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing :",font=("Times New Roman",14))
        self.r_s.place(x=650,y=280)
        self.rates=StringVar()
        self.r_s_E=Entry(self,textvariable=self.rates,font=("Times New Roman",14))
        self.rates.set(cUser.aair.getRS())
        self.r_s_E.place(x=900,y=280)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=100,y=320)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.aair.getAT())
        self.a_t_E.place(x=350,y=320)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=650,y=320)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.aair.getREACT())
        self.r_t_E.place(x=900,y=320)
        #Response Factor
        self.r_f=Label(self,text="Respond Factor :",font=("Times New Roman",14))
        self.r_f.place(x=100,y=360)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.aair.getRF())
        self.r_f_E.place(x=350,y=360)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=650,y=360)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.aair.getRECOVT())
        self.recovery_time_E.place(x=900,y=360)

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
        errors=0
        text=""
        try:
            cUser.aair.setLRL(self.lrl.get())
            self.lrl.set(cUser.aair.getLRL())
        except TypeError:
            text=text+"Lower rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Lower rate limit must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.aair.setURL(self.url.get())
            self.url.set(cUser.aair.getURL())
        except TypeError:
            text=text+"Upper rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Upper rate limit must be between 50 and 175\n"
            errors+=1
            
        try:
            cUser.vvir.setMSR(self.msr.get())
            self.msr.set(cUser.vvir.getMSR())
        except TypeError:
            text=text+"Maximum sensor rate must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Maximum sensor rate must be between 50 and 175\n"
            errors+=1
            
        try:
            cUser.aair.setAA(self.aa.get())
            self.aa.set(cUser.aair.getAA())
        except TypeError:
            text=text+"Atrial pulse amplitude must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Atrial pulse amplitude must be between 0.5 and 5.0\n"
            errors+=1
            
        try:
            cUser.aair.setAPW(self.apw.get())
            self.apw.set(cUser.aair.getAPW())
        except TypeError:
            text=text+"Atrial pulse width must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Atrial pulse width must be between 1 and 30\n"
            errors+=1
            
        try:
            cUser.vvir.setAS(self.as.get())
            self.as.set(cUser.vvir.getAS())
        except TypeError:
            text=text+"Atrial Sensitivity must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Atrial Sensitivity must be between 0.0 and 5.0\n"
            errors+=1
            
        try:
            cUser.aair.setARP(self.arp.get())
            self.arp.set(cUser.aair.getARP())
        except TypeError:
            text=text+"ARP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"ARP must be between 150 and 500\n"
            errors+=1
            
        try:
            cUser.aair.setPVARP(self.pvarp.get())
            self.pvarp.set(cUser.aair.getPVARP())
        except TypeError:
            text=text+"PVARP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"PVARP must be between 150 and 500\n"
            errors+=1
            
        try:
            cUser.vvir.setHYST(self.hys.get())
            self.hys.set(cUser.vvir.getHYST())
        except TypeError:
            text=text+"Hysteresis rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Hysteresis rate limit must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.vvir.setRS(self.rates.get())
            self.rates.set(cUser.vvir.getRS())
        except TypeError:
            text=text+"Rate smoothing must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Rate smoothing must be between 3 and 21\n"
            errors+=1
            
        try:
            cUser.vvir.setAT(self.at.get())
            self.at.set(cUser.vvir.getAT())
        except TypeError:
            text=text+"Activity Threshold must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Activity Threshold must be between 2 and 8\n"
            errors+=1
            
        try:
            cUser.vvir.setREACT(self.rt.get())
            self.rt.set(cUser.vvir.getREACT())
        except TypeError:
            text=text+"Reaction Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Reaction Time must be between 10s and 50s\n"
            errors+=1
            
        try:
            cUser.vvir.setRF(self.rf.get())
            self.rf.set(cUser.vvir.getRF())
        except TypeError:
            text=text+"Response factor must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Response factor must be between 1 and 16\n"
            errors+=1

        try:
            cUser.vvir.setRECOVT(self.ret.get())
            self.ret.set(cUser.vvir.getRECOVT())
        except TypeError:
            text=text+"Recovery Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Recovery Time must be between 1 and 16\n"
            errors+=1
            
        if(errors==0):
            messagebox.showinfo("Message","Changes saved")
            main.storeD()
        elif(errors<5):
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Other values are saved")
            main.storeD()
        else:
            messagebox.showinfo("Message","There are "+str(errors)+" error(S):\n"+text)

    
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
            self.at.set(cUser.vvir.getAT())
            self.rt.set(cUser.vvir.getREACT())
            self.rf.set(cUser.vvir.getRF())
            self.ret.set(cUser.vvir.getRECOVT())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
