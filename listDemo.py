# list is grop of mix typeof of deta
l=[1,2,3,1,12,2,"tops","true ",1,2 ] 

print(l)
l.append(100)  # list na last ma singal element add karva mate append
print(l)
# l.clear()  "list khali thai jse"
# print(l)
ll=l.copy() # list copy thayu l1 ma
print(11)
ll.append(200)
print(1)    #orijan 
print(11)   # copy ma add thse 
l2=l       
print(l2)
l2.append(300)
print(l)
print(l2)
print(l.count(1)) #  (1)one count karse list mathi true=(1)
l3=[101,202,303] # list ni pachal aakhu biju list jodvu voy tyare extent no use thay
l.extend(13)  
print(l)
print(l.index(1)) # 1 ni index (0) malse
l.insert(5,1000)  #  5 number index par 1000 add karse  element riples nthi kartu
print(l)
l.pop()   # list na last mathi eliment remov karse
print(l)
l.remove(100) #argumet ma je aapyu hse te remov karse
print(l)
l.pop(1)  #index number  parthi remov karse
print(l)
l.reverse()  # index reverse karse
print(l)

