'''
5.3. Очередь к Дракону

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Один Дракон из далёких-далёких синих гор держит у себя в замке принцессу и никому её не отдает. А принцесса то с хорошим приданным, да и выглядит прекрасно. 
Поэтому и не стоит удивляться, что около замка выстроилась довольно длинная очередь из всякого рода рыцарей, желающих победить Дракона и освободить принцессу. 
А поскольку много рыцарей в одном месте быстро образуют очень неприятную толпу, которая своим шумом мешает принцессе проводить свой досуг, 
Дракон решил установить некоторые правила касательно порядка в очереди:
1. Обычные рыцари должны вставать в конец очереди.
2. Рыцари-дворяне, знающие особый пароль, встают ровно в ее середину, причем при нечетной длине очереди они встают сразу за центром.
3. Если среди рыцарей объявится принц, то он встает в начало очереди.
Так как рыцари не особо хотят слушать дракона, а уж тем более выполнять его правила, то дракон попросил вас написать программу, 
которая могла бы отслеживать порядок рыцарей в очереди.

Описание входных данных
В первой строке входных данный записано число N (1 <= N <= 10 ** 5) − количество запросов. Следующие N строк содержат описание запросов в формате:
+ i - Рыцарь с номером i (1 <= i <= N) встает в конец очереди.
* i - Рыцарь - дворянин с номером i встает в середину очереди.
! i - Рыцарь - принц с номером i встает в начало очереди. Гарантируется, что на всю очередь может быть только один принц.
- - Первый рыцарь из очереди идет биться с драконом. Гарантируется, что на момент такого запроса очередь не пуста.

Описание выходных данных
Для каждого запроса типа "-" программа должна вывести номер рыцаря, который должен идти биться с драконом.

Формат ввода
8
+ 1
+ 2
* 3
! 4
-
-
-
-

Формат вывода
4
1
3
2
'''

class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next, self.prev = None, None

    def __init__(self):
        self.start = self.end = self.center = self.Node(None)
        self.length = 0

    def check_if_empty(self, node):
        if self.start.value is None:
            self.start = self.end = self.center = node
            return True
        return False

    def add_to_start(self, value):
        self.length += 1
        new_node = self.Node(value)
        if self.check_if_empty(new_node):
            return
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node
        if self.length % 2 == 0:
            self.center = self.center.prev

    def insert(self, node, value):
        new_node = self.Node(value)
        next_node = node.next
        if next_node is None:
            new_node.next = None
            node.next = new_node
            new_node.prev = node
            self.end = new_node
            return
        next_node.prev = new_node
        new_node.next = next_node
        node.next = new_node
        new_node.prev = node
        self.length += 1
        if self.length % 2 == 1:
            self.center = self.center.next

    def add_to_the_end(self, value):
        self.length += 1
        new_node = self.Node(value)
        if self.check_if_empty(new_node):
            return
        self.insert(self.end, value)
        if self.length % 2 == 1:
            self.center = self.center.next

    def front_pop(self):
        result = self.start
        self.start = self.start.next
        return result.value


dragon_queue = DoubleLinkedList()
res = ''
for _ in range(int(input())):
    in_put = input()
    if '+' in in_put:
        dragon_queue.add_to_the_end(in_put.split()[1])
    elif '*' in in_put:
        dragon_queue.insert(dragon_queue.center, in_put.split()[1])
    elif '!' in in_put:
        dragon_queue.add_to_start(in_put.split()[1])
    else:
        res += str(dragon_queue.front_pop()) + '\n'
print(res)
