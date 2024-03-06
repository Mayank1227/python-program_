#Multipal inheritance

class Base:

    def getA(self,a):
        self.a=a
        return self.a
    def printA(self):
        print("A:",self.a)

class Derived:

    def getB(self, b):
       self.b=b
       return self.b
    def printB(self):
        print("B:",self.b)

class Subderived(Base,Derived):

    def getC(self,c):
        self.c=c
        return self.c
    def printC(self):
        print("C:",self.c)

d1=Subderived()
d1.getA(20)
d1.getB(30)
d1.getC(40)
d1.printA()
d1.printB()
d1.printC()

 