class Bank:
    def openAccount(self,cname,acno,balance):
        self.c=cname
        self.ac=acno
        self.b=balance
        print("Hello",self.c,"Your Account Number",self.ac,"Is oppend with",self.b," Rs")
    def diposite(self,amount):
        self.b=self.b+amount
    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            self.needs=amount-self.b
            print("Soory You Need Another",self.needs,"Rs.To Withdraw")
    def checkBalance(self):
        print("Current Balance:",self.b)

b1=Bank()
cname=input("Enter Customer Name:")
acno=int(input("Enter ACcount Number :"))
balance=int(input("Enter Initial Balance :"))
b1.openAccount(cname,acno,balance)

while True:

    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice=int(input("Enter Your Choice :"))

    if choice==1:
        amount=int(input("Enter Deposit Amount:"))
        b1.diposite(amount)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount:"))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkBalance()
    else:
        print("Thank You For Using Our Services Goo By :")
        break


# dbabbcabccdcddcabbdd