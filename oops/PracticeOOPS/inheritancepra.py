class A: # a is a super class
    def __init__(self):
        print("init")

    def feature(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("binit")
    def feature4(self):
        print("feature 3 is working")
    def feature2(self):
        print("feature 4 is working")
class C(B):
    def feature5(self):
        print("feature 5 is working")
    


a1 = B()
