# November 28, 2021
# Author: Group 5
# 3k04 DCM assignment 2 aair parameters

class Aair:
    def __init__(self):
        self.__lrl = 60
        self.__url = 120
        self.__msr = 120
        self.__aaReg = 3.5
        self.__aaUnreg = 3.75
        self.__apw = 0.4
        self.__as = 0.75
        self.__arp = 250
        self.__pvarp = 250
        self.__isHyst = False
        self.__hyst = 60
        self.__isRs = False
        self.__rs = 3
        self.__at = 4 #default is med, high is 8, med is 4, low is 2
        self.__reactT = 30000 #in ms (i.e. 30s)
        self.__rf = 8
        self.__recovT = 300000 #in ms (i.e. 5min)

    def getLRL(self):
        return self.__lrl

    def getURL(self):
        return self.__url

    def getMSR(self):
        return self.__msr

    def getAAReg(self):
        return self.__aaReg

    def getAAUnreg(self):
        return self.__aaUnreg

    def getAPW(self):
        return self.__apw

    def getAS(self):
        return self.__as

    def getARP(self):
        return self.__arp

    def getPVARP(self):
        return self.__pvarp

    def getisHYST(self):
        return self.__isHyst

    def getHYST(self):
        return self.__hyst

    def getisRS(self):
        return self.__isRs
    
    def getRS(self):
        return self.__rs
    
    def getAT(self):
        return self.__at

    def getREACT(self):
        return self.__reactT

    def getRF(self):
        return self.__rf

    def getRECOVT(self):
        return self.__recovT

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
            if (num <= 175 and num >= 50):
                self.__url = num
            else:
                raise IndexError
        else:
            raise TypeError

    def setMSR(self, val):
        if (self.__is_num(val)):
            num = 5 * round(float(val) / 5)
            if (num <= 175 and num >= 50):
                self.__msr = num
            else:
                raise IndexError
        else:
            raise TypeError

    def setAAReg(self, val):
        if (self.__is_num(val)):
            num = 0.5 * round(float(val) / 0.5)
            if (round(float(val), 1) <= 3.2 and round(float(val), 1) >= 0.5):
                self.__aaReg = round(float(val), 1)
            elif (num <= 7.0 and num >= 3.5):
                self.__aaReg = num
            elif (round(float(val), 1) == 0):
                self.__aaReg = 0
            else:
                raise IndexError
        else:
            raise TypeError

    def setAAUnreg(self, val):
        if (self.__is_num(val)):
            num = 1.25 * round(float(val) / 1.25)
            if (round(float(val), 2) <= 5.00 and round(float(val), 2) >= 1.25):
                self.__aaReg = num
            elif (round(float(val), 1) == 0):
                self.__aa = 0
            else:
                raise IndexError
        else:
            raise TypeError

    def setAPW(self, val):
        if (self.__is_num(val)):
            if (round(float(val), 1) <= 1.9 and round(float(val), 1) >= 0.1):
                self.__apw = float(val)
            else:
                raise IndexError
        else:
            raise TypeError

    def setARP(self, val):
        if (self.__is_num(val)):
            if (int(round(float(val), -1)) <= 500 and int(round(float(val), -1)) >= 150):
                self.__arp = int(round(float(val), -1))
            else:
                raise IndexError
        else:
            raise TypeError

    def setPVARP(self, val):
        if (self.__is_num(val)):
            if (int(round(float(val), -1)) <= 500 and int(round(float(val), -1)) >= 150):
                self.__pvarp = int(round(float(val), -1))
            else:
                raise IndexError
        else:
            raise TypeError

    def setHYST(self,val):
        if(self.__isHyst):
            if (self.__is_num(val)):
                num = 5 * round(float(val) / 5)
                if (round(float(val)) <= 90 and round(float(val)) >= 50):
                    self.__hyst = round(float(val))
                elif ((num <= 50 and num >= 30) or (num <= 175 and num >= 90)):
                    self.__hyst = num
                else:
                    raise IndexError
            else:
                raise TypeError
        else:
            raise IndexError #?

    def setRS(self,val):
        if(self.__isRS):
            if (self.__is_num(val)):
                num = 3 * round(float(val) / 3)
                if (round(float(val)) <= 3 and round(float(val)) >= 21):
                    self.__rs = round(float(val))
                else:
                    raise IndexError
            else:
                raise TypeError
        else:
            raise IndexError #?

    def setAT(self,val):
        if (self.__is_num(val)):
            num = round(float(val))
            if (num != 8 and num != 4 and num != 2):
                raise IndexError
            else:
                self.__at = num
        else:
            raise TypeError

    def setREACT(self,val):
        if (self.__is_num(val)):
            num = 10 * round(float(val) / 10)
            if (num <= 50 and num >= 10):
                self.__reactT = num*1000 #in ms
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
                self.__recovT = round(float(val))*60000 #in ms
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
