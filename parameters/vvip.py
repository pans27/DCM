class Vvip:
    def __init__(self) :
        self.__lrl=60
        self.__url=120
        self.__va=3.5
        self.__vpw=0.4
        self.__vrp=320

    def getLRL(self):
        return self.__lrl
    
    def getURL(self):
        return self.__url
    
    def getVA(self):
        return self.__va
    
    def getVPW(self):
        return self.__vpw
         
    def getVRP(self):
        return self.__vrp
    def setLRL(self,val):
        if(self.__is_num(val)):
            if(int(val)<=175 and int(val)>=30):
                self.__lrl=int(val)
            else:
                raise IndexError
        else:
            raise TypeError

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
    def setVA(self,val):
        if(self.__is_num(val)):
            if(round(float(val),1)<=7.0 and round(float(val),1)>=0.5):
                self.__va=round(float(val),1)
            else:
                raise IndexError  
        else:
            raise TypeError
    def setVPW(self,val):
        if(self.__is_num(val)):
            if(round(float(val),1)<=1.9 and round(float(val),1)>=0.1):
                self.__vpw=round(float(val),1)
            else:
                raise IndexError      
        else:
            raise TypeError

    def setVRP(self,val):
        if(self.__is_num(val)):
            if(int(round(float(val),-1))<=500 and int(round(float(val),-1))>=150):
                self.__vrp=int(round(float(val),-1))
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
