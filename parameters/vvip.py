class Vvip:
    def __init__(self) :
        self.lrl=60
        self.url=120
        self.va=3.5
        self.vpw=0.4
        self.vrp=320

    def getLRL(self):
        return self.lrl
    
    def getURL(self):
        return self.Url
    
    def getVA(self):
        return self.va
    
    def getVPW(self):
        return self.vpw
         
    def getVRP(self):
        return self.vrp
    def setLRL(self,val):
        if(val.isnumeric() and int(val)<=175 and int(val)>=30):
            self.lrl=int(val)
        else:
            raise TypeError

    def setURL(self,val):
        if(val.isnumeric() and int(val)<=175 and int(val)>=50):
            self.url=int(val)
        else:
            raise TypeError
    def setVA(self,val):
        if(val.isnumeric() and float(val)<=7.0 and float(val)>=0.5):
            self.va=float(val)
        else:
            raise TypeError
    def setVPW(self,val):
        if(val.isnumeric() and float(val)<=1.9 and float(val)>=0.1):
            self.vpw=float(val)
        else:
            raise TypeError
    def setVRP(self,val):
        if(val.isnumeric() and int(val)<=500 and float(val)>=150):
            self.vrp=int(val)
        else:
            raise TypeError