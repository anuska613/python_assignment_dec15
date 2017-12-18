#!/usr/bin/python3
salary = [15000, 20000, 17000, 18900, 30000]

def salary_after_raise(salary):
    return salary+0.23*salary

print('Salary after raise: ')
for index, each in enumerate(salary,start=1):
    raised_salary=salary_after_raise(each)
    print('For employee {}, total salary = Rs. {:.2f}'.format(index, raised_salary))
