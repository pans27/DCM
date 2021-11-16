import parameters.aoop
import parameters.voop
import parameters.aaip
import parameters.vvip
import parametersA2.aoorp
import parametersA2.voorp
import parametersA2.aairp
import parametersA2.vvirp
import parametersA2.doop
import parametersA2.doorp
#Oct 31, 2021
#Author: Group 5
#3k04 DCM assignment 1 user object for storing data

class User:
    def __init__(self,n,pw):
        self.__un=n
        self.__pw=pw
        self.aoo=parameters.aoop.Aoop()
        self.aai=parameters.aaip.Aaip()
        self.voo=parameters.voop.Voop()
        self.vvi=parameters.vvip.Vvip()
        self.aoor=parametersA2.aoorp.Aoorp()
        self.aair=parametersA2.aairp.Aairp()
        self.voor=parametersA2.voorp.Voorp()
        self.vvir=parametersA2.vvirp.Vvirp()
        self.doo=parametersA2.doop.Doop()
        self.door=parametersA2.doorp.doorp()

    def getUN(self):
        return self.__un

    def getPW(self):
        return self.__pw

    
