from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import pickle
import main


class VOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_voor_parameters()

    def write_voor_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="VOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=125,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.voor.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.voor.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.voor.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.voor.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate : "+str(cUser.voor.getMSR()),font=("Times New Roman",18))
        self.m_s_r.place(x=55,y=220)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",18))
        self.msr.set(cUser.voor.getMSR())
        self.m_s_r_E.place(x=350,y=220)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude : "+str(cUser.voor.getVA()),font=("Times New Roman",18))
        self.v_a.place(x=605,y=220)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",18))
        self.va.set(cUser.voor.getVA())
        self.v_a_E.place(x=900,y=220)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width : "+str(cUser.voor.getVPW()),font=("Times New Roman",18))
        self.v_p_w.place(x=40,y=280)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",18))
        self.vpw.set(cUser.voor.getVPW())
        self.v_p_w_E.place(x=350,y=280)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold : "+str(cUser.voor.getAT()),font=("Times New Roman",18))
        self.a_t.place(x=640,y=280)
        self.at_data = ['1 V-Low', '2 Low', '3 Med-Low', '4 Med','5 Med-High', '6 High', '7 V-High']
        self.at_roll = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.at_roll['values'] = self.at_data
        self.at_roll.set(self.at_data[cUser.voor.getATV()-1])
        self.at_roll.place(x=900,y=280)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time : "+str(cUser.voor.getREACT()),font=("Times New Roman",18))
        self.r_t.place(x=130,y=340)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",18))
        self.rt.set(cUser.voor.getREACT())
        self.r_t_E.place(x=350,y=340)
        #Response Factor
        self.r_f=Label(self,text="Response Factor : "+str(cUser.voor.getRF()),font=("Times New Roman",18))
        self.r_f.place(x=660,y=340)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",18))
        self.rf.set(cUser.voor.getRF())
        self.r_f_E.place(x=900,y=340)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time : "+str(cUser.voor.getRECOVT()),font=("Times New Roman",18))
        self.recovery_time.place(x=125,y=400)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",18))
        self.ret.set(cUser.voor.getRECOVT())
        self.recovery_time_E.place(x=350,y=400)

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
            cUser.voor.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.voor.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.voor.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.voor.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175, and larger than LRL\n"
            errors+=1
        try:
            cUser.voor.setVA(self.va.get())
            self.v_a['text']="Ventricular Amplitude : "+str(cUser.voor.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.voor.setVPW(self.vpw.get())
            self.v_p_w['text']="Ventricular Pulse Width : "+str(cUser.voor.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
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
            self.r_f['text']="Response factor : "+str(cUser.voor.getRF())
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
                    info=main.serial_Communication(4,cUser.voor.getLRL(),0,cUser.voor.getVPW(),round(cUser.voor.getVA()*10),0,0,0,cUser.voor.getRECOVT()*60,cUser.voor.getRF(),cUser.voor.getMSR(),0,cUser.voor.getATV(),cUser.voor.getREACT())
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
            self.lrl.set(cUser.voor.getLRL())
            self.url.set(cUser.voor.getURL())
            self.va.set(cUser.voor.getVA())
            self.vpw.set(cUser.voor.getVPW())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()