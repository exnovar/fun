def square(x):
    return x**2

n = [1,4,2,10,38]

squared = map(square, n)

print(list(squared))

for square in map(lambda x: x**2, n):
    print(square)
