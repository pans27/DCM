from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
import main


class VVIRparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_vvir_parameters()

    def write_vvir_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="VVIR Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=30,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.vvir.getLRL())
        self.l_r_l_E.place(x=180,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=360,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.vvir.getURL())
        self.u_r_l_E.place(x=540,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=30,y=200)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.vvir.getMSR())
        self.m_s_r_E.place(x=180,y=200)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=360,y=200)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvir.getVA())
        self.v_a_E.place(x=540,y=200)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=30,y=240)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvir.getVPW())
        self.v_p_w_E.place(x=180,y=240)
        #Ventricular Sensitivity
        self.v_s=Label(self,text="Ventricular Sensitivity :",font=("Times New Roman",14))
        self.v_s.place(x=360,y=240)
        self.vs=StringVar()
        self.v_s_E=Entry(self,textvariable=self.vs,font=("Times New Roman",14))
        self.vs.set(cUser.vvir.getVS())
        self.v_s_E.place(x=540,y=240)
        #VRP
        self.v_r_p=Label(self,text="VRP :",font=("Times New Roman",14))
        self.v_r_p.place(x=30,y=280)
        self.vrp=StringVar()
        self.vrp_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",14))
        self.vrp.set(cUser.vvir.getVRP())
        self.vrp_E.place(x=180,y=280)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis :",font=("Times New Roman",14))
        self.hysteresis.place(x=360,y=280)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",14))
        self.hys.set(cUser.vvir.getHYST())
        self.hysteresis_E.place(x=540,y=280)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing :",font=("Times New Roman",14))
        self.r_s.place(x=30,y=320)
        self.rates=StringVar()
        self.r_s_E=Entry(self,textvariable=self.rates,font=("Times New Roman",14))
        self.rates.set(cUser.vvir.getRS())
        self.r_s_E.place(x=180,y=320)
         #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=360,y=320)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvir.getAT())
        self.a_t_E.place(x=540,y=320)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=30,y=360)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvir.getREACT())
        self.r_t_E.place(x=180,y=360)
        #Response Factor
        self.r_f=Label(self,text="Response Factor :",font=("Times New Roman",14))
        self.r_f.place(x=360,y=360)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvir.getRF())
        self.r_f_E.place(x=540,y=360)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=30,y=400)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvir.getRECOVT())
        self.recovery_time_E.place(x=180,y=400)

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
            cUser.vvir.setLRL(self.lrl.get())
            self.lrl.set(cUser.vvir.getLRL())
        except TypeError:
            text=text+"Lower rate limit must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Lower rate limit must be between 30 and 175\n"
            errors+=1
            
        try:
            cUser.vvir.setURL(self.url.get())
            self.url.set(cUser.vvir.getURL())
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
            cUser.vvir.setVA(self.va.get())
            self.va.set(cUser.vvir.getVA())
        except TypeError:
            text=text+"Ventricular pulse amplitude must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Ventricular pulse amplitude must be between 0.5 and 7.0\n"
            errors+=1
            
        try:
            cUser.vvir.setVPW(self.vpw.get())
            self.vpw.set(cUser.vvir.getVPW())
        except TypeError:
            text=text+"Ventricular pulse width must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Ventricular pulse width must be between 0.1 and 1.9\n"
            errors+=1
            
        try:
            cUser.vvir.setVS(self.vs.get())
            self.vs.set(cUser.vvir.getVS())
        except TypeError:
            text=text+"Ventricular Sensitivity must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Ventricular Sensitivity must be between 0.0 and 5.0\n"
            errors+=1
            
        try:
            cUser.vvir.setVRP(self.vrp.get())
            self.vrp.set(cUser.vvir.getVRP())
        except TypeError:
            text=text+"VRP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VRP must be between 150 and 500\n"
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
                                                                                                                   `
        #Error counting and final part, every try before this
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
            self.lrl.set(cUser.vvir.getLRL())
            self.url.set(cUser.vvir.getURL())
            self.va.set(cUser.vvir.getVA())
            self.vpw.set(cUser.vvir.getVPW())
            self.vrp.set(cUser.vvir.getVRP())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
