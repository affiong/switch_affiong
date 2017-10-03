no_of_acc = [0]
class Banking():
    balance = 0.0
    no_of_acc = [0]
    
    def __init__ (self,username,phone,email):
        self.username = username
        self.useraccn = phone
        self.email = email
        self.accn = ""


    def creatAccount(self,increment):
        accountnumb = 1234567890
        self.accn = accountnumb + increment [0]
        no_of_acc [0] =no_of_acc[0]+1
        return self.accn
        
    def checkBalance(self,accn):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if self.balance<amount:
            print ("insufficient balance")
        else:
            self.balance -= amount
            print("you have withdranw", amount, "and your balance is", self.balance)
        return self.balance
    
cust_obj = Banking ("frank", "07038960562", "frank@gmal.com")
accn=cust_obj.creatAccount(no_of_acc)
print(cust_obj.checkBalance(accn))
print(cust_obj.accn)
cust_obj.withdraw(25000)
cust_obj.deposit(50000)
cust_obj.withdraw(15000)


cust_obj1 = Banking ("jean","08038960662","jean@yahoo.com")
accn=cust_obj1.creatAccount(no_of_acc)
print(cust_obj1.checkBalance(accn))
print(cust_obj1.accn)
cust_obj1.withdraw(25000)
cust_obj1.deposit(50000)
cust_obj1.withdraw(15000)

