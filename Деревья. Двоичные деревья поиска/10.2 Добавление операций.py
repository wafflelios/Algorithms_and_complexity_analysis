'''
10.2. Добавление операций

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Мы написали двоичное дерево. Очень здорово! Но зачем оно нам, если мы не можем провести с ним никаких операций? Поэтому давайте добавим парочку команд:
1. add <число/список чисел> - Добавить число/список чисел в дерево и вывести "Ok".
2. delete <число> - Удалить число из дерева и вывести "Ok".
3. find <число> - Найти число в дереве. Если такое имеется, вывести "Число нашлось". Если такого не имеется, то вывести "Число не нашлось".
4. next <число> - Вывести следующее после введённого числа число. Если следующего числа нет, то вывести "Следующего числа нет". 
(Гарантируется, что для этой команды числа будут браться из дерева).
5. print - Вывести дерево в том же формате, что и в предыдущей задаче.
6. exit - Выйти из программы.

Описание входных данных
Первой строкой вводится отсортированный список длины n (1 <= n <= 10 ** 4) Следующими строками вводятся команды управления двоичным деревом, по одной на строке.
Гарантируется, что команд не больше 2 * 10 ** 4.
 
Описание выходных данных
Требуется вывести протокол работы с двоичным деревом, по одному сообщению на строке.

Формат ввода
1 3 4 10 13
print
delete 3
print
add 7 6 8
print
find 7
find 3
next 4
next 13
exit

Формат вывода
4
├───3
│   └───1
└───13
    └───10
Ok
4
├───1
└───13
    └───10
Ok
4
├───1
└───13
    └───10
        └───7
            ├───6
            └───8
Число нашлось
Число не нашлось
6
Следующего числа нет
'''

class Node:
    def __init__(self, num: int, parent, left=None, right=None):
        self.num, self.left, self.right, self.parent = num, left, right, parent


class Tree:
    def __init__(self, root):
        self.root = root

    def add(self, node, num):
        if self.root is None:
            self.root = Node(num, None)
            return
        if node is None:
            return
        if num < node.num:
            if node.left is None:
                node.left = Node(num, node)
                return
            self.add(node.left, num)
        else:
            if node.right is None:
                node.right = Node(num, node)
                return
            self.add(node.right, num)

    def find(self, num):
        return self.find2(num, self.root)

    def find2(self, num, node):
        if node is None:
            return
        if node.num == num:
            return node
        if node.num > num:
            return self.find2(num, node.left)
        else:
            return self.find2(num, node.right)

    def delete(self, num):
        if self.root is None:
            return
        node = self.find(num)
        if node:
            self.delete2(node)

    def delete2(self, node):
        if node.left is None or node.right is None:
            if node.left:
                child = node.left
            else:
                child = node.right
            if node is self.root:
                self.root = child
                if child:
                    child.parent = None
            else:
                if node.parent.left == node:
                    node.parent.left = child
                    if child:
                        child.parent = node.parent
                else:
                    node.parent.right = child
                    if child:
                        child.parent = node.parent
        else:
            next_node = node.right
            while next_node.left:
                next_node = next_node.left
            node.num = next_node.num
            self.delete2(next_node)


def create_balanced_tree(arr, start, end):
    if start + 1 > end:
        return None
    if start + 1 == end:
        return Node(arr[start], None)
    if (start + end) % 2 == 0:
        middle = (start + end) // 2 - 1
    else:
        middle = (start + end) // 2
    node = Node(arr[middle], None)
    node.left = create_balanced_tree(arr, start, middle)
    node.right = create_balanced_tree(arr, middle + 1, end)
    if node.left is not None:
        node.left.parent = node
    if node.right is not None:
        node.right.parent = node
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
array_copy = array.copy()
tree = Tree(create_balanced_tree(array, 0, len(array)))
request = ''
while request != 'exit':
    request = input()
    if 'add' in request:
        values = request.split(maxsplit=1)[1]
        for value in values.split():
            value = int(value)
            array_copy.append(value)
            tree.add(tree.root, value)
        print('Ok')
    elif 'delete' in request:
        value = request.split()[1]
        value = int(value)
        if value in array_copy:
            array_copy.remove(value)
        tree.delete(value)
        print('Ok')
    elif 'find' in request:
        value = request.split()[1]
        value = int(value)
        if tree.find(value):
            print('Число нашлось')
        else:
            print('Число не нашлось')
    elif 'next' in request:
        value = request.split()[1]
        value = int(value)
        array_copy = sorted(array_copy)
        try:
            print(array_copy[array_copy.index(value) + 1])
        except IndexError:
            print('Следующего числа нет')
    elif request == 'print':
        print_root(tree.root)
