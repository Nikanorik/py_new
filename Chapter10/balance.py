class Balance:
    def __init__(self, bal):
        self.__balance=bal
    def deposite(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
        else:
            print('You have small money!!!')
    def get_balance(self):
        return self.__balance
