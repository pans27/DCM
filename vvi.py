from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
import pickle
import main
import egram

class VVIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_vvi_parameters()

    def write_vvi_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="VVI Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=125,y=120)
        #lower rate limit
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.vvi.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.vvi.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        #upper rate limit
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.vvi.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=650,y=160)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.vvi.getURL())
        self.u_r_l_E.place(x=900,y=160)
        #Ventricular Amplitude
        self.v_a=Label(self,text="Ventricular Amplitude : "+str(cUser.vvi.getVA()),font=("Times New Roman",18))
        self.v_a.place(x=55,y=220)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",18))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=350,y=220)
        #Ventricular Pulse Width
        self.v_p_w=Label(self,text="Ventricular Pulse Width : "+str(cUser.vvi.getVPW()),font=("Times New Roman",18))
        self.v_p_w.place(x=590,y=220)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",18))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=900,y=220)
        #Ventricular Sensitivity
        self.v_s=Label(self,text="Ventricular Sensitivity : "+str(cUser.vvi.getVS()),font=("Times New Roman",18))
        self.v_s.place(x=55,y=280)
        self.vts=StringVar()
        self.v_s_E=Entry(self,textvariable=self.vts,font=("Times New Roman",18))
        self.vts.set(cUser.vvi.getVS())
        self.v_s_E.place(x=350,y=280)
        #VRP
        self.v_r_p=Label(self,text="VRP : "+str(cUser.vvi.getVRP()),font=("Times New Roman",18))
        self.v_r_p.place(x=775,y=280)
        self.vrp=StringVar()
        self.v_r_p_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",18))
        self.vrp.set(cUser.vvi.getVRP())
        self.v_r_p_E.place(x=900,y=280)
        #Hysteresis
        self.hysteresis=Label(self,text="Hysteresis : "+str(cUser.vvi.getHYST()),font=("Times New Roman",18))
        self.hysteresis.place(x=720,y=340)
        self.hys=StringVar()
        self.hysteresis_E=Entry(self,textvariable=self.hys,font=("Times New Roman",18))
        self.hys.set(cUser.vvi.getHYST())
        self.hysteresis_E.place(x=900,y=340)
        #Rate Smoothing
        self.r_s=Label(self,text="Rate Smoothing : "+str(cUser.vvi.getRS()),font=("Times New Roman",18))
        self.r_s.place(x=120,y=340)
        self.rs_data = ['0 OFF','3','6','9','12','15','18','21','25']
        self.rs = ttk.Combobox(self, state='readonly',font=("Times New Roman",18))
        self.rs.set(cUser.vvi.getRS())
        self.rs['values'] = self.rs_data
        self.rs.place(x=350,y=340)

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
            cUser.vvi.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.vvi.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.vvi.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.vvi.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.vvi.setVA(self.va.get())
            self.v_a['text']="Ventricular Amplitude : "+str(cUser.vvi.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0.5 and 7.0\n"
            errors+=1
        try:
            cUser.vvi.setVPW(self.vpw.get())
            self.v_p_w['text']="Ventricular Pulse Width : "+str(cUser.vvi.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        try:
            cUser.vvi.setVRP(self.vrp.get())
            self.v_r_p['text']="VRP : "+str(cUser.vvi.getVRP())
        except TypeError:
            text=text+"VRP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VRP must be between 150 and 500\n"
            errors+=1
        try:
            cUser.vvi.setVS(self.vts.get())
            self.v_s['text']="Ventricular Sensitivity : "+str(cUser.vvi.getVS())
        except TypeError:
            text=text+"VS must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VS must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.vvi.setHYST(self.hys.get())
            self.hysteresis['text']="Hysteresis : "+str(cUser.vvi.getHYST())
        except TypeError:
            text=text+"HYST must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"HYST must be between 30 and 175\n"
            errors+=1
        try:
            cUser.vvi.setRS(self.rs.get().split()[0])
            self.r_s['text']="Rate Smoothing : "+str(cUser.vvi.getRS())
        except :
            text=text+"RS not stored\n"
            errors+=1
            
        if(errors==0):
            main.storeD()
            if(Commu):
                prompt=messagebox.askquestion("Message","Changes saved, Send to connected pacemaker?")
                if(prompt=="yes"):
                    info=main.serial_Communication(3,cUser.vvi.getLRL(),0,cUser.vvi.getVPW(),round(cUser.vvi.getVA()*10),0,cUser.vvi.getVRP(),0,0,0,0,0,0,0)
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
            self.lrl.set(cUser.vvi.getLRL())
            self.url.set(cUser.vvi.getURL())
            self.va.set(cUser.vvi.getVA())
            self.vpw.set(cUser.vvi.getVPW())
            self.vts.set(cUser.vvi.getVS())
            self.vrp.set(cUser.vvi.getVRP())
            self.hys.set(cUser.vvi.getHYST())
            self.rs.set(cUser.vvi.getRS())

    def egramPressed(self,e):
        egram.Egram()

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()
