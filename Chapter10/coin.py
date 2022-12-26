import random
class Coin:
    def __init__(self):
        self.__sideup='Eagle'

    def toss(self):
        count=random.randint(0,1)
        if count==0:
            self.__sideup='Eagle'
        else:
            self.__sideup='Tails'

    def get_sideup(self):
        return self.__sideup


