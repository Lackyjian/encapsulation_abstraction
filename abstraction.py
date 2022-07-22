from abc import ABC, abstractmethod
class student(ABC):
    @abstractmethod
    def m1(self):
        pass
class A(student):
    def m1(self):
        print("m1")
ob = A()
ob.m1()