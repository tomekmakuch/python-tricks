class Test:
	def __init__(self):
		self.a = 11
		self._b = 12
		self.__c = 13

t = Test()
print(dir(t))


class ExtendedTest:
	def __init__(self):
		super().__init__()
		self.a = 'modified'
		self._b = 'modified'
		self.__c = 'modified'

import ipdb; ipdb.set_trace()