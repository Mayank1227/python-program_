number =int(input("Enter any number between 100 and 500:"))
while number <100  or number > 500:
    print ("Incorrect number, please enter the correct number:")
    number = int(input("Enter any number between 100 and 500:"))
else:
    print("Given Number is correct",number)