#through Generators
def fibonacci(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


f = fibonacci(100)
for x in f:
    print(x)

#through List
def fibonacci2(number):
    result = []
    a = 0
    b = 1
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


f2 = fibonacci2(100)
print(f2)
