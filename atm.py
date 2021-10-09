class ATM:
    def __init__ (self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balance(self):
        print("your balance is 50,000")

    def withdraw(self, amount):
        newAmount = 50000 - amount
        print("you have withdrawn" + str(amount)+"your remaining balance is " + str(newAmount))

def main():
    cardNumber = input("please insert card number")
    pin = input(" please insert pin")

    withdrawer = ATM(cardNumber,pin)
    print("choose your activity")
    print("1.balanceEnquiry  2.withdrawl")
    activity = int(input("enter activity number"))
    if(activity == 1):
        withdrawer.balance()

    elif(activity == 2):
        amount = int(input("enter the amount"))
        withdrawer.withdraw(amount)

    else:
        print("Enter a valid number")

main()
