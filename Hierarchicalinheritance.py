# hierarchical inheritance

class Base:

    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)

class Derived(Base):

    def getB(self, b):
       self.b=b
    def putB(self):
        print("B:",self.b)

class Subderived(Base):

    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)

class Subderived1(Base):

    def getD(self,d):
        self.d=d
    def putD(self):
        print("D:",self.d)

d1=Derived()
sd=Subderived()
sd1=Subderived1()

d1.getA(20)
d1.getB(30)
sd.getC(40)
sd1.getD(50)

d1.putA()
d1.putB()
sd.putC()
sd1.putD()

 