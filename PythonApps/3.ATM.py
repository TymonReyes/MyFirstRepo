#I will create a simple ATM menu, with an interactive menu
i=0
money = 1000
    #First I will show a little welcome to the client, I used this print out of the loop (while) because
    #I only want to show this 1 time when the client inicialize the code.
print("    WELCOME TO TYMON'S ATM" )
    #Here I create a loop using while, and I show with prints all the menu.
    #I used the number 4 because I want to run all the code until the client wants to go. 
while i != 4:
    print("Select an option in the menu" )
    print("1- View Money" )
    print("2- Deposit Money" )
    print("3- Withdraw Money" )
    print("4- Exit")
        #Here I create a variable called option to save the selection of the client, with this, the code will
        #know what the client wants. I declare option like a integer because I need a number not a string
    option = int(input("Select an option: "))
        #Here the code analize what the client wants with the number who was inserted.
    if option == 1:
        print("---------------------------------")
        print("Your balance is ",money)
        print("---------------------------------")
        #With these elif the code sum or rest the money of the account.
    elif option == 2:
        Deposit = int(input("Enter the amount you want to deposit: "))
        money = money + Deposit
        print("---------------------------------")
        print("Your new balance is: ", money)
        print("---------------------------------")
    elif option == 3:
        Withdraw = int(input("Enter the amount you want to withdraw: "))
            #Here the code will verify if the account has enough money, if it doesn't, it will notify the client
            #and it will restart the loop
        if money - Withdraw >= 0:
            money = money - Withdraw
            print("---------------------------------")
            print("Your new balance is: ", money)
            print("---------------------------------")
        else :
            print("---------------------------------")
            print("INSUFICIENT BALANCE")
            print("---------------------------------")
        #Here if the client select number 4, the code will change the value of i to 4, and the loop will end.
    elif option == 4:
        print("THANKS FOR CHOOSE TYMON'S ATM, BACK SOON")
        i=4
        #If the client doesnt select a correct option, it will notify the client and it will restart the loop
        #letting the client to insert a new value
    else:
        print("You did not select a correct option")
