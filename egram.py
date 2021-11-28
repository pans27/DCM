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
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Egram():
    def __init__(self):
        self.aData=np.array([])
        self.vData=np.array([])
        self.vS=False
        self.aS=False
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
        self.plotA.set_xlabel("Sample", fontsize = 10)
        self.plotA.set_ylabel("Voltage (mV)", fontsize = 10)
        self.plotV.set_xlabel("Sample", fontsize = 10)
        self.plotV.set_ylabel("Voltage (mV)", fontsize = 10)
        self.plotA.set_ylim(-6,6)
        self.plotA.set_xlim(0,300)
        self.linesA=self.plotA.plot([],[])[0]
        self.plotV.set_ylim(-6,6)
        self.plotV.set_xlim(0,300)
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
    
    def plot(self):
        try:
            ser = serial.Serial(port="COM"+str(global_.Commu), baudrate=115200)
        except:
            raise PortNotOpenError
        if(self.aS==True and self.vS==True):
            ser.open
            ser.reset_input_buffer()
            ser.write(struct.pack('<2B16H',0x16,0x22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            serialdata=ser.read(16)
            ser.close
            a=-6.6*(struct.unpack('d',serialdata[0:8])[0]-0.5)
            v=-6.6*(struct.unpack('d',serialdata[8:16])[0]-0.5)
            if(len(self.aData)<300):
                self.aData=np.append(self.aData,a)
                self.vData=np.append(self.vData,v)
            else:
                self.aData[0:299]=self.aData[1:300]
                self.vData[0:299]=self.vData[1:300]
                self.aData[299]=a
                self.vData[299]=v
            self.linesA.set_xdata(np.arange(0,len(self.aData)))
            self.linesA.set_ydata(self.aData)
            self.linesV.set_xdata(np.arange(0,len(self.vData)))
            self.linesV.set_ydata(self.vData)
            self.canvas.draw()
        elif(self.aS==True):
            ser.open
            ser.reset_input_buffer()
            ser.write(struct.pack('<2B16H',0x16,0x22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            serialdata=ser.read(16)
            ser.close
            a=-6.6*(struct.unpack('d',serialdata[0:8])[0]-0.5)
            if(len(self.aData)<300):
                self.aData=np.append(self.aData,a)
                self.vData=np.append(self.vData,0)
            else:
                self.aData[0:299]=self.aData[1:300]
                self.vData[0:299]=self.vData[1:300]
                self.aData[299]=a
                self.vData[299]=0
            self.linesA.set_xdata(np.arange(0,len(self.aData)))
            self.linesA.set_ydata(self.aData)
            self.linesV.set_xdata(np.arange(0,len(self.vData)))
            self.linesV.set_ydata(self.vData)
            self.canvas.draw()
        elif(self.vS==True):
            ser.open
            ser.reset_input_buffer()
            ser.write(struct.pack('<2B16H',0x16,0x22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            serialdata=ser.read(16)
            ser.close
            v=-6.6*(struct.unpack('d',serialdata[8:16])[0]-0.5)
            if(len(self.aData)<300):
                self.aData=np.append(self.aData,0)
                self.vData=np.append(self.vData,v)
            else:
                self.aData[0:299]=self.aData[1:300]
                self.vData[0:299]=self.vData[1:300]
                self.aData[299]=0
                self.vData[299]=v
            self.linesA.set_xdata(np.arange(0,len(self.aData)))
            self.linesA.set_ydata(self.aData)
            self.linesV.set_xdata(np.arange(0,len(self.vData)))
            self.linesV.set_ydata(self.vData)
            self.canvas.draw()
        self.window.after(1,self.plot)
    def plot_a(self):
        self.aS = not self.aS

    def plot_v(self):
        self.vS = not self.vS
