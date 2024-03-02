import random

data=open("dta.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()
print("Data fail Written Successfully")

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
l=data.read().split(",")[:-1]
for i in l:
    if int (i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
data.close()        
even.close() 
odd.close() 

print("Data Fail Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even Fail Content")
data=open("Even.txt","r")
print(data.read())
data.close()

print("odd Fail Content")
data=open("odd.txt","r")
print(data.read())
data.close()
