# 1.
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

# ['qux']
print(max(a[2:4] + ['grault']))

# ['quux', 'baz', 'foo']
print(a[4::-2])

# ['foo']
print(a[-6])

# Flase
print(a[:] is a)

# 2.
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']

# 'z' from 'baz'
print(x[1][2][1][2])

# ["baz",2.718]
print(x[1][2][1:])

# 3.
a = [1, 2, 7, 8]

# [1, 2, 3, 4, 5, 6, 7, 8]
a[2:2] = [3, 4, 5, 6]
print(a)

# 4
x = 5
y = -5
x, y = (y, x)[::-1]
print(x,y)
# same value