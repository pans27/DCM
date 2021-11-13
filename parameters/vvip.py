# Oct 31, 2021
# Author: Group 5
# 3k04 DCM assignment 1 aai parameters

class Vvip:
    def __init__(self) :
        self.lrl=60
        self.url=120
        self.va=3.5
        self.vpw=0.4
        self.vrp=320
        self.__lrl=60
        self.__url=120
        self.__va=3.5
        self.__vpw=0.4
        self.__vrp=320

    def getLRL(self):
        return self.lrl
        return self.__lrl

    def getURL(self):
        return self.url
        return self.__url

    def getVA(self):
        return self.va
        return self.__va

    def getVPW(self):
        return self.vpw
        return self.__vpw

    def getVRP(self):
        return self.vrp
        return self.__vrp
    def setLRL(self,val):
        if(val.isnumeric() and int(val)<=175 and int(val)>=30):
            self.lrl=int(val)
        if(self.__is_num(val)):
            if(int(val)<=175 and int(val)>=30):
                self.__lrl=int(val)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self,val):
        if(val.isnumeric() and int(val)<=175 and int(val)>=50):
            self.url=int(val)
        if(self.__is_num(val)):
            if(int(val)<=175 and int(val)>=50):
                self.__url=int(val)
            else:
                raise IndexError
        else:
            raise TypeError
    def setVA(self,val):
        if(val.isnumeric() and float(val)<=7.0 and float(val)>=0.5):
            self.va=float(val)
        if(self.__is_num(val)):
            if(float(val)<=7.0 and float(val)>=0.5):
                self.__va=float(val)
            else:
                raise IndexError
        else:
            raise TypeError
    def setVPW(self,val):
        if(val.isnumeric() and float(val)<=1.9 and float(val)>=0.1):
            self.vpw=float(val)
        if(self.__is_num(val)):
            if(float(val)<=1.9 and float(val)>=0.1):
                self.__vpw=float(val)
            else:
                raise IndexError
        else:
            raise TypeError

    def setVRP(self,val):
        if(val.isnumeric() and int(val)<=500 and float(val)>=150):
            self.vrp=int(val)
        if(self.__is_num(val)):
            if(int(val)<=500 and float(val)>=150):
                self.__vrp=int(val)
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