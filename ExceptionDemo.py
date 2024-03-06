print("Start Code")

try:
    a=int("Enter Value :")
    b=int("Enter Value :")

    c=a/b
    print("Division :",c)  # exception hendel karva mate  programna te part ne try block ma mukavo.
    
    l=[1,2,3,4,5]
    index=int(input("Enter Index Number:"))
    print("Data:",1[index])
except Exception as e:
    print("Exception Caught:",e)

print("End Code")    


# except ZeroDivisionError as e:
#     print("Exception Caught:",e)
# except ValueError as e:
#     print("Exception Caught:",e)
# except IndexError as e:
#     print("Exception Caught:",e)



    

