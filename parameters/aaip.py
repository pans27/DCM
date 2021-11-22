#Oct 31, 2021
#Author: Group 5
#3k04 DCM assignment 1 aai parameters



class Aaip:
    def __init__(self) :
        self.__lrl=60
        self.__url=120
        self.__aa = 5.0
        self.__apw=1
        self.__as = 0.8
        self.__arp=250
        self.__pvarp = 250
        self.__hyst = 0
        self.__rs = 0

    def getLRL(self):
        return self.__lrl
    
    def getURL(self):
        return self.__url
    
    def getAA(self):
        if(self.__aa):
            return self.__aa 
        else:
            return 'OFF'

    def getAPW(self):
        return self.__apw
    
    def getAS(self):
        return self.__as

    def getARP(self):
        return self.__arp
    
    def getPVARP(self):
        return self.__pvarp

    def getHYST(self):
        if(self.__hyst):
            return self.__hyst 
        else:
            return 'OFF'
    
    def getRS(self):
        if(self.__rs):
            return self.__rs
        else:
            return "OFF"
        
    def setLRL(self,val):
        if(self.__is_num(val)):
            num=5* round(float(val)/5)
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
            if(num<=175 and num>=50 and num>=self.__lrl):
                self.__url=num
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
            
    def setAS(self, val):
        if (self.__is_num(val)):
            if(round(float(val), 1) <= 5.0 and round(float(val), 1) >= 0):
                self.__as = round(float(val), 1)
            else:
                raise IndexError
        else:
            raise TypeError
            
    def setARP(self,val):
        if(self.__is_num(val)):
            if(int(round(float(val),-1))<=500 and int(round(float(val),-1))>=150):
                self.__arp=int(round(float(val),-1))
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
        if(val.casefold()=='off'.casefold()):
            self.__hyst = 0
            return
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
        self.__rs = round(float(val))
 
            
    def __is_num(self,s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
