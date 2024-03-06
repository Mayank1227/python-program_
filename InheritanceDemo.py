 #singal inheritance
class Base:

    def getA(self,a):
        self.a=a
        return self.a
    def putA(self):
        print("A:",self.a)

class Derived(Base):

    def getB(self, b):
       self.b=b
       return self.b
    def putB(self):
        print("B:",self.b)

d1=Derived()
d1.getA(20)
d1.getB(30)
d1.putA()
d1.putB() 

# self =>self ni mdadthi koi pan veribal use karvama aave & value asain karvama aave to ae class no veribal keyay 
