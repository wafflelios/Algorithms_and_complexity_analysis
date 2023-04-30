import random


def find_order_statistic(array, num, extra_id=None):
    if extra_id is None:
        extra_id = 0
    r_num, flag = random.choice(array), True
    less_el, bigger_el, equal_el = [], [], []
    for el in array:
        if el < r_num or el == r_num and not flag:
            less_el.append(el)
        elif el > r_num:
            bigger_el.append(el)
        elif flag:
            equal_el.append(el)
            flag = False
    if len(less_el) + extra_id == num:
        print(r_num)
    elif num > len(less_el) + extra_id:
        find_order_statistic(bigger_el, num, extra_id + len(less_el) + len(equal_el))
    else:
        find_order_statistic(less_el, num, extra_id)


input_arr, k = list(map(int, input().split())), int(input())
find_order_statistic(input_arr, k)
