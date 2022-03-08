
class FileManagerExample:
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		self.file = open(self.name, 'w')
		return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.file:
			self.file.close()


with FileManagerExample('hello.txt') as f:
	f.write('hello, world!\n')
	f.write('\nbye now!')

