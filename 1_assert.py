def apply_sth(some_number):
	assert some_number > 0, 'you fucking moron'
	print(f'{some_number}')

apply_sth(-1)


# Things to remember:
# Do not use assert for data validation
# - assert can be disbaled with global debug flag thefore it's not a good idea to use it like so.
