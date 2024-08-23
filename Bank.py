# Bank System:
# Create an account
print("Welcome to Bank let's Create Account")
username = input("Enter what you want to be your username: ")
password = int(input("Enter what do you want to be your password: "))
# elections
print("Your username is " + username)
print("Choose only one:")
print("Type 1 to Withdraw")
print("Type 2 for Deposit")
print("Type 3 to exit")
# Withdraw, Deposit, Exit
def select(selection):
    # Withdraw
    if selection == 1:
        print("If you want to Withdraw Money we need your username and password")
        print("to make sure that it's your account")
        username_check = input("Enter your username: ")
        password_check = int(input("Enter your password: "))
        if username_check == username and password_check == password:
            print("Let's continue")
            withdraw = int(input("How much do you want to withdraw: "))
            print("Here is your Money: gives",withdraw,"$")
        else:
            print("Either username or password is incorrect")
            print("Please try again")
            username_check = input("Enter your username: ")
            password_check = int(input("Enter your password: "))
            if username_check == username and password_check == password:
                print("Let's continue")
                withdraw = int(input("How much do you want to withdraw: "))
                print("Here is your Money: gives",withdraw,"$")
            else:
                print("Too many wrong attemps, please try again later")
    # Deposit            
    elif selection == 2:
        print("If you want to Deposit Money we need your username and password")
        print("to make sure that it's your account")
        username_check = input("Enter your username: ")
        password_check = int(input("Enter your password: "))
        if username_check == username and password_check == password:
            print("Let's continue")
            Deposit = int(input("How much do you want to Deposit: "))
            print(Deposit,"$ has been added to your account")
            print("Balance =",Deposit,"$")
        else:
            print("Either username or password is incorrect")
            print("Please try again")
            username_check = input("Enter your username: ")
            password_check = int(input("Enter your password: "))
            if username_check == username and password_check == password:
                print("Let's continue")
                Deposit = int(input("How much do you want to Deposit: "))
                print(Deposit,"$ has been added to your account")
                print("Balance =",Deposit,"$")
            else:
                print("Too many wrong attemps, please try again later")
    # Exit
    elif selection == 3:
        print("Thanks for visiting our Bank")
    else:
        print("There are no choises like that")
select(int(input("which one do you want to do: ")))