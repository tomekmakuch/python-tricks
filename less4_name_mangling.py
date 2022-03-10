class Test:
	def __init__(self):
		self.a = 11
		self._b = 12
		self.__c = 13


class ExtendedTest(Test):
	def __init__(self):
		super().__init__()
		self.a = 'modified'
		self._b = 'modified'
		self.__c = 'modified'

	def get_mangled(self):
		return self.__c


_ManagledGlobal__mangled = 23

class ManagledGlobal:
	def test(self):
		return __mangled

print(ManagledGlobal().test())

# Dunder methods ("double underscore")


class SomeClass:

	# example of a dunder method
	def __init__(self):
		pass

	# example of a dunder method
	def __call__(self):
		pass

