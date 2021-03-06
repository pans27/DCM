#Oct 31, 2021
#Author: Group 5
#3k04 DCM assignment 1 aoo parameters

class Aoop:
    def __init__(self) :
        self.__lrl=60
        self.__url=120
        self.__aa=5.0
        self.__apw=1
        
    def getLRL(self):
        return self.__lrl
    
    def getURL(self):
        return self.__url
    
    def getAA(self):
        if(self.__aa):
            return self.__aa
        else:
            return "OFF"
   
    def getAPW(self):
        return self.__apw

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
        elif (self.__is_num(val)):
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

    def __is_num(self,s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
