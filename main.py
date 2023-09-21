from client import Client
from bank import Bank

bank = Bank()

running = True
while running :
    print()
    print(bank.name)

    print("""
        1- Open A New_Bank_Account 
        
        2- Open An Existing_Bank_Account 
        
        3- Exit
    """)

    choice = int(input("Please, Choose 1, 2 or 3 : "))

    if choice == 1 :
        print()
        print("In order to open a new account , You should fill some information.")
        print()
        client = Client(input("Enter Your Triple Name : ") , int(input("Enter Your Age : ")) , float(input("Enter The Intial Deposit Amount : ")))
        bank.update_db(client)
        print()
        print("Please, Keep Your ACCount Number Secret" , end="")
        print(" , Your Account Number is : ",Client.accounts["account_num"])
        print()
        print("Congratulations! , Your Bank Account Has Been Created Successfully.")
        print()

    elif choice == 2 :
        print()
        print("In Order To Open Your Bank Account, You Must Register With Bank Info.")
        print()
        name = input("Enter Your Name : ")
        gender = input("Are You Male Or Female ?. : ").capitalize()
        account_num = int(input("Enter You Account Number : "))
        current_client = bank.authentication(name,account_num)
        if current_client :
            acc_open = True
            while acc_open :
                x = "Mr" if gender == "Male" else "Mss"
                print()
                print(f"Welcome {x} {name}, Your Bank Account Has Been Opened Successfully!.")
                print()
                print(""" Choose One From These Procedures :
                    
                    1- Withdraw 
                    2- Deposit
                    3- Balance 
                    4 - Exit 
                    
                    """)
                service_choice = int (input("Enter 1, 2, 3 or 4 : "))
                if service_choice == 1 :
                    current_client.withdraw(int(input("Enter The Amount You Need To withdraw From Your Bank Accout: ")))

                elif service_choice == 2 :
                    current_client.deposit(int(input("Enter The Amount You Need To Add To Your Bank Account: ")))

                elif service_choice == 3 :
                    current_client.balance()    

                else :
                    print("Thanks alot for Visiting us.")
                    current_client = ""
                    acc_open = False
                    
                    
        else : 
            print()
            print("Authication Failed!")
            print("Reason: account not found.")
            print()
            print("Try Again With The correct Name And Account Number.")
            continue
                        
    else :
        print() 
        print("Goodbye!.")
        running = False






