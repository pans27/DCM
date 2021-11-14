from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
import main


class VVIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_vvi_parameters()

    def write_vvi_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="VVI Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=50)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.vvi.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.vvi.getURL())
        self.u_r_l_E.place(x=350,y=200)
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=240)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",14))
        self.va.set(cUser.vvi.getVA())
        self.v_a_E.place(x=350,y=240)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=280)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",14))
        self.vpw.set(cUser.vvi.getVPW())
        self.v_p_w_E.place(x=350,y=280)
        self.v_r_p=Label(self,text="VRP :",font=("Times New Roman",14))
        self.v_r_p.place(x=100,y=320)
        self.vrp=StringVar()
        self.vrp_E=Entry(self,textvariable=self.vrp,font=("Times New Roman",14))
        self.vrp.set(cUser.vvi.getVRP())
        self.vrp_E.place(x=350,y=320)

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
            cUser.vvi.setLRL(self.lrl.get())
            self.lrl.set(cUser.vvi.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.vvi.setURL(self.url.get())
            self.url.set(cUser.vvi.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.vvi.setVA(self.va.get())
            self.va.set(cUser.vvi.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0.5 and 7.0\n"
            errors+=1
        try:
            cUser.vvi.setVPW(self.vpw.get())
            self.vpw.set(cUser.vvi.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        try:
            cUser.vvi.setVRP(self.vrp.get())
            self.vrp.set(cUser.vvi.getVRP())
        except TypeError:
            text=text+"VRP must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VRP must be between 150 and 500\n"
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
            self.lrl.set(cUser.vvi.getLRL())
            self.url.set(cUser.vvi.getURL())
            self.va.set(cUser.vvi.getVA())
            self.vpw.set(cUser.vvi.getVPW())
            self.vrp.set(cUser.vvi.getVRP())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()