# Method overloding

class A:

    def show(self):
        print("Show Form Class A")

class B(A):

    def show(self):
        super().show()
        print("Show Form Class B")

class C(B):

    def show(self):
        super().show()
        print("Show Form Class C")

b1=C()
b1.show()
# 
print("*****************")
#  multipal ma method over raiding sol..
class A:

    def show(self):
        super().show()
        print("Show Form Class A")

class B:

    def show(self):
       
        print("Show Form Class B")

class C(A,B):

    def show(self):
        super().show()
        print("Show Form Class C")

b1=C()
b1.show()


# 
print("*****************")
# 
class A:

    def show(self):
        print("Show Form Class A")

class B(A):
    def show(self):
        super().show()
        print("Show Form Class B")

class C(A):

    def show(self):
        super().show()
        print("Show Form Class C")

class D(B,C):

    def show(self):
        super().show()
        print("Show Form Class D")

b1=D()
b1.show()