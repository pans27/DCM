class Aoop:
    def __init__(self) :
        self.lrl=60
        self.url=120
        self.aa=3.5
        self.apw=0.4
        
    def getLRL(self):
        return self.lrl
    
    def getURL(self):
        return self.url
    
    def getAA(self):
        return self.aa
    
    def getAPW(self):
        return self.apw
    def setLRL(self,val):
        if(is_num(val)):
            if(int(val)<=175 and int(val)>=30):
                self.lrl=int(val)
            else:
                raise IndexError
        else:
            raise TypeError

    def setURL(self,val):
        if(is_num(val) and int(val)<=175 and int(val)>=50):
            self.url=int(val)
        else:
            raise TypeError
    def setAA(self,val):
        if(is_num(val) and float(val)<=7.0 and float(val)>=0.5):
            self.aa=float(val)
        else:
            raise TypeError
    def setAPW(self,val):
        if(is_num(val) and float(val)<=1.9 and float(val)>=0.1):
            self.apw=float(val)
        else:
            raise TypeError

    
def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True
