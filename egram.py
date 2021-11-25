import time
from tkinter import *
from tkinter import messagebox
import tkinter
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure 
from serial.serialutil import PortNotOpenError
from user import *
import pickle
import global_
import serial
import struct
import matplotlib
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class Egram():
    def __init__(self):
        self.aData=np.array([])
        self.vData=np.array([])
        self.sData=np.array([])
        self.vS=False
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
        self.plotA.set_xlabel("Time (ms)", fontsize = 10)
        self.plotA.set_ylabel("Voltage (mV)", fontsize = 10)
        self.plotV.set_xlabel("Time (ms)", fontsize = 10)
        self.plotV.set_ylabel("Voltage (mV)", fontsize = 10)
        self.plotA.set_ylim(-6,6)
        self.plotA.set_xlim(0,400)
        self.linesA=self.plotA.plot([],[])[0]
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
        self.start = tkinter.Button(self.window, text = "Start", font = ('calbiri',12),command = lambda: self.plot_start())
        self.start.place(x = 100, y = 450 )

        self.window.update()
        self.stop = tkinter.Button(self.window, text = "Stop", font = ('calbiri',12), command = lambda:self.plot_stop())
        self.stop.place(x = self.start.winfo_x()+self.start.winfo_reqwidth() + 20, y = 450)
        self.window.update()
        self.close = tkinter.Button(self.window, text = "Close", font = ('calbiri',12), command = lambda:self.plot_close())
        self.close.place(x = self.stop.winfo_x()+self.stop.winfo_reqwidth() + 20, y = 450)
        #ser.reset_input_buffer()
        self.window.after(1,self.plot)
    
    def plot(self):
        if global_.Commu  == 3:
            ser = serial.Serial(port="COM3", baudrate=115200)
        elif global_.Commu  == 4:
            ser = serial.Serial(port="COM4", baudrate=115200)
        elif global_.Commu  == 5:
            ser = serial.Serial(port="COM5", baudrate=115200)
        elif global_.Commu  == 6:
            ser = serial.Serial(port="COM6", baudrate=115200)
        else:
            raise PortNotOpenError
        if(self.aS==True):
            ser.open
            ser.write(struct.pack('<2B16H',0x16,0x22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
            #time.sleep(0.5)
            serialdata=ser.read(48)
            ser.close
            print(struct.unpack('d',serialdata[32:40])[0])
            if(len(self.sData)<100):
                self.aData=np.append(self.aData,struct.unpack('d',serialdata[32:40])[0])
                self.vData=np.append(self.vData,struct.unpack('d',serialdata[40:48])[0])
            else:
                self.aData[0:99]=self.aData[1:100]
                self.vData[0:99]=self.vData[1:100]
                self.aData[99]=struct.unpack('d',serialdata[32:40])[0]
                self.vData[99]=struct.unpack('d',serialdata[40:48])[0]
            print(self.aData[len(self.aData)-1])
            self.linesA.set_xdata(np.arange(0,len(self.aData)))
            self.linesA.set_ydata(self.aData)
            self.canvas.draw()
        self.window.after(25,self.plot)
    def plot_start(self):
        self.aS = True

    def plot_stop(self):
        self.aS = False
    
    def plot_close(self):
        del self
