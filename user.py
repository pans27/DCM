import parameters.aoop
import parameters.voop
import parameters.aaip
import parameters.vvip

class User:
    def __init__(self,n,pw):
        self.__un=n
        self.__pw=pw
        self.aoo=parameters.aoop.Aoop()
        self.aai=parameters.aaip.Aaip()
        self.voo=parameters.voop.Voop()
        self.vvi=parameters.vvip.Vvip()

    def getUN(self):
        return self.__un

    def getPW(self):
        return self.__pw

    
