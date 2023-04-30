'''
2.2. Монструозная планета

Ограничение времени: 6 секунд
Ограничение памяти: 128.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

На некоторой планете Икс существуют 2 вида монстров: многоножки и многоручки. 
Чтобы им было комфортнее жить, представители каждого вида разделились на несколько групп одинаковой длины l. У многоножек получилось 
n групп, а у многоручек - m. Чтобы не запутаться, кто в каком отряде, многоножки и многоручки решили вести письменный учет членов группы. 
Но путаница всё же произошла! Многоножки записывали своих участников в список в таком порядке, чтобы количество ног монстров не убывали, 
а многоручки записывали так, чтобы количество рук монстров в списке не возрастали!
И решили монстры планеты Икс создать новый вид - многоножеручек с помощью новейшего изобретения "Скрещиватель 3000" путём объединения двух монстров 
из разных групп многоножек и многоручек. Однако монстры испугались, что если брать монстров с разных позиций в списках, то начнётся новая путаница! 
При этом, всем известно, что много конечностей у монстра - это плохо. Монстры обратились к вам за помощью: помогите найти такую позицию 
k в двух списках, чтобы максимальное количество одинаковых конечностей монстров на позиции 
k каждого списка, было минимальным (Например, объединим монстра с 5 ногами и монстра с 9 руками. Максимальное количество одинаковых конечностей - 9).
Если таких k несколько, выведите максимальное значение.

Описание входных данных:
В первой строке даны 3 числа: n, m и l (1 <= n, m <= 900; 1 <= l <= 3000). Следующие n строк содержат описания списков многоножек, каждый список описывается
перечислением l элементов через пробел (кол-во ног многоножки). Элементы - целые числа от 0 до 10 ** 5 - 1. Далее идут m списков многоручек в таком же формате. 
Списки и позиции монстров в них нумеруются с 0. В следующей строке число запросов q (1 <= q <= m * n). Следующие q строк содержат пары чисел i, j 
(0 <= i <= n - 1, 0 <= j <= mm - 1)

Описание выходных данных:
Выведите q чисел от 1 до l - 1 - ответы на запросы.

Формат ввода
4 3 5
1 2 3 4 5
1 1 1 1 1
0 99999 99999 99999 99999
0 0 0 0 99999
5 4 3 2 1
99999 99999 99999 0 0
99999 99999 0 0 0
12
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2

Формат вывода
2
3
2
4
4
4
0
4
4
3
3
3
'''


def main():
    legs_groups, arms_groups, amount = input().split()
    amount = int(amount)
    legs_arr, arms_arr, answer = [], [], []
    for __ in range(int(legs_groups)):
        legs_arr.append(list(map(int, input().split())))
    for __ in range(int(arms_groups)):
        arms_arr.append(list(map(int, input().split())))
    requests_amount = int(input())
    for __ in range(requests_amount):
        leg_index, arm_index = map(int, input().split())
        start, end, val_minim, middle = 0, amount - 1, 9999999, 0
        while end - start > 1:
            middle = (end - start) // 2 + start
            if legs_arr[leg_index][middle] <= arms_arr[arm_index][middle]:
                start = middle
            elif legs_arr[leg_index][middle] > arms_arr[arm_index][middle]:
                end = middle
            if val_minim >= max(legs_arr[leg_index][middle], arms_arr[arm_index][middle]):
                val_minim = max(legs_arr[leg_index][middle], arms_arr[arm_index][middle])
        if end - start == 1:
            if int(max(legs_arr[leg_index][end], arms_arr[arm_index][end])) <= \
                    int(max(legs_arr[leg_index][start], arms_arr[arm_index][start])):
                start = end
                for counter in range(end + 1, amount):
                    if legs_arr[leg_index][counter] == legs_arr[leg_index][end]:
                        start += 1
                    else:
                        break
            answer.append(start)
        elif int(max(legs_arr[leg_index][0], arms_arr[arm_index][0])) == \
                int(max(legs_arr[leg_index][amount - 1], arms_arr[arm_index][amount - 1])):
            answer.append(amount - 1)
    print(*answer, sep='\n')


main()
