'''
@author: SOURABH GUPTA
'''
'''
Create a module "number_checker.py" which has following 2 functions:
•is_prime(num) : this function returns true if the input number is prime
•is_even(num): this function returns true if the input number is even
•Create another Python module "test_module.py".
•Invoke the functions "is_prime(num)" and "is_even(num)" in "test_module.py".
•Observe the results.
'''
def is_prime(num):
    flag = 0
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            flag = 1
            break
        else:
            flag = 0
    if flag == 1:
        return True
    else:
        return False

def is_even(num):
    flag = 0
    if num % 2 == 0:
        flag = 1
    else:
        flag = 0
    if flag == 1:
        return True
    else:
        return False
