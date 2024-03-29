'''
11.1. Получить компоненту!

Ограничение времени: 0.12 секунд
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Компонента связности графа - это максимальный связный подграф графа.

11.1.png

На данном изображении 3 компоненты связности: {1; 2; 4; 6}, {0}, {3; 5}
Дан неориентированный невзвешенный граф и вершина из него. Необходимо найти все вершины, лежащие в одной компоненте связности с данной (включая эту вершину), в отсортированном порядке.

Описание входных данных:
В первой строке даны два целых числа - n и v(1 <= n <= 100; 1 <= v <= n), разделенные пробелом. Где n - количество вершин в графе (вершины нумеруются с 0), v - вершина из необходимой компоненты связности.
В следующих n строках для каждой вершины графа даны вершины, соединенные с ней ребром (или же "соседи"), разделенные пробелом (в первой строке соседи вершины 0, во второй строке соседи вершины 1, в третьей строке соседи вершины 2 и т.д.).
Если вершина не соединена ни с одной другой, то в строке будет дано "-1".

Описание выходных данных:
В единственной строке необходимо вывести все вершины графа из то же компоненты связности, что и вершина v (включая v), разделенные пробелом, в отсортированном порядке.

Формат ввода
7 4
-1
2 4
1
5
1 6
3
4

Формат вывода
1 2 4 6
'''

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start]:
        if nxt not in visited:
            dfs(graph, nxt, visited)
    return visited


amount, node = map(int, input().split())
graph = []
for _ in range(amount):
    nums = list(map(int, input().split()))
    graph.append(nums)
if graph[node] == [-1]:
    print(node)
else:
    res = sorted(dfs(graph, node))
    print(*res)
