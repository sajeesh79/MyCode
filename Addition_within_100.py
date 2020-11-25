import random

def gen_random(min_n, max_n):
    min_number = min_n
    max_number = max_n
    num1 = str(random.randint(min_number, max_number))
    n1 = (len(str(max_number)) - len(num1)) * '0' + num1
    num2= str(random.randint(min_number, max_number))
    n2 = (len(str(max_number)) - len(num2)) * '0' + num2
    sum_n1_n2 = int(n1) + int(n2)
    return [n1, n2, sum_n1_n2]


