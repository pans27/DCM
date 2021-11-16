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
        self.message.place(x=420,y=50)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=380,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.doo.getLRL())
        self.l_r_l_E.place(x=630,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=380,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.doo.getURL())
        self.u_r_l_E.place(x=630,y=200)
        #Fixed AV Dealy
        self.fixed_AV_delay=Label(self,text="Fixed AV Dealy :",font=("Times New Roman",14))
        self.fixed_AV_delay.place(x=380,y=240)
        self.fad=StringVar()
        self.fixed_AV_delay_E=Entry(self,textvariable=self.fad,font=("Times New Roman",14))
        self.fad.set(cUser.doo.getAA())
        self.fixed_AV_delay_E.place(x=630,y=240)
        #Atrial Amplitude
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=380,y=280)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.doo.getAA())
        self.a_a_E.place(x=630,y=280)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=380,y=320)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.doo.getVA())
        self.v_a_E.place(x=630,y=320)
        #Atrial Pulse Width
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=380,y=360)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.doo.getAPW())
        self.a_p_w_E.place(x=630,y=360)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=380,y=400)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.doo.getVPW())
        self.v_p_w_E.place(x=630,y=400)

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