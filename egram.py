import time
from tkinter import *
from tkinter import messagebox
import tkinter

from serial.serialutil import PortNotOpenError
from user import *
import pickle
import global_
import serial
import struct

def egram():
    plot=Tk()
    plot.title("Egram") 
    plot.geometry("720x576+50+50")
    plot.resizable(False, False)
    plot.mainloop()

if __name__=='__main__':
    egram()