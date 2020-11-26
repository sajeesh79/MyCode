import random

def gen_random(min_n, max_n):
    min_number = min_n
    max_number = max_n
    num1 = random.randint(min_number, max_number)
    # n1 = (len(str(max_number)) - len(num1)) * '0' + num1
    num2 = random.randint(min_number, max_number)
    # n2 = (len(str(max_number)) - len(num2)) * '0' + num2
    sum_n1_n2 = num1 + num2
    return [num1, num2, sum_n1_n2]
    # return [n1, n2, sum_n1_n2]


def gen_random_for_first(min_n, max_n):
    min_number = min_n
    max_number = max_n
    num = random.randint(min_number, max_number)
    # n = (len(str(max_number)) - len(num)) * '0' + num
    return num


def gen_random_for_second(min_n, max_n):
    min_number = min_n
    max_number = max_n
    num = random.randint(min_number, max_number)
    # n = (len(str(max_number)) - len(num)) * '0' + num
    return num

