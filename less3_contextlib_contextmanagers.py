from contextlib import contextmanager

@contextmanager
def file_manager_example(name):
	try:
		f = open(name, 'w')
		yield f
	finally:
		f.close()

with file_manager_example('hello.txt') as f:
	f.write('less 3 hello world')
	f.write('less 3 bye now')

