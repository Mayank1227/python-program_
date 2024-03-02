import random
# # l=[44,55,75,43,5,45,55,445]
# # print(random.choice(l))

# print(random.randint(1000,9999))
l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(10):
     num=random.choice(l)
     lucky.append(num)
     l.remove(num)  #karo to duplicet aave

print(l)
print(lucky)