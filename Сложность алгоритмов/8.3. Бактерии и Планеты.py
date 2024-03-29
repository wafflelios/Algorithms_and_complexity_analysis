'''
8.3. Бактерии и Планеты

Ограничение времени: 7.5 секунд
Ограничение памяти: 8.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

В недалеком будущем британские ученые решили провести следующий эксперимент: отправить на планеты некоторой системы X несколько видов бактерий и посмотреть, 
как они на этих планетах будут развиваться.
Ученым уже известны температуры на планетах системы X, а также для каждого вида бактерий известная минимальная и максимальная температуры, 
при которых бактерия выживает. Осталось только для каждой планеты узнать, сколько видов бактерий на ней смогут выжить, 
чтобы определить целесообразность отправления на неё колоний.

Описание входных данных:
В первой строке дано целое число n (1 <= n <= 5000) - кол-во различных видов бактерий.
Далее в n строках два целых числа i и j (-10 ** 7 + 1 <= i <= j <= 10 ** 7 - 1) - минимальная и максимальная температуры 
для выживания бактерии отдельного вида соответственно.

Описание выходных данных:
Для каждой планеты в порядке появления выведите в отдельной строке количество различных видов бактерий, которые на ней выживут.

Формат ввода
10
-2 3
0 3
-1 0
-1 3
0 1
-2 -1
1 3
2 3
1 2
2 3
-3 -1 0 2 3

Формат вывода
0
4
5
7
6
'''

def main():
    amount = int(input())
    temp_diff = []
    for _ in range(amount):
        min_t, max_t = map(int, input().split())
        temp_diff.append([min_t, max_t])
    temp_diff = tuple(temp_diff)
    bacteria = tuple(map(int, input().split()))
    for bact in bacteria:
        counter = 0
        for min_t, max_t in temp_diff:
            if max_t >= bact >= min_t:
                counter += 1
        print(counter)


main()
