#!/usr/bin/python3
my_list = [4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45]
maximum=my_list[0]
minimum=my_list[0]

for each in my_list:
    if each > maximum: 
        each, maximum=maximum, each

    if each < minimum:
        each, minimum=minimum, each


print('List = {}'.format(my_list))
print('Maximum number = {}'.format(maximum)) 
print('Minimum number: {}'.format(minimum))
