from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 5, 6]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

# defualt function lambda
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])

#maintains the order by this one
d= OrderedDict()
d['a']=1
d['b']=2

d2= OrderedDict()
d2['a']=2
d2['b']=1

print (d==d2)