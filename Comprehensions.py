some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#changed to set by set function then changed back to list by list function
duplicates = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates)
