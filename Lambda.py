# Square
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# List Sorting

a = [(0, 2), (4, 3), (2, 9), (10, -1)]
#print(list(filter()))

a.sort(key= lambda x: x[1])
print(a)