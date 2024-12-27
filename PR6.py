Information = []
class InsufficientFundsError(Exception):
    pass
def demo(Add_Deposit):
    if Add_Deposit>0 :
        
        for i in Information :
            New_Deposits = i["Deposits"]+Add_Deposit
            i["Deposits"] = New_Deposits
            print(f"Deposited Successfully! Your Current Balance is : {New_Deposits}")
    else :
        raise ValueError("The Amount must be Positive!!")
        
def demo1():
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
        
def demo2(withdrawal):
    if withdrawal>0:
        for i in Information:
            if withdrawal>i["Deposits"]:
                raise InsufficientFundsError("Your Account does not have enough balance sorry!")
            else :
                new_Deposits = i["Deposits"]-withdrawal
                i["Deposits"] = new_Deposits
                print(f"withdrawed Successfully! Your Current Balance is : {new_Deposits}")
    else :
        raise ValueError("The Amount you haved entered is negative!")
print("Welcome to the Robust Banking System!")
while True :
    print("Please select an option:")
    print("1.Create Accounts")
    print("2.Deposits Funds")
    print("3.Withdraw Funds")
    print("4.Check Balance")
    print("5.Exit")
    try:
        choice = int(input("Enter the choice you want = ")) 
        if choice==1 :
            try :
                demo1()
            except :
                print("General Exception Block!!")
        elif choice==2 :
            try :
                demo(int(input("Enter Deposit Amount = ")))
            except ValueError as e : 
                print(f"Not Possible Because of {e}")
            except :
                print("General Exception Block!!")
        elif choice==3 :
            try :
                demo2(int(input("Enter withdrawal Amount = ")))
            except InsufficientFundsError as e : 
                print(f"Not Possible Because of {e}")
            except :
                print("General Exception Block!!")
        elif choice==4 :
            for i in Information :
                print("Your Current Balance is :",i["Deposits"])
        elif choice==5 :
            print("Thank you for using the Robust Banking System! Goodbye!")
            break
        else:
            raise TypeError()   
    except:
        print("Error: Invalid choice. Please select a valid option.")