from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import main
import egram

class AOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aoor_parameters()

    def write_aoor_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="AOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=125,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.aoor.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.aoor.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.aoor.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.aoor.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate : "+str(cUser.aoor.getMSR()),font=("Times New Roman",18))
        self.m_s_r.place(x=55,y=220)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",18))
        self.msr.set(cUser.aoor.getMSR())
        self.m_s_r_E.place(x=350,y=220)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.aoor.getAA()),font=("Times New Roman",18))
        self.a_a.place(x=655,y=220)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",18))
        self.aa.set(cUser.aoor.getAA())
        self.a_a_E.place(x=900,y=220)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.aoor.getAPW()),font=("Times New Roman",18))
        self.a_p_w.place(x=95,y=280)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",18))
        self.apw.set(cUser.aoor.getAPW())
        self.a_p_w_E.place(x=350,y=280)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold : "+str(cUser.aoor.getAT()),font=("Times New Roman",18))
        self.a_t.place(x=640,y=280)
        self.at_data = ['1.13 V-Low', '1.25 Low', '1.4 Med-Low', '1.6 Med','2 Med-High', '2.4 High', '3 V-High']
        self.at_roll = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.at_roll['values'] = self.at_data
        self.at_roll.set(cUser.aoor.getATV())
        self.at_roll.place(x=900,y=280)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time : "+str(cUser.aoor.getREACT()),font=("Times New Roman",18))
        self.r_t.place(x=130,y=340)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",18))
        self.rt.set(cUser.aoor.getREACT())
        self.r_t_E.place(x=350,y=340)
        #Response Factor
        self.r_f=Label(self,text="Response Factor : "+str(cUser.aoor.getRF()),font=("Times New Roman",18))
        self.r_f.place(x=660,y=340)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",18))
        self.rf.set(cUser.aoor.getRF())
        self.r_f_E.place(x=900,y=340)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time : "+str(cUser.aoor.getRECOVT()),font=("Times New Roman",18))
        self.recovery_time.place(x=120,y=400)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",18))
        self.ret.set(cUser.aoor.getRECOVT())
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
        self.egramB.bind("<Button-1>",self.egramPressed)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
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
            if(float(self.url.get())<float(self.lrl.get()) and float(self.msr.get())<float(self.lrl.get()) and float(self.url.get())<float(self.msr.get())):
                errors+=1
                text=text+"LRL, URL, and MSR are conflictd\n"
            else:
                try:
                    cUser.aoo.setLRL(self.lrl.get())
                    self.l_r_l['text']="Lower Rate Limit : "+str(cUser.aoo.getLRL())
                except TypeError:
                    text=text+"LRL must be numeric\n"
                    errors+=1
                except IndexError:
                    text=text+"LRL must be between 30 and 175, and smaller than URL\n"
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
                    cUser.aoor.setMSR(self.msr.get())
                    self.m_s_r['text']="Maximum Sensor Rate : "+str(cUser.aoor.getMSR())
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
            cUser.aoor.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.aoor.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0 and 5.0\n"
            errors+=1
            
        try:
            cUser.aoor.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.aoor.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
            
        try:
            cUser.aoor.setAT(self.at_roll.get().split()[0])
            self.a_t['text']="Activity Threshold : "+str(cUser.aoor.getAT())
        except :
            text=text+"Activity Threshold not stored\n"
            errors+=1
            
        try:
            cUser.aoor.setREACT(self.rt.get())
            self.r_t['text']="Reaction Time : "+str(cUser.aoor.getREACT())
        except TypeError:
            text=text+"Reaction Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Reaction Time must be between 10s and 50s\n"
            errors+=1
            
        try:
            cUser.aoor.setRF(self.rf.get())
            self.r_f['text']="Response Factor : "+str(cUser.aoor.getRF())
        except TypeError:
            text=text+"Response factor must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Response factor must be between 1 and 16\n"
            errors+=1

        try:
            cUser.aoor.setRECOVT(self.ret.get())
            self.recovery_time['text']="Recovery Time : "+str(cUser.aoor.getRECOVT())
        except TypeError:
            text=text+"Recovery Time must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"Recovery Time must be between 2 and 16\n"
            errors+=1
        
        if(errors==0): #print out errors ifthere are any, store the changes without error to hard drive
            main.storeD()
            if(Commu):
                prompt=messagebox.askquestion("Message","Changes saved, Send to connected pacemaker?")
                if(prompt=="yes"):
                    info=main.serial_Communication(5,cUser.aoor.getLRL(),cUser.aoor.getAPW(),0,0,0,0,cUser.aoor.getAA(),cUser.aoor.getRECOVT()*60,cUser.aoor.getRF(),cUser.aoor.getMSR(),0,cUser.aoor.getATV(),cUser.aoor.getREACT(),0,0)
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
            self.lrl.set(cUser.aoor.getLRL())
            self.url.set(cUser.aoor.getURL())
            self.aa.set(cUser.aoor.getAA())
            self.apw.set(cUser.aoor.getAPW())
            self.at_roll.set(cUser.aoor.getATV())
            self.rt.set(cUser.aoor.getREACT())
            self.rf.set(cUser.aoor.getRF())
            self.ret.set(cUser.aoor.getRECOVT())

    def egramPressed(self,e):
        from global_ import Commu
        if(Commu!=0):
            egram.Egram()
        else:
            messagebox.showinfo("Message","Pacemaker not connected")

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
