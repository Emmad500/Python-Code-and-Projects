# CH 9
#Multiple Inheritence
# class Employee:
#     company = "ITC"
#     name = "Default name"

#     def show(self):
#         print(f"The name of the Employee is {self.name} and the company is {self.company}")

# class coder:
#     language = "Python"
#     def printLanguages(self):
#         print(f"Out of all the languages here is your language: {self.language}")

# class Programmer(Employee, coder):
#     company = "ITC InfoTech"
#     def showLanguage(self):
#         print(f"The name is {self.company} and he is good with {self.language} language")

# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguages()
# b.showLanguage()

#Multilevel Inheritance
# class Employee:
#     a = 1

# class Programmer(Employee):
#     b = 2

# class Manager(Programmer):
#     c = 3

# o = Employee()
# print(o.a) #Prints the a attribute 
# # print(o.b) #shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)

#Super method
# class Employee:
#     def __init__(self) -> None:
#         print("Constructor of Employee")
#     a = 1

# class Programmer(Employee):
#     def __init__(self) -> None:
#         print("Constructor of Programmer")
#     b = 2

# class Manager(Programmer):
#     def __init__(self) -> None:
#         super().__init__()
#         print("Constructor of Manager")
#     c = 3

# o = Employee()
# print(o.a) #Prints the a attribute 


# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)

#Class Method
# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")

# e = Employee()
# e.a = 45

# e.show()

#Property Decorators
# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

#         @property
#         def name(self):
#             return f"{self.fname} {self.lname}"

#         @name.setter
#         def name (self, value):
#             self.fname = value.split(" ")[0]
#             self.lname = value.split(" ")[1]


# e = Employee()
# e.a = 45

# e.name = "emad raza"
# print(e.fname, e.lname)

# e.show()


#Operator overloading

class Number:
    def __init__(self, n) -> None:
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)
