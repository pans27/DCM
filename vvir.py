from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import main
import egram

class VVIRparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_vvir_parameters()

    def write_vvir_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="VVIR Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=125,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.vvir.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.vvir.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.vvir.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.vvir.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate : "+str(cUser.vvir.getMSR()),font=("Times New Roman",18))
        self.m_s_r.place(x=55,y=210)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",18))
        self.msr.set(cUser.vvir.getMSR())
        self.m_s_r_E.place(x=350,y=210)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude : "+str(cUser.vvir.getVA()),font=("Times New Roman",18))
        self.v_a.place(x=605,y=210)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",18))
        self.va.set(cUser.vvir.getVA())
        self.v_a_E.place(x=900,y=210)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width : "+str(cUser.vvir.getVPW()),font=("Times New Roman",18))
        self.v_p_w.place(x=40,y=260)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",18))
        self.vpw.set(cUser.vvir.getVPW())
        self.v_p_w_E.place(x=350,y=260)
        #Ventricular Sensitivity
        self.v_s=Label(self,text="Ventricular Sensitivity : "+str(cUser.vvir.getVS()),font=("Times New Roman",18))
        self.v_s.place(x=605,y=260)
        self.vs=StringVar()
        self.v_s_E=Entry(self,textvariable=self.vs,font=("Times New Roman",18))
        self.vs.set(cUser.vvir.getVS())
        self.v_s_E.place(x=900,y=260)
        #VRP
        self.v_r_p=Label(self,text="VRP : "+str(cUser.vvir.getVRP()),font=("Times New Roman",18))
        self.v_r_p.place(x=225,y=310)
        self.vrp=StringVar()
        self.vrp_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",18))
        self.vrp.set(cUser.vvir.getVRP())
        self.vrp_E.place(x=350,y=310)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis : "+str(cUser.vvir.getHYST()),font=("Times New Roman",18))
        self.hysteresis.place(x=720,y=310)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",18))
        self.hys.set(cUser.vvir.getHYST())
        self.hysteresis_E.place(x=900,y=310)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing : "+str(cUser.vvir.getRS()),font=("Times New Roman",18))
        self.r_s.place(x=120,y=360)
        self.rs_data = ['0 OFF','3','6','9','12','15','18','21','25']
        self.rs = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.rs.set(cUser.vvir.getRS())
        self.rs['values'] = self.rs_data
        self.rs.place(x=350,y=360)
         #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold : "+str(cUser.vvir.getAT()),font=("Times New Roman",18))
        self.a_t.place(x=640,y=360)
        self.at_data = ['1.13 V-Low', '1.25 Low', '1.4 Med-Low', '1.6 Med','2 Med-High', '2.4 High', '3 V-High']
        self.at_roll = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.at_roll['values'] = self.at_data
        self.at_roll.set(cUser.vvir.getATV())
        self.at_roll.place(x=900,y=360)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time : "+str(cUser.vvir.getREACT()),font=("Times New Roman",18))
        self.r_t.place(x=130,y=410)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",18))
        self.rt.set(cUser.vvir.getREACT())
        self.r_t_E.place(x=350,y=410)
        #Response Factor
        self.r_f=Label(self,text="Response Factor : "+str(cUser.vvir.getRF()),font=("Times New Roman",18))
        self.r_f.place(x=660,y=410)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",18))
        self.rf.set(cUser.vvir.getRF())
        self.r_f_E.place(x=900,y=410)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time : "+str(cUser.vvir.getRECOVT()),font=("Times New Roman",18))
        self.recovery_time.place(x=125,y=460)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",18))
        self.ret.set(cUser.vvir.getRECOVT())
        self.recovery_time_E.place(x=350,y=460)

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
            cUser.vvir.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.vvir.getLRL())
        except TypeError:
            text=text+"Lower rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Lower rate limit must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.vvir.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.vvir.getURL())
        except TypeError:
            text=text+"Upper rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Upper rate limit must be between 50 and 175, and larger than LRL\n"
            errors+=1
            
        try:
            cUser.vvir.setMSR(self.msr.get())
            self.m_s_r['text']="Maximum Sensor Rate : "+str(cUser.vvir.getMSR())
        except TypeError:
            text=text+"Maximum sensor rate must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Maximum sensor rate must be between 50 and 175\n"
            errors+=1
            
        try:
            cUser.vvir.setVA(self.va.get())
            self.v_a['text']="Ventricular Amplitude : "+str(cUser.vvir.getVA())
        except TypeError:
            text=text+"Ventricular pulse amplitude must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Ventricular pulse amplitude must be between 0.5 and 7.0\n"
            errors+=1
            
        try:
            cUser.vvir.setVPW(self.vpw.get())
            self.v_p_w['text']="Ventricular Pulse Width : "+str(cUser.vvir.getVPW())
        except TypeError:
            text=text+"Ventricular pulse width must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Ventricular pulse width must be between 0.1 and 1.9\n"
            errors+=1
            
        try:
            cUser.vvir.setVS(self.vs.get())
            self.v_s['text']="Ventricular Sensitivity : "+str(cUser.vvir.getVS())
        except TypeError:
            text=text+"Ventricular Sensitivity must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Ventricular Sensitivity must be between 0.0 and 5.0\n"
            errors+=1
            
        try:
            cUser.vvir.setVRP(self.vrp.get())
            self.v_r_p['text']="VRP : "+str(cUser.vvir.getVRP())
        except TypeError:
            text=text+"VRP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VRP must be between 150 and 500\n"
            errors+=1    

        try:
            cUser.vvir.setHYST(self.hys.get())
            self.hysteresis['text']="Hysteresis : "+str(cUser.vvir.getHYST())
        except TypeError:
            text=text+"Hysteresis rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Hysteresis rate limit must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.vvir.setRS(self.rs.get().split()[0])
            self.r_s['text']="Rate Smoothing : "+str(cUser.vvir.getRS())
        except :
            text=text+"RS not stored\n"
            errors+=1
            
        try:
            cUser.vvir.setAT(self.at_roll.get().split()[0])
            self.a_t['text']="Activity Threshold : "+str(cUser.vvir.getAT())
        except :
            text=text+"Activity Threshold not stored\n"
            errors+=1
            
        try:
            cUser.vvir.setREACT(self.rt.get())
            self.r_t['text']="Reaction Time : "+str(cUser.vvir.getREACT())
        except TypeError:
            text=text+"Reaction Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Reaction Time must be between 10s and 50s\n"
            errors+=1
            
        try:
            cUser.vvir.setRF(self.rf.get())
            self.r_f['text']="Response Factor : "+str(cUser.vvir.getRF())
        except TypeError:
            text=text+"Response factor must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Response factor must be between 1 and 16\n"
            errors+=1

        try:
            cUser.vvir.setRECOVT(self.ret.get())
            self.recovery_time['text']="Recovery Time : "+str(cUser.vvir.getRECOVT())
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
                    info=main.serial_Communication(8,cUser.vvir.getLRL(),0,cUser.vvir.getVPW(),cUser.vvir.getVA(),0,cUser.vvir.getVRP(),0,cUser.vvir.getRECOVT()*60,cUser.vvir.getRF(),cUser.vvir.getMSR(),0,cUser.vvir.getATV(),cUser.vvir.getREACT())
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
            self.lrl.set(cUser.vvir.getLRL())
            self.url.set(cUser.vvir.getURL())
            self.msr.set(cUser.vvir.getMSR())
            self.va.set(cUser.vvir.getVA())
            self.vpw.set(cUser.vvir.getVPW())
            self.vs.set(cUser.vvir.getVS())
            self.vrp.set(cUser.vvir.getVRP())
            self.hys.set(cUser.vvir.getHYST())
            self.rs.set(cUser.vvir.getRS())
            self.at_roll.set(cUser.vvir.getATV())
            self.rt.set(cUser.vvir.getREACT())
            self.rf.set(cUser.vvir.getRF())
            self.ret.set(cUser.vvir.getRECOVT())

    def egramPressed(self,e):
        from global_ import Commu
        if(Commu!=0):
            egram.Egram()
        else:
            messagebox.showinfo("Message","Pacemaker not connected")

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
