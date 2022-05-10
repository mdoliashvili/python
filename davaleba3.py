class Person:
    def __init__(self,name,deposit='1000',loan='0'):
        self.name = name
        self.deposit = deposit
        self.loan = loan


    def __str__(self):
        return f'{self.name},{self.}'

class House:
    def __init__(self,ID,price,owner,status):
        self.ID=ID
        self.price = price
        self.owner= owner
        self.status = status
