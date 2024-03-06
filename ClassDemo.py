class Student:

    def grtData(self,fname,lname):  # self always Represent class 
      self.f=fname
      self.l=lname
    def putData(self):
       print("Frist Name :",self.f)
       print("Last Name :",self.l)

s1=Student()
s1.grtData("Mayank","Patel")
s1.putData()