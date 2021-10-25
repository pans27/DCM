class Aaip:
    def __init__(self) :
        self.__lrl=60
        self.__url=120
        self.__aa=3.5
        self.__apw=0.4
        self.__arp=250

    def getLRL(self):
        return self.__lrl
    
    def getURL(self):
        return self.__url
    
    def getAA(self):
        return self.__aa
    
    def getAPW(self):
        return self.__apw

    def getARP(self):
        return self.__arp
        
    def setLRL(self,val):
        if(self.__is_num(val)):
            if(round(float(val))<=175 and round(float(val))>=30):
                self.__lrl=round(float(val))
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
    def setAA(self,val):
        if(self.__is_num(val)):
            if(round(float(val),1)<=7.0 and round(float(val),1)>=0.5):
                self.__aa=round(float(val),1)
            else:
                raise IndexError  
        else:
            raise TypeError
    def setAPW(self,val):
        if(self.__is_num(val)):
            if(round(float(val),1)<=1.9 and round(float(val),1)>=0.1):
                self.__apw=float(val)
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
    
    def __is_num(self,s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
