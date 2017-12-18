#!/usr/bin/python3
def name():
    full_name=input('Enter you full name: ')
    return full_name.split(" ")

name_temp=name()
if (len(name_temp)==3):
    first_name, middle_name, last_name=name_temp
    print('First name:\t{}\nMiddle name:\t{}\nLast name:\t{}'.format(first_name, middle_name, last_name))

else:
    first_name, last_name=name_temp
    print('First name:\t{}\nLast name:\t{}'.format(first_name, last_name))
