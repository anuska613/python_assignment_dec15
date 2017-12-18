#!/usr/bin/python3
list_num=[1, 2, 3, 4, 6, 7, 8, 9]

def cubed(list_num):
    cubed_list=list();
    for each in list_num:
        cube=each**3
        cubed_list+=[cube]

    return cubed_list


cubed_list=cubed(list_num)

print('Original list\t = {}\nCubed list\t = {}'.format(list_num,cubed_list))
    
