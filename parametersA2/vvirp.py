# November 28, 2021
# Author: Group 5
# 3k04 DCM assignment 2 vvir parameters

class Vvirp:
    def __init__(self):
        self.__lrl = 60
        self.__url = 120
        self.__msr = 120
        self.__va=5.0
        self.__vpw = 1
        self.__vs = 2.5
        self.__vrp = 320
        self.__hyst = 0
        self.__rs = 0
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

    def getVA(self):
        return self.__va

    def getVPW(self):
        return self.__vpw

    def getVS(self):
        return self.__vs

    def getVRP(self):
        return self.__vrp

    def getHYST(self):
        return self.__hyst
    
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

    def setVA(self, val):
        if (self.__is_num(val)):
            num =round(float(val),1)
            if (num <= 5.0 and num >= 3.5):
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
            
    def setVS(self, val):
        if (self.__is_num(val)):
            if(round(float(val), 1) <= 5.0 and round(float(val), 1) >= 0):
                self.__vs = round(float(val), 1)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVRP(self, val):
        if (self.__is_num(val)):
            if (int(round(float(val), -1)) <= 500 and int(round(float(val), -1)) >= 150):
                self.__vrp = int(round(float(val), -1))
            else:
                raise IndexError
        else:
            raise TypeError
            
    def setHYST(self,val):
        if (self.__is_num(val)):
            num = 5 * round(float(val) / 5)
            if (round(float(val)) <= 90 and round(float(val)) >= 50):
                self.__hyst = round(float(val))
            elif ((num <= 50 and num >= 30) or (num <= 175 and num >= 90)):
                self.__hyst = num
            elif (round(float(val)) == 0):
                self.__hyst = 0
            else:
                raise IndexError
        else:
            raise TypeError

    def setRS(self,val):
        if (self.__is_num(val)):
            num = 3 * round(float(val) / 3)
            if (round(float(val)) <= 3 and round(float(val)) >= 21):
                self.__rs = round(float(val))
            elif (round(float(val)) == 0):
                self.__rs = 0
            else:
                raise IndexError
        else:
            raise TypeError

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
