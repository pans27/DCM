from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
import main

class AOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=57,relheight=0.9,relwidth=1)
        self.write_aoo_parameters()

    def write_aoo_parameters(self): #creating labels and entry fields
        from global_ import cUser
        self.title=Label(self,text="AOO Parameters",font=("Times New Roman",30))
        self.title.place(x=220,y=40)
        self.current=Label(self,text="Stored values : ",font=("Times New Roman",16))
        self.current.place(x=100,y=120)
        self.l_r_l=Label(self,text="Lower Rate Limit : "+str(cUser.aoo.getLRL()),font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.lrl=StringVar()
        self.l_r_l_E=Entry(self,textvariable=self.lrl,font=("Times New Roman",14))
        self.lrl.set(cUser.aoo.getLRL())
        self.l_r_l_E.place(x=350,y=160)
        self.url=StringVar()
        self.u_r_l=Label(self,text="Upper Rate Limit : "+str(cUser.aoo.getURL()),font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,textvariable=self.url,font=("Times New Roman",14))
        self.url.set(cUser.aoo.getURL())
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude : "+str(cUser.aoo.getAA()),font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.aa=StringVar()
        self.a_a_E=Entry(self,textvariable=self.aa,font=("Times New Roman",14))
        self.aa.set(cUser.aoo.getAA())
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width : "+str(cUser.aoo.getAPW()),font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.apw=StringVar()
        self.a_p_w_E=Entry(self,textvariable=self.apw,font=("Times New Roman",14))
        self.apw.set(cUser.aoo.getAPW())
        self.a_p_w_E.place(x=350,y=280)

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
    
    def confirmPressed(self,e): # check each parameter to see if there is an error, keep track of the errors
        from global_ import cUser
        prompt=messagebox.askquestion("Message","Values that does not match the specified increment may be rounded, save?")
        if(prompt=="no"):
            return
        errors=0
        text=""
        try:
            cUser.aoo.setLRL(self.lrl.get())
            self.l_r_l['text']="Lower Rate Limit : "+str(cUser.aoo.getLRL())
        except TypeError:
            text=text+"LRL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"LRL must be between 30 and 175\n"
            errors+=1
        try:
            cUser.aoo.setURL(self.url.get())
            self.u_r_l['text']="Upper Rate Limit : "+str(cUser.aoo.getURL())
        except TypeError:
            text=text+"URL must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"URL must be between 50 and 175\n"
            errors+=1
        try:
            cUser.aoo.setAA(self.aa.get())
            self.a_a['text']="Atrial Amplitude : "+str(cUser.aoo.getAA())
        except TypeError:
            text=text+"AA must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"AA must be between 0 and 5.0\n"
            errors+=1
        try:
            cUser.aoo.setAPW(self.apw.get())
            self.a_p_w['text']="Atrial Pulse Width : "+str(cUser.aoo.getAPW())
        except TypeError:
            text=text+"APW must be numeric\n"
            errors+=1
        except IndexError:
            text=text+"APW must be between 1 and 30\n"
            errors+=1
        if(errors==0): #print out errors ifthere are any, store the changes without error to hard drive
            messagebox.showinfo("Message","Changes saved")
            main.storeD()
        elif(errors<4):
            messagebox.showinfo("Message","There is/are "+str(errors)+" error(S):\n"+text+"Other values are saved")
            main.storeD()
        else:
            messagebox.showinfo("Message","There are "+str(errors)+" error(S):\n"+text)

    def clearPressed(self,e):
        from global_ import cUser
        prompt=messagebox.askquestion("Message","All unsaved changes will be discarded, are you sure?") # set all entry field to show the parameter stored
        if(prompt=='yes'):
            self.lrl.set(cUser.aoo.getLRL())
            self.url.set(cUser.aoo.getURL())
            self.aa.set(cUser.aoo.getAA())
            self.apw.set(cUser.aoo.getAPW())

    def backPressed(self,e):
        main.Modes(master=self.master)
        self.destroy()