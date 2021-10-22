from tkinter import *
from tkinter import messagebox
import tkinter
from user import *
import pickle

#welcome screeen

class Modes(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.displaymodes()

    def displaymodes(self):
        self.AOO=Button(self,width=10,height=2)
        self.AOO["text"]="AOO"
        self.AOO.place(x=200,y=100)
        self.AAI=Button(self,width=10,height=2)
        self.AAI["text"]="AAI"
        self.AAI.place(x=420,y=100)
        self.VOO=Button(self,width=10,height=2)
        self.VOO["text"]="VOO"
        self.VOO.place(x=200,y=180)
        self.VVI=Button(self,width=10,height=2)
        self.VVI["text"]="VVI"
        self.VVI.place(x=420,y=180)
        self.DOO=Button(self,width=10,height=2)
        self.DOO["text"]="DOO"
        self.DOO.place(x=200,y=260)
        self.VOOR=Button(self,width=10,height=2)
        self.VOOR["text"]="VOOR"
        self.VOOR.place(x=420,y=260)
        self.AOOR=Button(self,width=10,height=2)
        self.AOOR["text"]="AOOR"
        self.AOOR.place(x=200,y=340)
        self.AAIR=Button(self,width=10,height=2)
        self.AAIR["text"]="AAIR"
        self.AAIR.place(x=420,y=340)
        self.VVIR=Button(self,width=10,height=2)
        self.VVIR["text"]="VVIR"
        self.VVIR.place(x=200,y=420)
        self.DOOR=Button(self,width=10,height=2)
        self.DOOR["text"]="DOOR"
        self.DOOR.place(x=420,y=420)
        self.AOO.bind("<Button-1>",self.AOOPressed)
        self.AAI.bind("<Button-1>",self.AAIPressed)
        self.VOO.bind("<Button-1>",self.VOOPressed)
        self.VVI.bind("<Button-1>",self.VVIPressed)
        # self.DOO.bind("<Button-1>",self.DOOPressed)
        # self.VOOR.bind("<Button-1>",self.VOORPressed)
        # self.AOOR.bind("<Button-1>",self.AOORPressed)
        # self.AAIR.bind("<Button-1>",self.AAIRPressed)
        # self.VVIR.bind("<Button-1>",self.VVIRPressed)
        # self.DOOR.bind("<Button-1>",self.DOORPressed)
    
    def AOOPressed(self,e):
        AOOparameter(master=self.master)
        self.destroy()

    def AAIPressed(self,e):
        AAIparameter(master=self.master)
        self.destroy() 
    
    def VOOPressed(self,e):
        VOOparameter(master=self.master)
        self.destroy() 
    
    def VVIPressed(self,e):
        VVIparameter(master=self.master)
        self.destroy() 
    
    # def DOOPressed(self,e):
    #     DOOparameter(master=self.master)
    #     self.destroy()

    # def VOORPressed(self,e):
    #     VOORparameter(master=self.master)
    #     self.destroy() 
    
    # def AOORPressed(self,e):
    #     AOORparameter(master=self.master)
    #     self.destroy() 
    
    # def AAIRPressed(self,e):
    #     AAIRparameter(master=self.master)
    #     self.destroy() 
    
    # def VVIRPressed(self,e):
    #     VVIRparameter(master=self.master)
    #     self.destroy() 
    
    # def DOORPressed(self,e):
    #     VOORparameter(master=self.master)
    #     self.destroy() 
    
class AOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.write_aoo_parameters()

    def write_aoo_parameters(self):
        self.message=Label(self,text="AOO Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.l_r_l_E=Entry(self,font=("Times New Roman",14))
        self.l_r_l_E.place(x=350,y=160)
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,font=("Times New Roman",14),show="*")
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.a_a_E=Entry(self,font=("Times New Roman",14))
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.a_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.a_p_w_E.place(x=350,y=280)
        
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=320)
        self.v_a_E=Entry(self,font=("Times New Roman",14))
        self.v_a_E.place(x=350,y=320)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=360)
        self.v_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.v_p_w_E.place(x=350,y=360)
        self.vrp=Label(self,text="VRP :",font=("Times New Roman",14))
        self.vrp.place(x=100,y=400)
        self.vrp_E=Entry(self,font=("Times New Roman",14))
        self.vrp_E.place(x=350,y=400)
        self.arp=Label(self,text="ARP :",font=("Times New Roman",14))
        self.arp.place(x=100,y=440)
        self.arp_E=Entry(self,font=("Times New Roman",14),show="*")
        self.arp_E.place(x=350,y=440)


        self.comfirmB=Button(self,width=10,height=2)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=320,y=500)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        messagebox.showinfo("Message","saved")

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
        

        
class VOOparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.write_voo_parameters()

    def write_voo_parameters(self):
        self.message=Label(self,text="VOO Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.l_r_l_E=Entry(self,font=("Times New Roman",14))
        self.l_r_l_E.place(x=350,y=160)
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,font=("Times New Roman",14),show="*")
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.a_a_E=Entry(self,font=("Times New Roman",14))
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.a_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.a_p_w_E.place(x=350,y=280)
        
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=320)
        self.v_a_E=Entry(self,font=("Times New Roman",14))
        self.v_a_E.place(x=350,y=320)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=360)
        self.v_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.v_p_w_E.place(x=350,y=360)
        self.vrp=Label(self,text="VRP :",font=("Times New Roman",14))
        self.vrp.place(x=100,y=400)
        self.vrp_E=Entry(self,font=("Times New Roman",14))
        self.vrp_E.place(x=350,y=400)
        self.arp=Label(self,text="ARP :",font=("Times New Roman",14))
        self.arp.place(x=100,y=440)
        self.arp_E=Entry(self,font=("Times New Roman",14),show="*")
        self.arp_E.place(x=350,y=440)


        self.comfirmB=Button(self,width=10,height=2)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=320,y=500)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        messagebox.showinfo("Message","saved")

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
        
class VVIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.write_vvi_parameters()

    def write_vvi_parameters(self):
        self.message=Label(self,text="VVI Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.l_r_l_E=Entry(self,font=("Times New Roman",14))
        self.l_r_l_E.place(x=350,y=160)
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,font=("Times New Roman",14),show="*")
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.a_a_E=Entry(self,font=("Times New Roman",14))
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.a_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.a_p_w_E.place(x=350,y=280)
        
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=320)
        self.v_a_E=Entry(self,font=("Times New Roman",14))
        self.v_a_E.place(x=350,y=320)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=360)
        self.v_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.v_p_w_E.place(x=350,y=360)
        self.vrp=Label(self,text="VRP :",font=("Times New Roman",14))
        self.vrp.place(x=100,y=400)
        self.vrp_E=Entry(self,font=("Times New Roman",14))
        self.vrp_E.place(x=350,y=400)
        self.arp=Label(self,text="ARP :",font=("Times New Roman",14))
        self.arp.place(x=100,y=440)
        self.arp_E=Entry(self,font=("Times New Roman",14),show="*")
        self.arp_E.place(x=350,y=440)


        self.comfirmB=Button(self,width=10,height=2)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=320,y=500)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        messagebox.showinfo("Message","saved")

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
        

        
class AAIparameter(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(relheight=1,relwidth=1)
        self.write_aai_parameters()

    def write_aai_parameters(self):
        self.message=Label(self,text="AAI Parameters",font=("Times New Roman",30))
        self.message.place(x=220,y=100)
        self.l_r_l=Label(self,text="Lower Rate Limit :",font=("Times New Roman",14))
        self.l_r_l.place(x=100,y=160)
        self.l_r_l_E=Entry(self,font=("Times New Roman",14))
        self.l_r_l_E.place(x=350,y=160)
        self.u_r_l=Label(self,text="Upper Rate Limit :",font=("Times New Roman",14))
        self.u_r_l.place(x=100,y=200)
        self.u_r_l_E=Entry(self,font=("Times New Roman",14),show="*")
        self.u_r_l_E.place(x=350,y=200)
        self.a_a=Label(self,text="Atrial Amplitude :",font=("Times New Roman",14))
        self.a_a.place(x=100,y=240)
        self.a_a_E=Entry(self,font=("Times New Roman",14))
        self.a_a_E.place(x=350,y=240)
        self.a_p_w=Label(self,text="Atrial Pulse Width :",font=("Times New Roman",14))
        self.a_p_w.place(x=100,y=280)
        self.a_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.a_p_w_E.place(x=350,y=280)
        
        self.v_a=Label(self,text="Ventricular Amplitude :",font=("Times New Roman",14))
        self.v_a.place(x=100,y=320)
        self.v_a_E=Entry(self,font=("Times New Roman",14))
        self.v_a_E.place(x=350,y=320)
        self.v_p_w=Label(self,text="Ventricular Pulse Width :",font=("Times New Roman",14))
        self.v_p_w.place(x=100,y=360)
        self.v_p_w_E=Entry(self,font=("Times New Roman",14),show="*")
        self.v_p_w_E.place(x=350,y=360)
        self.vrp=Label(self,text="VRP :",font=("Times New Roman",14))
        self.vrp.place(x=100,y=400)
        self.vrp_E=Entry(self,font=("Times New Roman",14))
        self.vrp_E.place(x=350,y=400)
        self.arp=Label(self,text="ARP :",font=("Times New Roman",14))
        self.arp.place(x=100,y=440)
        self.arp_E=Entry(self,font=("Times New Roman",14),show="*")
        self.arp_E.place(x=350,y=440)


        self.comfirmB=Button(self,width=10,height=2)
        self.comfirmB["text"]="Comfirm"
        self.comfirmB.place(x=320,y=500)
        self.comfirmB.bind("<Button-1>",self.confirmPressed)
        self.back=Button(self,width=10,height=2)
        self.back["text"]="Back"
        self.back.place(relx=0.85,rely=0.9)
        self.back.bind("<Button-1>",self.backPressed)
    
    def confirmPressed(self,e):
        messagebox.showinfo("Message","saved")

    def backPressed(self,e):
        Modes(master=self.master)
        self.destroy()
        

if __name__=='__main__':
    #get users list
    try:
        users=pickle.load(open('users.dat','rb'))
        count=len(users)
    except:
        users= []
        count=0
    print(count)
    root=Tk()
    root.title("Pacemaker User Terminal")
    root.geometry("720x576+100+100")
    root.resizable(False, False)
    Modes(master=root)
    root.mainloop()