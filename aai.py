from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import pickle
import main
import egram
class AAIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aai_parameters()

    def write_aai_parameters(self):
        from global_ import cUser
        from global_ import Commu
        self.message=Label(self,text="AAI Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=160,y=120)
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.aai.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.aai.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.aai.getAA()),font=("Times New Roman",18))
        self.a_a.place(x=110,y=220)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",18))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=350,y=220)
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.aai.getAPW()),font=("Times New Roman",18))
        self.a_p_w.place(x=640,y=220)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",18))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=900,y=220)
        #Atrial Sensitivity
        self.a_s=Label(self,text="Atrial Sensitivity : "+str(cUser.aai.getAS()),font=("Times New Roman",18))
        self.a_s.place(x=110,y=280)
        self.ats=StringVar()
        self.a_s_E=Entry(self,textvariable=self.ats,font=("Times New Roman",18))
        self.ats.set(cUser.aai.getAS())
        self.a_s_E.place(x=350,y=280)
        #ARP
        self.a_r_p=Label(self,text="ARP : "+str(cUser.aai.getARP()),font=("Times New Roman",18))
        self.a_r_p.place(x=775,y=280)
        self.arp=StringVar()
        self.a_r_p_E=Entry(self,textvariable=self.arp,font=("Times New Roman",18))
        self.arp.set(cUser.aai.getARP())
        self.a_r_p_E.place(x=900,y=280)
        #PVARP
        self.p_v_a_r_p=Label(self,text="PVARP : "+str(cUser.aai.getPVARP()),font=("Times New Roman",18))
        self.p_v_a_r_p.place(x=195,y=340)
        self.pvarp=StringVar()
        self.p_v_a_r_p_E=Entry(self,textvariable=self.pvarp,font=("Times New Roman",18))
        self.pvarp.set(cUser.aai.getPVARP())
        self.p_v_a_r_p_E.place(x=350,y=340)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis : "+str(cUser.aai.getHYST()),font=("Times New Roman",18))
        self.hysteresis.place(x=720,y=340)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",18))
        self.hys.set(cUser.aai.getHYST())
        self.hysteresis_E.place(x=900,y=340)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing : "+str(cUser.aai.getRS()),font=("Times New Roman",18))
        self.r_s.place(x=120,y=400)
        self.rs_data = ['0 OFF','3','6','9','12','15','18','21','25']
        self.rs = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.rs.set(cUser.aai.getRS())
        self.rs['values'] = self.rs_data
        self.rs.place(x=350,y=400)

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
            cUser.aai.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.aai.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.aai.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.aai.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175, and larger than LRL\n"
            errors+=1
        try:
            cUser.aai.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.aai.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0.5 and 5.0\n"
            errors+=1
        try:
            cUser.aai.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.aai.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
        try:
            cUser.aai.setARP(self.arp.get())
            self.a_r_p['text']="ARP : "+str(cUser.aai.getARP())
        except TypeError:
            text=text+"ARP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"ARP must be between 150 and 500\n"
            errors+=1
        try:
            cUser.aai.setAS(self.ats.get())
            self.a_s['text']="Atrial Sensitivity : "+str(cUser.aai.getAS())
        except TypeError:
            text=text+"AS must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AS must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.aai.setPVARP(self.pvarp.get())
            self.p_v_a_r_p['text']="PVARP : "+str(cUser.aai.getPVARP())
        except TypeError:
            text=text+"PVARP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"PVARP must be between 150 and 500\n"
            errors+=1
        try:
            cUser.aai.setHYST(self.hys.get())
            self.hysteresis['text']="Hysteresis : "+str(cUser.aai.getHYST())
        except TypeError:
            text=text+"HYST must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"HYST must be between 30 and 175\n"
            errors+=1
        try:
            cUser.aai.setRS(self.rs.get().split()[0])
            self.r_s['text']="Rate Smoothing : "+str(cUser.aai.getRS())
        except :
            text=text+"RS not stored\n"
            errors+=1

        if(errors==0):
            main.storeD()
            if(Commu):
                prompt=messagebox.askquestion("Message","Changes saved, Send to connected pacemaker?")
                if(prompt=="yes"):
                    info=main.serial_Communication(2,cUser.aai.getLRL(),cUser.aai.getAPW(),0,0,cUser.aai.getARP(),0,cUser.aai.getAA(),0,0,0,0,7,0)
                    messagebox.showinfo("Message",info)
            else:
                messagebox.showinfo("Message","Changes saved")
        else:
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Values may not be saved")
            main.storeD()

    def egramPressed(self,e):
        egram.Egram()
    
    def clearPressed(self,e):
        from global_ import cUser
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?")
        if(prompt=='yes'):
            self.lrl.set(cUser.aai.getLRL())
            self.url.set(cUser.aai.getURL())
            self.aa.set(cUser.aai.getAA())
            self.apw.set(cUser.aai.getAPW())
            self.arp.set(cUser.aai.getARP())
            self.ats.set(cUser.aai.getAS())
            self.pvarp.set(cUser.aai.getPVARP())
            self.hys.set(cUser.aai.getHYST())
            self.rs.set(cUser.aai.getRS())
    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
