import os

class Settings:
    @staticmethod
    def getDBUsername():
        return os.environ["EldenRingCalcUsername"]


    @staticmethod
    def getDBPassword():
        return os.environ["EldenRingCalcPassword"]