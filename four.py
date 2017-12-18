#!/usr/bin/python3
def solve_for_y(x_values):
    m=45
    c=0.5
    print('m = {}, c = {}, Now, y=mx+c,'.format(m,c))
    for x in x_values:
        y=45*x+c
        print('\nx = {},  ==>>  y = {:.2f}'.format(x,y))

solve_for_y([1, 2.3, 5.6, 7, 78])
