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

def plot():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (7, 7),dpi = 100)
  
    # list of squares
    y = [i**2 for i in range(101)]
  
    # adding the subplot
    plotA = fig.add_subplot(211)
    plotB = fig.add_subplot(212)
    fig.subplots_adjust(hspace = 0.5)
    # plotting the graph
    plotA.plot(y)
    plotB.plot(y)
    plotA.set_title('Atrium Signals', fontsize = 12)
    plotB.set_title('Ventricle Signals', fontsize = 12)
    plotA.set_xlabel("Time (ms)", fontsize = 10)
    plotA.set_ylabel("Voltage (mV)", fontsize = 10)
    plotB.set_xlabel("Time (ms)", fontsize = 10)
    plotB.set_ylabel("Voltage (mV)", fontsize = 10)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
window = Tk()
  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("720x576")
  
# button that displays the plot

  
# place the button 
# in main window
plot()
  
# run the gui
window.mainloop()