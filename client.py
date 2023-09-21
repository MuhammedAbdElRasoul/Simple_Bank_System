from random import randint

class Client :
    # Create a list contains all bank accounts         
    # Each client has name : xxxx , age : xx , holdings : xxxxx , account_num : xxxxxx
    accounts = {}

    def __init__(self , name , age , deposit) :
        self.accounts["name"] = name
        self.accounts["age"] = age
        self.accounts["holdings"] = deposit
        self.accounts["account_num"] = randint(10000 , 100000)

    def withdraw (self, amount) :
        if self.accounts["holdings"] >= amount :
            self.accounts["holdings"] -= amount
            print()
            print("The Amount Has Been Withdrawn Successfully from Your Bank Account.")
            print()
            self.balance()

        else :
            print()
            print("No Enough Funds!.")
            print()


    def deposit (self, amount) :
        self.accounts["holdings"] += amount
        print()
        print("The Amount Has Been Added Successfully To Your Bank Account.")
        print()
        self.balance()

    def balance(self) :
        print("Now, Your Current Balance is {} ".format(self.accounts["holdings"]))      





