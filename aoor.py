from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
import main


class AOORparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aoor_parameters()

    def write_aoor_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="AOOR Parameters",font=("Times New Roman",30))
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aai.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aai.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Maximum Sensor Rate
        self.m_s_r=Label(self,text="Maximum Sensor Rate :",font=("Times New Roman",14))
        self.m_s_r.place(x=100,y=200)
        self.msr=StringVar()
        self.m_s_r_E=Entry(self,textvariable=self.msr,font=("Times New Roman",14))
        self.msr.set(cUser.aai.getAA())
        self.m_s_r_E.place(x=350,y=200)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=650,y=200)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aai.getAA())
        self.a_a_E.place(x=900,y=200)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=240)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aai.getAPW())
        self.a_p_w_E.place(x=350,y=240)
        #Activity Threshold
        self.a_t=Label(self,text="Activity Threshold :",font=("Times New Roman",14))
        self.a_t.place(x=650,y=240)
        self.at=StringVar()
        self.a_t_E=Entry(self,textvariable=self.at,font=("Times New Roman",14))
        self.at.set(cUser.vvi.getVPW())
        self.a_t_E.place(x=900,y=240)
        #Reaction Time
        self.r_t=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_t.place(x=100,y=280)
        self.rt=StringVar()
        self.r_t_E=Entry(self,textvariable=self.rt,font=("Times New Roman",14))
        self.rt.set(cUser.vvi.getVPW())
        self.r_t_E.place(x=350,y=280)
        #Response Factor
        self.r_f=Label(self,text="Reaction Time :",font=("Times New Roman",14))
        self.r_f.place(x=650,y=280)
        self.rf=StringVar()
        self.r_f_E=Entry(self,textvariable=self.rf,font=("Times New Roman",14))
        self.rf.set(cUser.vvi.getVPW())
        self.r_f_E.place(x=900,y=280)
        #Recovery Time
        self.recovery_time=Label(self,text="Recovery Time :",font=("Times New Roman",14))
        self.recovery_time.place(x=100,y=320)
        self.ret=StringVar()
        self.recovery_time_E=Entry(self,textvariable=self.ret,font=("Times New Roman",14))
        self.ret.set(cUser.vvi.getVPW())
        self.recovery_time_E.place(x=350,y=320)

        self.comfirmB=Button(self,width=11,height=3)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=620,y=450)
        self.clearB=Button(self,width=11,height=3)
        self.clearB["text"]="Clear changes"
        self.clearB.place(x=420,y=450)
        #self.clearB.bind("<Button-1>",self.clearPressed)
        #self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)

    # back to the previous page (modes page)
    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()