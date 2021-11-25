from serial import Serial
import struct
mode=1
LR=120
VA=5.0
VPW=1

header = '<2B4Hf2Hf6H'
sp = struct.pack(header,0x16,0x55,mode,LR,0,VPW,VA,0,0,0,0,0,0,0,0,0)

with Serial("COM6",115200) as pacemaker:
    #while True:
    pacemaker.write(sp)
