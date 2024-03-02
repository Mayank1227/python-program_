l=[1,2,10,"python",False,"java",101,202,303,1,2,3,1.1,2.2,10,"Tops",True]
l1=[]

for i in l:
    print(i)
print(10.10 in l)

#  dupliget element

for i in l:
    c=l.count(i)
    if c>1:
        l1.append(i)
print(l1)

# dupliget element remov
for i in l:
    c=l.count(i)
    if c>1:
        if i not in l1:
             l1.append(i)
print(l1)