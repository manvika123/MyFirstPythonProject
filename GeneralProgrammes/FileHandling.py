with open('sample.txt', mode='r+') as my_file:  # a= append
    # print(my_file.read())
    # my_file.seek(0)
    # text= my_file.write('Hey it\'s me!')
    text = my_file.write(':)')
    print(text)
    print(my_file.readlines())

# print(my_file.readline())
# my_file.close()
