'''
1.simple if

 if condition:
    statement

2. If/Else
 
  if condition:
    statement
  else:
       statement

3. Nested If

 if condition:
   if condition:
      statement
      else:
          statement
   else:
       statement  

4.Ladder If/else 

  if condition:
      statement
  elif condition:
     statement
  elif condition:
     statement
  else:
     statement
'''
#  possitive & Negative number
a= int(input("Enter A:"))
if a>0:
    print("A is possitive Number")
else:
    print("A is Negative Number")

#  even or odd number
a= int(input("Enter A:"))
if a%2==00:
    print("A is Even Number")
else:
    print("A is odd Number")

# a>b Greater number
a= int(input("Enter A:"))
b= int(input("Enter B:"))
if a>b:
    print("A is Greater Number")
else:
    print("B is Greater Number")

# a>b>c Greater number
a= int(input("Enter A:"))
b= int(input("Enter B:"))
c= int(input("Enter C:"))
if a>b:
    if a>c:
      print("A is Greater Number")
    else:
       print("c is Greater Number")
elif b>c:
      print("B is Greater Number")
else:
    print("c is Greater Number")