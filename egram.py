from tkinter import *
import tkinter
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure 
from serial.serialutil import PortNotOpenError
from user import *
import global_
import serial
import struct
import time
from tkinter import * 
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Egram():
    def __init__(self):
        self.aData=np.array([])
        self.vData=np.array([])
        self.tData=np.array([])
        self.vS=True
        self.aS=True
        self.window = Tk()
    
        # setting the title 
        self.window.title('Egram')
    
        # dimensions of the main window
        self.window.geometry("720x576")
        self.egram()
        self.window.mainloop()
    def egram(self):
        # the figure that will contain the plot
        self.fig = Figure(figsize = (7, 7),dpi = 100)
    
        # adding the subplot
        self.plotA = self.fig.add_subplot(211)
        self.plotV = self.fig.add_subplot(212)
        self.fig.subplots_adjust(hspace = 0.5)
        # plotting the graph
        
        self.plotA.set_title('Atrium Signals', fontsize = 12)
        self.plotV.set_title('Ventricle Signals', fontsize = 12)
        self.plotA.set_xlabel("Time (sec)", fontsize = 10)
        self.plotA.set_ylabel("Voltage (V)", fontsize = 10)
        self.plotV.set_xlabel("Time (sec)", fontsize = 10)
        self.plotV.set_ylabel("Voltage (V)", fontsize = 10)
        self.plotA.set_ylim(-6,6)
        self.plotA.set_xlim(0,14)
        self.linesA=self.plotA.plot([],[])[0]
        self.plotV.set_ylim(-6,6)
        self.plotV.set_xlim(0,14)
        self.linesV=self.plotV.plot([],[])[0]
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig,master = self.window)  
        self.canvas.draw()
    
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()
    
        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.window)
        self.toolbar.update()
    
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()
        
        self.window.update()
        self.a = tkinter.Button(self.window, text = "Atrium", font = ('calbiri',12),command = lambda: self.plot_a())
        self.a.place(x = 100, y = 280 )

        self.window.update()
        self.v = tkinter.Button(self.window, text = "Ventricle", font = ('calbiri',12), command = lambda:self.plot_v())
        self.v.place(x = self.a.winfo_x()+self.a.winfo_reqwidth() + 20, y = 280)
        self.window.update()
        #ser.reset_input_buffer()
        self.window.after(1,self.plot)
        self.start=time.time()
    
    def plot(self):
        try:
            with serial.Serial(port="COM"+str(global_.Commu), baudrate=115200) as ser:
                ser.open
                ser.reset_input_buffer()
                ser.write(struct.pack('<2B10fH',0x16,0x22,0,0,0,0,0,0,0,0,0,0,0))
                serialdata=ser.read(16)
                ser.close
        except:
            self.window.destroy()
            messagebox.showinfo("Message","Pacemaker not connected")
        a=-6.6*(struct.unpack('d',serialdata[0:8])[0]-0.5)
        v=-6.6*(struct.unpack('d',serialdata[8:16])[0]-0.5)
        if(len(self.aData)<300):
            self.aData=np.append(self.aData,a)
            self.vData=np.append(self.vData,v)
            self.tData=np.append(self.tData,time.time()-self.start)
        else:
            self.aData[0:299]=self.aData[1:300]
            self.vData[0:299]=self.vData[1:300]
            self.aData[299]=a
            self.vData[299]=v
            self.tData[0:299]=self.tData[1:300]
            self.tData[299]=time.time()-self.start
            self.plotA.set_xlim(self.tData[0],self.tData[299])
            self.plotV.set_xlim(self.tData[0],self.tData[299])
        self.linesA.set_xdata(self.tData)
        self.linesA.set_ydata(self.aData)
        self.linesV.set_xdata(self.tData)
        self.linesV.set_ydata(self.vData)
        self.canvas.draw()
        self.window.after(1,self.plot)
    def plot_a(self):
        self.aS = not self.aS
        self.plotA.set_visible(self.aS)


    def plot_v(self):
        self.vS = not self.vS
        self.plotV.set_visible(self.vS)
