#we start asking for the weight of the user
weight = float(input ("Insert your Weight: "))

#We have to ask if their weight its on Kilograms or Pounds
Kilo_Pounds = input("(K)g or (L)bs: ")

#We have to use a conditional to identify what type of operation we will do
if (Kilo_Pounds == "K" or Kilo_Pounds == "k"):
    convert= weight * 2.20462
    ##Here I used (f) to print the value of Convert only with 2 decimals
    print("Your weight in Pounds: ", f"{convert:,.2f}")
elif (Kilo_Pounds == "L" or Kilo_Pounds == "l"):
    convert = weight * 0.453592
    print ( "Your weigth in Kg: ", f"{convert:,.2f}" )
else:
    print ("Incorrect value")
