
def show_balance(balance):
    print("***************************")
    print(f"Your Balance is Rs :{balance:.2f}")
    print("***************************")

def deposit():
    print("***************************")
    amount = int(input("Enter an amount to be deposition: "))
    print("***************************")

    if amount <=0 :
        print("***************************")
        print("That's not a valid amount")
        print("***************************")
        return 0
    else:
        return amount

def withdraw(balance):
     print("***************************")
     amount = int(input("Enter an amount to be withdraw: "))
     print("***************************")


     if amount >balance:
         print("***************************")
         print("Insufficient Balance")
         print("***************************")
         return 0

     elif amount < 0:
         print("***************************")
         print("Amount must be greater than '0'")
         print("***************************")
     else:
         return amount




def main():

    balance = 0
    is_running=True

    while is_running:
        print("*****************************")
        print("     Banking Program     ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*****************************")

        choice = input("Enter your choice (1-4):")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance +=deposit()
        elif choice =="3":
             balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************")
            print("That is not a valid choice!")
            print("***************************")

    print("***************************")
    print("Thank You ! Have a Nice Day!")
    print("***************************")


if __name__ =="__main__":
    main()