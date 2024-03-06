# MethodOveriding

class A:

    def show(self):
        print("Show Form Class A")

class B(A):

    def show(self):
        print("Show Form Class B")

b1=B()
b1.show()