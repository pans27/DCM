from tkinter import *
from tkinter import messagebox
import tkinter
import main
import egram

class VOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_voo_parameters()

    def write_voo_parameters(self):
        from global_ import cUser
        self.message=Label(self,text="VOO Parameters",font=("Times New Roman",30))
        self.message.place(x=640,anchor = CENTER,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",20))
        self.current.place(x=425,y=120)
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.voo.getLRL()),font=("Times New Roman",18))
        self.l_r_l.place(x=400,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",18))
        self.lrl.set(cUser.voo.getLRL())
        self.l_r_l_E.place(x=650,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.voo.getURL()),font=("Times New Roman",18))
        self.u_r_l.place(x=400,y=220)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",18))
        self.url.set(cUser.voo.getURL())
        self.u_r_l_E.place(x=650,y=220)
        self.v_a=Label(self,text="Ventricular Amplitude : "+str(cUser.voo.getVA()),font=("Times New Roman",18))
        self.v_a.place(x=355,y=280)
        self.va=StringVar()
        self.v_a_E=Entry(self,textvariable=self.va,font=("Times New Roman",18))
        self.va.set(cUser.voo.getVA())
        self.v_a_E.place(x=650,y=280)
        self.v_p_w=Label(self,text="Ventricular Pulse Width : "+str(cUser.voo.getVPW()),font=("Times New Roman",18))
        self.v_p_w.place(x=340,y=340)
        self.vpw=StringVar()
        self.v_p_w_E=Entry(self,textvariable=self.vpw,font=("Times New Roman",18))
        self.vpw.set(cUser.voo.getVPW())
        self.v_p_w_E.place(x=650,y=340)

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
            if(float(self.url.get())<float(self.lrl.get())):
                errors+=1
                text=text+"LRL and URL are conflictd\n"
            else:
                try:
                    cUser.voo.setLRL(self.lrl.get())
                    self.l_r_l['text']="Lower Rate Limit : "+str(cUser.voo.getLRL())
                except TypeError:
                    text=text+"LRL must be numeric\n"
                    errors+=1
                except IndexError:
                    text=text+"LRL must be between 30 and 175, and smaller than URL\n"
                    errors+=1
                try:
                    cUser.voo.setURL(self.url.get())
                    self.u_r_l['text']="Upper Rate Limit : "+str(cUser.voo.getURL())
                except TypeError:
                    text=text+"URL must be numeric\n"
                    errors+=1
                except IndexError:
                    text=text+"URL must be between 50 and 175, and larger than LRL\n"
                    errors+=1
        except:
            text=text+"LRL and URL must be numeric\n"
            errors+=1
        try:
            cUser.voo.setVA(self.va.get())
            self.v_a['text']="Ventricular Amplitude : "+str(cUser.voo.getVA())
        except TypeError:
            text=text+"VA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.voo.setVPW(self.vpw.get())
            self.v_p_w['text']="Ventricular Pulse Width : "+str(cUser.voo.getVPW())
        except TypeError:
            text=text+"VPW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"VPW must be between 0.1 and 1.9\n"
            errors+=1
        if(errors==0):
            main.storeD()
            if(Commu):
                prompt=messagebox.askquestion("Message","Changes saved, Send to connected pacemaker?")
                if(prompt=="yes"):
                    info=main.serial_Communication(1,cUser.voo.getLRL(),0,cUser.voo.getVPW(),cUser.voo.getVA(),0,0,0,0,0,175,0,7,0,2.5,2.5)
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
            self.lrl.set(cUser.voo.getLRL())
            self.url.set(cUser.voo.getURL())
            self.va.set(cUser.voo.getVA())
            self.vpw.set(cUser.voo.getVPW())
            
    def egramPressed(self,e):
        from global_ import Commu
        if(Commu!=0):
            egram.Egram()
        else:
            messagebox.showinfo("Message","Pacemaker not connected")

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()