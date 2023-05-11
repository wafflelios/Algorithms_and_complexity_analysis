'''
11.3. Математическая вечность

Ограничение времени: 6 секунд
Ограничение памяти: 48.0 Мб
Ввод стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Кай попал в плен к Снежной королеве, которая в прошлом преподавала комбинаторику. Его заставляют преобразовывать последовательность кубиков с числами не содержащие нулей при помощи следующего разрешенного набора действий:
Можно перевернуть первый кубик в последовательности, тем самым увеличить первую цифру числа на 1, если она не равна 9.
Можно перевернуть последний кубик в последовательности, тем самым уменьшить последнюю цифру на 1, если она не равна 1.
Можно циклически сдвинуть все кубики на одну вправо.
Можно циклически сдвинуть все кубики на одну влево.
Например, применяя эти правила к числу 1234 можно получить числа 2234, 1233, 4123 и 2341 соответственно.
В плену очень холодно и голодно, поэтому Каю нужно из одной последовательности кубиков получить другую за минимальное количество операций.

Описание входных данных
Во входном файле содержится два различных числа, с одинаковым количеством разрядов n (2⩽n⩽6), каждое из которых не содержит нулей.

Описание выходных данных
Программа должна вывести последовательность чисел, не содержащих нулей. Последовательность должна начинаться первым из данных чисел и заканчиваться вторым из данных чисел, каждое последующее число в последовательности должно быть получено из предыдущего числа применением одного из правил. 
Количество чисел в последовательности должно быть минимально возможным.

Формат ввода
1234
4321

Формат вывода
1234
2234
3234
4323
4322
4321

Примечания
Если существует несколько последовательностей одинаковой минимальной длины, то выполняйте действия в такой последовательности, как они указаны в задании.
'''

from collections import deque
import math


def plus_one(num, divider):
    if num // divider != 9:
        return num + divider
    return num


def minus_one(num):
    if num % 10 != 1:
        return num - 1
    return num

def shift_right(num, divider):
    return (num % 10) * divider + num // 10

def shift_left(num, divider):
    return (num % divider) * 10 + num // divider


def bfs(root, end):
    visited, queue = {}, deque()
    visited[root] = None
    queue.append(root)
    divider = 10 ** math.floor(math.log10(root))
    while queue:
        current = queue.popleft()
        after_operations = [plus_one(current, divider), minus_one(current),
                            shift_right(current, divider), shift_left(current, divider)]
        for changed_num in after_operations:
            if changed_num not in visited:
                queue.append(changed_num)
                visited[changed_num] = current
                if changed_num == end:
                    result = []
                    while changed_num is not None:
                        result.append(changed_num)
                        changed_num = visited[changed_num]
                    return result[::-1]


root = int(input())
end = int(input())
res = bfs(root, end)
for num in res:
    print(num)
