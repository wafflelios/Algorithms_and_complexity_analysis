def merge_sort(lst, begin, end):
    if end - begin > 1:
        middle = (begin + end) // 2
        merge_sort(lst, begin, middle)
        merge_sort(lst, middle, end)
        merge(lst, begin, middle, end)


def merge(lst, begin, middle, end):
    global pairs
    left_s = lst[begin: middle]
    right_s = lst[middle: end]
    len_left, len_right = len(left_s), len(right_s)
    main_p, l_point, r_point = begin, 0, 0
    while l_point < len_left and r_point < len_right:
        if left_s[l_point] >= right_s[r_point]:
            lst[main_p] = left_s[l_point]
            l_point += 1
            pairs += len_right - r_point
        else:
            lst[main_p] = right_s[r_point]
            r_point += 1
        main_p += 1
    while r_point < len_right:
        lst[main_p] = right_s[r_point]
        r_point += 1
        main_p += 1
    while l_point < len_left:
        lst[main_p] = left_s[l_point]
        l_point += 1
        main_p += 1
        pairs += len_right - r_point


amount = int(input())
rocks, pairs = [], 0
for _ in range(amount):
    rocks.append(int(input()))
copy = rocks.copy()
merge_sort(copy, 0, len(rocks))
if rocks == copy[::-1] and rocks != [rocks[0]] * amount:
    print(0)
else:
    print(pairs)
