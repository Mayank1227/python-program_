rno=int(input("Enter Roll No:"))
sname=input("Enter student Name:")
s1=int(input("Enter Marks of subject 1:"))
s2=int(input("Enter Marks of subject 2:"))
s3=int(input("Enter Marks of subject 3:"))
s4=int(input("Enter Marks of subject 4:"))

total=s1+s2+s3+s4
per=total/4

print("student Roll No :",rno)
print("Student Name :",sname)
print("total :",total)
print("percentage :",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("pass class")   
else:
    print("fail")

