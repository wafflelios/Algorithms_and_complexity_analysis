'''
10.1. Построение двоичного дерева

Ограничение времени: 1.5 секунд
Ограничение памяти: 32.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Реализуйте структуру двоичного дерева. И сохраните в неё дерево, построенное из отсортированного массива.

Описание входных данных
В единственной строке входных данных подаётся массив целых чисел длинной n (1 <= n <= 10 ** 5), который нужно сохранить в дерево.

Описание выходных данных
Выводится отформатированное дерево (смотри пример). При форматировании используются следующие символы Unicode: ' ', '│', '└', '├', '─'

Формат ввода
1 3 4 9 10 10 13 15 16

Формат вывода
10
├───3
│   ├───1
│   └───4
│       └───9
└───13
    ├───10
    └───15
        └───16
        
Примечания
Подсказки по алгоритму форматирования вывода
1. Реализуйте рекурсивный алгоритм для прохода по дереву.
2. Передавайте в каждый новый запуск рекурсивной функции массив bool значений, которые показывают есть ли элементы ниже на каждом уровне вложенности.
3. Преобразите эти значения в '│', если есть элементы ниже на этом уровне, или в ' ', если нету.
4. Последний элемент аналогично, но он может принимать значения '├───' или '└───' соответственно.
5. Обработайте исключение нулевой вложенности у первого элемента.
6. Запускаете рекурсивно для каждого левого и правого ответвления, если оно не None.

Решение на Java: https://www.baeldung.com/java-print-binary-tree-diagram#2-adding-tree-edges
'''

class Node:
    def __init__(self, num: int, left=None, right=None):
        self.num, self.left, self.right = num, left, right


def create_balanced_tree(arr, start, end):
    if end < start:
        return None
    middle = (start + end) // 2
    node = Node(arr[middle])

    node.left = create_balanced_tree(arr, start, middle - 1)
    node.right = create_balanced_tree(arr, middle + 1, end)
    return node

def print_node(node, padding, pointer, has_right):
    if node is not None:
        print(f'{padding}{pointer}{node.num}')
        if has_right:
            padding += '│   '
        else:
            padding += '    '
        print_node(node.left, padding, '├───' if node.right is not None else '└───', node.right is not None)
        print_node(node.right, padding, '└───', False)

def print_root(root):
    if root is None:
        return ''
    print(root.num)
    print_node(root.left, '', '├───' if root.right is not None else '└───', root.right is not None)
    print_node(root.right, '', '└───', False)


array = list(map(int, input().split()))
tree = create_balanced_tree(array, 0, len(array) - 1)
print_root(tree)
