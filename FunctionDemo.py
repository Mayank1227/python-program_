#laibrary and user difain function
# Function With No Argument & No Return Value.
#python ma koi jatno deta tayp j nthi
# function is set of instason that parfoma a spacific task ther are 2 type function .


# Function with  No Argument & NO retun  Value.
def printLine():
    print("*"*50)
printLine()  #function ne call karvvu pde
print("Welome To User Difind Function In Python")
printLine()

# Function with Argument But No Return Value.

def add(a,b):
    print("Addittion:",a+b)

printLine()
x=int (input("Enter Value :"))
y=int (input("Enter Value :"))
add(x,y)
printLine()

# Function with Argument & Return Value.

def sub(a,b):
      return a-b

printLine()
x=int (input("Enter Value :"))
y=int (input("Enter Value :"))
# ans=(x,y)
print("Subtraction :",sub(x,y))
printLine()
