'''
7.1. Камешки

Ограничение времени: 1.5 секунд
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Заключённый Коленька сидит в одиночной камере. Ему очень скучно. Ему абсолютно нечем заняться. Поэтому он придумал себе очень увлекательную задачу! 
На прогулке по тюремному двору он набрал в карманы камешки, принёс к себе в камеру, разложил все камешки в один ряд и посчитал их размеры. 
Коленьке стало интересно, сколько для всех камешков (массива K = <k_1, k_2, ..., k_n>, где k_i - размер камешка) найдется таких пар (i, j), что
i < j и k_i >= k_j. Он принялся считать, но что-то его постоянно отвлекает, и ему приходится начинать сначала. 
Закончите мучения Коленьки и помогите ему написать программу, которая решит его задачку.

Описание входных данных
Первая строка входных данных содержит натуральное число N (1 <= N <= 100000) - кол-во камешков. Следующие N строк содержат элементы массива 
K - целых неотрицательных чисел, не превосходящих 10 ** 9

Описание выходных данных
Программа должна вывести одно число — ответ на задачу

Формат ввода
6
179
4
3
2
1
1

Формат вывода
15
'''

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
