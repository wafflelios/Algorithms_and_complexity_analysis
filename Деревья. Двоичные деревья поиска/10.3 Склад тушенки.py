'''
10.3. Склад тушёнки

Ограничение времени: 2 секунды
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Бабушка Нина решила поностальгировать о былых временах и неожиданно для себя вспомнила о советской тушёнке, которую очень любила в юности. 
Желая снова ощутить былые эмоции, Нина тут же ринулась в магазин и начала скупать различные банки тушёнки. Конечно, так как производители тушёнки различные, 
банки отличались по весу. Придя домой с кучей банок, бабушка Нина положила всю тушёнку в кладовую. Только час спустя Нина осознала весь ужас ситуации: 
столько тушёнки ей не съесть, ведь она ей когда-нибудь надоест!
Но бабушка Нина не промах: она решила распродать всю эту тушёнку соседям! Однако она не ожидала, что покупателей будет настолько много и переутомилась. 
Пожилая бизнесвумен выделила некоторую особенность покупателей: Они очень часто просят или самую маленькую банку тушёнки, или самую большую. 
Кроме того, каждый день нужно проводить инвентаризацию, чтобы знать прибыль. А ведь еще нужно ездить по магазинам за новым товаром!
Помогите Нине: организуйте учёт банок тушёнки при помощи двоичного дерева поиска со следующими командами:
1. add <x> - добавить банку тушёнки массой x на склад и вывести "Ok"
2. delete <x> - достать банку тушёнки массой x из склада и вывести "Ok".
3. find <x> - найти банку массой x на складе. Если такое имеется, вывести "Такая банка есть". Если такой не имеется, то вывести "Такой банки нет".
4. min - вывести вес самой лёгкой банки тушёнки на складе, если на складе больше не осталось банок, вывести "Склад пуст".
5. max - вывести вес самой тяжёлой банки тушёнки на складе, если на складе больше не осталось банок, вывести "Склад пуст".
6. list - вывести веса всех банок по возрастанию через пробел (если на складе хранится несколько банок одинакового веса, вывести их все).
7. exit - выйти из программы.

Описание входных данных
Первой строкой вводится отсортированный список весов банок тушёнки, хранящихся на данный момент в кладовой Нины.
Следующими строками вводятся команды для двоичного дерева поиска, описанные выше.

Описание выходных данных
Требуется вывести протокол работы с двоичным деревом, по одному сообщению на строке.

Формат ввода
1 2 3 4 5
add 3
list
min
max
delete 5
max
delete 1
min
find 4
delete 4
find 4
list
exit

Формат вывода
Ok
1 2 3 3 4 5
1
5
Ok
4
Ok
2
Такая банка есть
Ok
Такой банки нет
2 3 3
'''

class Stew:
    def __init__(self, weight: int, parent, left=None, right=None):
        self.weight, self.left, self.right, self.parent = weight, left, right, parent


class Tree:
    def __init__(self, root):
        self.root = root

    def add(self, stew: Stew, weight: int) -> None:
        if self.root is None:
            self.root = Stew(weight, None)
            return
        if stew is None:
            return
        if weight < stew.weight:
            if stew.left is None:
                stew.left = Stew(weight, stew)
                return
            self.add(stew.left, weight)
        else:
            if stew.right is None:
                stew.right = Stew(weight, stew)
                return
            self.add(stew.right, weight)

    def find(self, weight):
        return self.find2(weight, self.root)

    def find2(self, weight, stew):
        if stew is None:
            return
        if stew.weight == weight:
            return stew
        if stew.weight > weight:
            return self.find2(weight, stew.left)
        else:
            return self.find2(weight, stew.right)

    def delete(self, weight):
        if self.root is None:
            return
        stew = self.find(weight)
        if stew:
            self.delete2(stew)

    def delete2(self, stew):
        if stew.left is None or stew.right is None:
            if stew.left:
                child = stew.left
            else:
                child = stew.right
            if stew is self.root:
                self.root = child
                if child:
                    child.parent = None
            else:
                if stew.parent.left == stew:
                    stew.parent.left = child
                    if child:
                        child.parent = stew.parent
                else:
                    stew.parent.right = child
                    if child:
                        child.parent = stew.parent
        else:
            next_stew = stew.right
            while next_stew.left:
                next_stew = next_stew.left
            stew.weight = next_stew.weight
            self.delete2(next_stew)


def create_balanced_tree(arr, start, end):
    if start + 1 > end:
        return None
    if start + 1 == end:
        return Stew(arr[start], None)
    if (start + end) % 2 == 0:
        middle = (start + end) // 2 - 1
    else:
        middle = (start + end) // 2
    stew = Stew(arr[middle], None)
    stew.left = create_balanced_tree(arr, start, middle)
    stew.right = create_balanced_tree(arr, middle + 1, end)
    if stew.left is not None:
        stew.left.parent = stew
    if stew.right is not None:
        stew.right.parent = stew
    return stew


array = list(map(int, input().split()))
array_copy = array.copy()
tree = Tree(create_balanced_tree(array, 0, len(array)))
request = ''
while request != 'exit':
    request = input()
    if 'add' in request or 'delete' in request or 'find' in request:
        value = request.split()[1]
        value = int(value)
        if 'add' in request:
            array_copy.append(value)
            tree.add(tree.root, value)
            print('Ok')
        elif 'delete' in request:
            if value in array_copy:
                array_copy.remove(value)
            tree.delete(value)
            print('Ok')
        else:
            if tree.find(value):
                print('Такая банка есть')
            else:
                print('Такой банки нет')
    elif 'min' in request or 'max' in request or 'list' in request:
        array_copy = sorted(array_copy)
        if 'min' in request:
            if len(array_copy) == 0:
                print('Склад пуст')
            else:
                print(min(array_copy))
        elif 'max' in request:
            if len(array_copy) == 0:
                print('Склад пуст')
            else:
                print(max(array_copy))
        elif 'list' in request:
            print(*array_copy)
