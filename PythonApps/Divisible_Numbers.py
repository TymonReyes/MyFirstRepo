#In this code, I am going to ask the user for a number; 
#if the number is divisible by 3, it will show "Divisible by 3"
#if the number is divisible by 5, it will show "Divisible by 5"
#If none of the above is met, "Not divisible between 3 and 5" will be displayed

##I'll declare a variable, it will contain the number of the user.
print("---- Discover if your number is divisible by 3 or 5 ----")
    #I have to use float because I have to use it like a decimal number
Num = int(input("Insert the number: "))
    #I have to declare this variable to know the result of the division with 3 and 5

    #I used % to obtein the remain of the division.
if Num % 3 == 0 and Num % 5 == 0:
    print("Divisible by both")
elif Num % 3 == 0:
    print("Divisible by 3")
elif Num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible between 3 and 5")
