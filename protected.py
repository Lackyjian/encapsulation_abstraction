class Base:
	def __init__(self):
		self._a = 2
class Derived(Base):
	def __init__(self):
		Base.__init__(self)
obj1 = Derived()
print("Accessing protected member of obj1: ", obj1._a)
