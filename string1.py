s=input("Enter String:")
 
alpha=0
digit=0
space=0
upper=0
lower=0

for i in s:
  if i.isalpha():
     alpha+=1
  elif i.isnumeric():
     digit+=1
  elif i.isspace():
     space+=1
  if i. isupper():
     upper+=1
  elif i.islower():
     lower+=1
    
print("Total Alphabets:",alpha)
print("Total numeric:",digit)
print("Total space:",space)
print("Total Upper case:",upper)
print("Total Loewr case:",lower)