import math
def solution(num_list):
    list_mul = 1
    for i in num_list:
        list_mul *= i
    list_sum = sum(num_list)**2
    return 1 if list_mul<list_sum else 0