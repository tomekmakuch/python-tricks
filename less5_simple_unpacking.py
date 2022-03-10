some_var = ('a', 'b', 'c', 'd', 'e')

some_a, some_b, some_c, some_d, _ = some_var

print('some_a: ' + some_a)
print('some_b: ' + some_b)
print('some_c: ' + some_c)
print('some_d: ' + some_d)
print('_: ' + _)

# IMPORTANT!
# _ is a special variable that holds the last results of the interpreter

# >>> 10 + 10
# 10
# >>> _
# 10
