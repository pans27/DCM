# November 28, 2021
# Author: Group 5
# 3k04 DCM assignment 2 door parameters

class Doorp:
    def __init__(self):
        self.__lrl = 60
        self.__url = 120
        self.__msr = 120
        self.__favd = 150
        self.__aa=5.0
        self.__apw = 1
        self.__va=5.0
        self.__vpw = 1
        self.__at = 4 #default is med, high is 6, med is 4, low is 2
        self.__reactT = 30
        self.__rf = 8
        self.__recovT = 300 #in s (i.e. 5min)

    def getLRL(self):
        return self.__lrl

    def getURL(self):
        return self.__url

    def getMSR(self):
        return self.__msr
    
    def getFAVD(self):
        return self.__favd

    def getAA(self):
        if(self.__aa):
            return self.__aa 
        else:
            return 'OFF'

    def getAPW(self):
        return self.__apw

    def getVA(self):
        if(self.__va):
            return self.__va 
        else:
            return 'OFF'

    def getVPW(self):
        return self.__vpw
    
    def getAT(self):
        if(self.__at==1):
            return 'V-L'
        elif(self.__at==2):
            return 'L'
        elif(self.__at==3):
            return 'M-L'
        elif(self.__at==4):
            return 'M'
        elif(self.__at==5):
            return 'M-H'
        elif(self.__at==6):
            return 'H'
        elif(self.__at==7):
            return 'V-H'

    def getATV(self):
        return self.__at

    def getREACT(self):
        return self.__reactT

    def getRF(self):
        return self.__rf

    def getRECOVT(self):
        return round(self.__recovT/60)

    def setLRL(self, val):
        if (self.__is_num(val)):
            num = 5 * round(float(val) / 5)
            if (round(float(val)) <= 90 and round(float(val)) >= 50):
                self.__lrl = round(float(val))
            elif ((num <= 50 and num >= 30) or (num <= 175 and num >= 90)):
                self.__lrl = num
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self, val):
        if (self.__is_num(val)):
            num = 5 * round(float(val) / 5)
            if (num <= 175 and num >= 50 and num>=self.__lrl):
                self.__url = num
            else:
                raise IndexError
        else:
            raise TypeError
        
    def setFAVD(self,val):
        if (self.__is_num(val)):
            if (int(round(float(val), -1)) <= 300 and int(round(float(val), -1)) >= 70):
                self.__favd = int(round(float(val), -1))
            else:
                raise IndexError
        else:
            raise TypeError

    def setMSR(self, val):
        if (self.__is_num(val)):
            num = 5 * round(float(val) / 5)
            if (num <= 175 and num >= 50 and num<=self.__url and num>=self.__lrl):
                self.__msr = num
            else:
                raise IndexError
        else:
            raise TypeError

    def setAA(self, val):
        if(val.casefold()=='off'.casefold()):
            self.__aa = 0
            return
        if (self.__is_num(val)):
            num =round(float(val),1)
            if (num <= 5.0 and num >= 0.1):
                self.__aa = num
            elif (round(float(val), 1) == 0):
                self.__aa = 0
            else:
                raise IndexError
        else:
            raise TypeError

    def setAPW(self,val):
        if(self.__is_num(val)):
            if(round(float(val))<=30 and round(float(val))>=1):
                self.__apw=round(float(val))
            else:
                raise IndexError      
        else:
            raise TypeError
    
    def setVA(self, val):
        if(val.casefold()=='off'.casefold()):
            self.__va = 0
            return
        if (self.__is_num(val)):
            num =round(float(val),1)
            if (num <= 5.0 and num >= 0.1):
                self.__va = num
            elif (round(float(val), 1) == 0):
                self.__va = 0
            else:
                raise IndexError
        else:
            raise TypeError

    def setVPW(self,val):
        if(self.__is_num(val)):
            if(round(float(val))<=30 and round(float(val))>=1):
                self.__vpw=round(float(val))
            else:
                raise IndexError      
        else:
            raise TypeError
        
    def setAT(self,val):
        self.__at =round(float(val))


    def setREACT(self,val):
        if (self.__is_num(val)):
            num = 10 * round(float(val) / 10)
            if (num <= 50 and num >= 10):
                self.__reactT = num 
            else:
                raise IndexError
        else:
            raise TypeError

    def setRF(self,val):
        if (self.__is_num(val)):
            if (round(float(val)) <= 16 and round(float(val)) >= 1):
                self.__rf = round(float(val))
            else:
                raise IndexError
        else:
            raise TypeError

    def setRECOVT(self,val):
        if (self.__is_num(val)):
            if ( round(float(val)) <= 16 and round(float(val)) >= 2):
                self.__recovT = round(float(val))*60
            else:
                raise IndexError
        else:
            raise TypeError

    def __is_num(self, s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
