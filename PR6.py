def Demo(Add_Deposit):
    if Add_Deposit>0 :
        for i in Information :
            New_Deposits = i["Deposits"]+Add_Deposit
            i["Deposits"] = New_Deposits
            print(f"Deposited Successfully! Your Current Balance is : {New_Deposits}")
    else :
        raise ValueError("The Amount must be Positive!!")
        
def Demo1():
    Web = {}
    Account_Holder = input("Enter Your Name = ")
    Balance = int(input("Enter initial Deposit Amount = "))
    if Balance>0 :
        Web["Name"] = Account_Holder
        Web["Deposits"] = Balance
        Information.append(Web)
        print("Amount Created Successfully!")
    else :
        print("The Amount you haved Enter is negative!")
        
Information = []
class InsufficientFundsError(Exception):
    pass
print("Welcome to the Robust Banking System!")
while True :
    print("Please select an option:")
    print("1.Create Accounts")
    print("2.Deposits Funds")
    print("3.Withdraw Funds")
    print("4.Check Balance")
    print("5.Exit")
    try :
        choice = int(input("Enter the choice you want = "))
        if choice==1 :
            try :
                Demo1()
            except :
                print("General Exception Block!!")
        elif choice==2 :
            try :
                Demo(int(input("Enter Deposit Amount = ")))
            except ValueError as e :
                print(f"Not Possible Because of {e}")
            except :
                print("General Exception Block!!")
        elif choice==3 :
            pass
        elif choice==4 :
            for i in Information :
                print("Your Current Balance is :",i["Deposits"])
        elif choice==5 :
            print("Thank you for using the Robust Banking System! Goodbye!")
            break
        else :
            if choice>5 :
                print("Error: Invalid choice. Please select a valid option.")   
    except :
        print("Error: Invalid choice. Please select a valid option.")
