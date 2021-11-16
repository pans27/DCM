# Oct 31, 2021
# Author: Group 5
# 3k04 DCM assignment 1 aai parameters

class Vvip:
    def __init__(self) :
        self.__lrl=60
        self.__url=120
        self.__vaReg = 3.5
        self.__vaUnreg = 3.75
        self.__vpw=0.4
        self.__vs = 2.5
        self.__vrp=320
        self.__hyst = 0
        self.__rs = 0

    def getLRL(self):
        return self.__lrl

    def getURL(self):
        return self.__url

    def getVAReg(self):
        return self.__vaReg

    def getVAUnreg(self):
        return self.__vaUnreg

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
    
    def setLRL(self,val):
        if(self.__is_num(val)):
            num=5* round(float(val)/5)
            if(round(float(val))<=90 and round(float(val))>=50):
                self.__lrl=round(float(val))
            elif((num<=50 and num>=30) or (num<=175 and num>=90)):
                self.__lrl=num
        if(self.__is_num(val)):
            if(round(float(val))<=90 and round(float(val))>=50):
                self.__lrl=round(float(val))
            elif((num<=50 and num>=30) or (num<=175 and num>=90)):
                self.__lrl=num
            else:
                raise IndexError
        else:
            raise TypeError
            
    def setURL(self,val):
        if(self.__is_num(val)):
            num=5* round(float(val)/5)
            if(num<=175 and num>=50):
                self.__url=num
            else:
                raise IndexError    
        else:
            raise TypeError
            
    def setVAReg(self, val):
        if (self.__is_num(val)):
            num = 0.5 * round(float(val) / 0.5)
            if (round(float(val), 1) <= 3.2 and round(float(val), 1) >= 0.5):
                self.__vaReg = round(float(val), 1)
            elif (num <= 7.0 and num >= 3.5):
                self.__vaReg = num
            elif (round(float(val), 1) == 0):
                self.__vaReg = 0
            else:
                raise IndexError
        else:
            raise TypeError

    def setVAUnreg(self, val):
        if (self.__is_num(val)):
            num = 1.25 * round(float(val) / 1.25)
            if (round(float(val), 2) <= 5.00 and round(float(val), 2) >= 1.25):
                self.__vaUnreg = num
            elif (round(float(val), 1) == 0):
                self.__vaUnreg = 0
            else:
                raise IndexError
        else:
            raise TypeError
            
    def setVPW(self, val):
        if (self.__is_num(val)):
            if (round(float(val), 1) <= 1.9 and round(float(val), 1) >= 0.1):
                self.__vpw = float(val)
            else:
                raise IndexError
        else:
            raise TypeError
    
    def setVS(self, val):
        if (self.__is_num(val)):
            if (round(float(val), 2) == 0.25 or round(float(val), 2) == 0.5 or round(float(val), 2) == 0.75):
                self.__vs = round(float(val), 2)
            elif(round(float(val), 1) <= 10.0 and round(float(val), 1) >= 1.0):
                num = 0.5 * round(float(val) / 0.5)
                self.__vs = num
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
            
    def __is_num(self,s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            raise TypeError
            return True
