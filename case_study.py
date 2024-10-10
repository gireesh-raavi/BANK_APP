class Bank:
    def __init__(self):
        self.accounts={}
        self.transactions=[]
    def create_account(self):
        name=input("Enter Account Holder Name: ")
        account_number=int(input("Enter Account Number: "))
        initial_balance=int(input("Enter Initial Amount Deposited: "))
        if account_number not in self.accounts:
            self.accounts[account_number]={'name':name,'amount':initial_balance}
        else:
            print("Account Already Exists!")
    def view_accountdetails(self):
        k=int(input("Enter Account Number: "))
        if k in self.accounts:
            a=self.accounts[k]
            print("Account Holder Name: ",a["name"])
            print("Account Balance: ",a["amount"])
        else:
            print("No Account Details Found With The Account Number!")
    def withdraw(self):
        k=int(input("Enter Account Number: "))
        if k in self.accounts:
            a=self.accounts[k]
            amount=int(input("Enter Amount: "))
            a["amount"]=a["amount"]-amount
            print("Available Balance: ",a["amount"])
            self.transactions.append(f'Amount {amount} Rupees Withdrawn From The Account: {k}')
    def deposit(self):
        k=int(input("Enter Account Number: "))
        if k in self.accounts:
            a=self.accounts[k]
            amount=int(input("Enter Amount: "))
            a["amount"]=a["amount"]+amount
            print("Available Balance: ",a["amount"])
            self.transactions.append(f'Amount {amount} Rupees Deposited In The Account: {k}')
    def fund_transfer(self):
        from_acc=int(input("Enter Your Account Number: "))
        if from_acc in self.accounts:
            to_acc=int(input("Enter Receiver Account Number: "))
            if to_acc in self.accounts:
                amount=int(input("Enter Amount To Be Transferred: "))
                a=self.accounts[from_acc]
                b=self.accounts[to_acc]
                if a["amount"]>=amount:
                    a["amount"]=a["amount"]-amount
                    b["amount"]=b["amount"]+amount
                    print("amount transferred successfully",end=" ")
                    self.transactions.append(f'Amount Transferred {amount} From Account no: {from_acc} to {to_acc}')
                    print("remaining balance in your account: ",a["amount"])
                else:
                    print("Insufficient Funds")
            else:
                print("Receiver Account Not Found")
        else:
            print("Your Account Details Are Not Found")

                    
    def print_transactions(self):
        if self.transactions:
            for i in self.transactions:
                print(i)
        else:
            print("No Transactions Found..!")

obj=Bank()
while True:
    print("\nBANK APP")
    print("1:create account\n",
    "2:View Account Details by AccNo\n",
    "3.Withdraw\n",
    "4:Deposit\n",
    "5:Fund Transfer\n",
    "6:Print Transactions\n",
    "7:Exit")
    k=int(input("choose a option b/w 1 - 7: "))
    if k==1:
        obj.create_account()
    elif k==2:
        obj.view_accountdetails()
    elif k==3:
        obj.withdraw()
    elif k==4:
        obj.deposit()
    elif k==5:
        obj.fund_transfer()
    elif k==6:
        obj.print_transactions()
    elif k==7:
        print("exit")
        break 
    else:
        print("Invalid choice. Please choose a number b/w 1 to 7")
