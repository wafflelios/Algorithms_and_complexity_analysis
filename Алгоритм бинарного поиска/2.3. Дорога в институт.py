import math

v_outside, v_inside = map(int, input().split())
s_not_city = int(input())


def get_time(middle):
    time_outside = math.sqrt(pow(middle, 2) + pow(s_not_city / 100, 2)) / v_outside
    time_inside = math.sqrt(pow(1 - middle, 2) + pow(1 - s_not_city / 100, 2)) / v_inside
    return time_outside + time_inside


begin, end = 0, 1
while end - begin > 10 ** -7:
    middle_b = begin + (end - begin) / 3
    middle_e = end - (end - begin) / 3
    if get_time(middle_b) < get_time(middle_e):
        end = middle_e
    else:
        begin = middle_b
print('%.6f' % begin)
