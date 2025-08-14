class Grandparent:
    def method(self):
        print("Grandparent method")

class Parent1(Grandparent):
    def method(self):
        print("Parent1 method")

class Parent2(Grandparent):
    def method(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    pass

child = Child()
child.method()  # Output: "Parent1 method"
print(Child.mro())  # Shows method resolution order