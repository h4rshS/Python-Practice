# Class
class Computer:
    
    # __init__, Constructor
    def __init__(self, cpu, ram):
        print('Currently in init')
        
        # Self
        self.cpu = cpu
        self.ram = ram
    
    # Methods
    def config(self):
        print('Config is :', self.cpu, self.ram)
        
    def update(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        
    # Comparing Objects
    def compare(self, comp):
        if self == comp:
            print('Both are same objects')
        else:
            print('Both are different objects')
        
# Objects
comp1 = Computer('i7','8gb')
comp2 = Computer('Ryzen 5','16gb')

print()

print(type(comp1))
print(id(comp1))

print()

Computer.config(comp1)
Computer.config(comp2)

print()

comp1.config()
comp2.config()

print()

comp1.cpu = 'i7'
comp1.ram = '8gb'

print(comp1.cpu)
print(comp2.ram)

print()

comp1.compare(comp2)

print('------------------------------------------------------------------------------------------------------')

class Car:
    
    # Class Object Variables/Attributes
    wheels = 4
    
    def __init__(self):
        # Instance Variables/Attributes
        self.mil = 10
        self.comp = 'BMW'
        
c1 = Car()
c2 = Car()

c2.mil = 8

Car.wheels = 2

print(c1.mil, c1.comp, c1.wheels)
print(c2.mil, c2.comp, c2.wheels)

print('------------------------------------------------------------------------------------------------------')

# Outer Class
class Student:
    
    school = 'ABC'
    
    def __init__(self, name, rollno, m1, m2, m3):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()
    
    # Instance Methods   
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
     
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    
    def get_marks(self):
        return (self.m1, self.m2, self.m3)
    
    def set_marks(self, marks: tuple):
        self.m1 = marks[0]
        self.m2 = marks[1]
        self.m3 = marks[2]
        
    # Class Methods
    @classmethod
    def get_school(student):
        print('Student belongs to', student.school,'School')
        
    # Static Methods
    @staticmethod
    def info():
        print('This is a Student Class')
       
    # Inner Class 
    class Laptop:
        
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'Ryzen 5'
            self.ram = '16gb'
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
        
s1 = Student('Naveen', 1,32, 53, 42)
s2 = Student('Jenny', 2, 42, 53, 74)

s1.show()
s2.show()

print()

print(s2.get_marks())

print()

print(s1.avg())
print(s2.avg())

print()

Student.get_school()
s2.get_school()

print()

Student.info()
s2.info()

print()

print(Student.Laptop().brand)
print(s2.Laptop().cpu)
print(s2.lap.ram)

print('------------------------------------------------------------------------------------------------------')

# Super class/Parent Class
class A:
    
    def __init__(self):
        print('A is created')
    
    def feature1(self):
        print('Feature 1 is working')
        
    def feature2(self):
        print('Feature 2 is working')
        
a = A()

a.feature1()
a.feature2()

print()

# Single Level Inheritance
# Sub Class/Child Class
class B(A):
    
    # Constructor in Inheritance
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print('B is created')
    
    def feature3(self):
        print('Feature 3 is working')
        
    def feature4(self):
        print('Feature 4 is working')
        
b = B()

b.feature1()
b.feature2()
b.feature3()
b.feature4()

print()

# Multi Level Inheritance
class C(B):
    
    def __init__(self):
        print('C is created')
    
    def feature5(self):
        print('Feature 5 is working')
        
c = C()

c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()

# Multiple Inheritance
# class C(A, B):
    
#     def __init__(self):
#         super().__init__() # Calls __init__ of Super Class Prioritized from left to right
#         print('C is created')

print('------------------------------------------------------------------------------------------------------')

# Polymorphism
class VSCode:
    
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('compiling')
        print('running')
        
class Pycharm:
    
    def execute(self):
        print('Compiling')
        print('Running')
        
class Laptop:
    
    # Duck Typing
    def code(self, ide):
        ide.execute()
        
ide1 = VSCode()
ide2 = Pycharm()
        
lap = Laptop()

lap.code(ide1)

print()

lap.code(ide2)

print()

class Marks:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    # Operator Overloading
    def __add__(self, m):
        m1 = self.m1 + m.m1
        m2 = self.m2 + m.m2
        
        return Marks(m1, m2)
    
    def __gt__(self, m):
        t1 = self.m1 + self.m2
        t2 = m.m1 + m.m2
        
        if t1 > t2:
            return True
        else:
            return False
        
    def __str__(self):
        return f'{self.m1}, {self.m2}'
    
    # Method Overloading
    def sum(self, a=0, b=0, c=0):
        return a + b + c
    
    # Not Supported in python
    # def sum(self, a, b, c):
    #     return a + b + c
        
m1 = Marks(31, 52)
m2 = Marks(43, 65)

m3 = m1 + m2
print(m3.m1, m3.m2)

print()

if m1 > m2:
    print('Student 1 is clever')
else:
    print('Student 2 is clever')
    
print()

print(m1)

print()

print(m2.sum(4, 8))

print()

class Parent:
    
    def show(self):
        print('Currently in Parent')
        
class Child(Parent):
    
    # Method Overriding
    def show(self):
        print('Currently in Child')

parent = Parent()
parent.show()

child = Child()
child.show()