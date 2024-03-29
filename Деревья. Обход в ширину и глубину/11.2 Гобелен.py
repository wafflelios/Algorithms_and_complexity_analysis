'''
11.2. Гобелен

Ограничение времени: 1 секунда
Ограничение памяти: 128.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Два маленьких друга, Войтек и Казимир, нашли в одной заброшенной деревеньке один заброшенный дом. На заброшенном чердаке этого заброшенного дома висел большой-большой гобелен с генеалогическим деревом. Под каждым именем, чтобы не было путаницы, был указан уникальный идентификатор. 
К своему удивлению, на этом гобелене наши маленькие друзья нашли свои имена. Друзья догадались, что они не только друзья, но теперь еще и родственники. Осталось только найти их ближайшего общего предка. Помогите маленьким друзьям-родственникам решить эту задачку.

Описание входных данных
В первой строке дано целое число n − количество вершин генеалогического дерева. (3 <= n <= 5 * 10 ** 4)
В следующей строке представлено генеалогическое дерево в виде словаря, где ключ − родитель, значение (в виде списка) − дети. Первый ключ такого словаря является корнем всего дерева. Числа в словаре неотрицательны и не могут превышать число n.
Так, например, словарь G = {5: [1, 4], 4: [3, 2, 0], 0: [6, 7, 8]} можно визуализировать следующим образом:

11.2.png

В третьей строке входных данных через пробел указаны вершины a и b.

Описание выходных данных
В единственной строке выходных данных выведите одно число - ближайшего общего предка для вершин a и b.

Формат ввода
9
{5: [1, 4], 4: [3, 2, 0], 0: [6, 7, 8]}
1 6

Формат вывода
5
'''
import ast

amount_of_nodes = int(input())
str_tree = input()
tree = ast.literal_eval(str_tree)
boy_1, boy_2 = map(int, input().split())

ORDER, DEPTH = [], []


def dfs(graph, start, depth=0):
    global ORDER, DEPTH
    for nxt in graph[start]:
        DEPTH.append(depth)
        ORDER.append(start)
        if nxt in graph.keys():
            dfs(graph, nxt, depth + 1)
        else:
            DEPTH.append(depth + 1)
            ORDER.append(nxt)

def find_lsa():
    left = ORDER.index(boy_1)
    right = ORDER.index(boy_2)
    if right < left:
        right, left = left, right
    min_depth, res = amount_of_nodes, 0
    for node in range(left + 1, right):
        if DEPTH[node] < min_depth:
            res = ORDER[node]
            min_depth = DEPTH[node]
    return res


dfs(tree, list(tree.keys())[0])
result = find_lsa()
print(result)
