'''
12.2. Удаление из кучи

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Продолжайте работать со структурой "куча", реализованной в прошлой задаче.
Добавьте в неё следующие функции:

1. pop − программа должна удалить наименьший элемент из кучи и вывести его значение.
2. structure − программа должна вывести структуру кучи: в первой строке вывести
---STRUCTURE START---
далее вывести каждый её слой (элементы кучи одинаковой глубины) в отдельной строке через пробел, начиная с 0 глубины (корня), и после вывести
---STRUCTURE END---
в отдельной строке после слоёв (см. формат вывода для примера).

Описание входных данных
Вводятся команды управления очередью, по одной на строке.

Описание выходных данных
Требуется вывести протокол работы с очередью, по одному сообщению на строке.

Формат ввода
add 1
add 2
add 0
add 3
structure
pop
structure
exit

Формат вывода
ok
ok
ok
ok
---STRUCTURE START---
0
2 1
3
---STRUCTURE END---
0
---STRUCTURE START---
1
2 3
---STRUCTURE END---
bye

Примечания
При проходе вниз, если оба потомка равны между собой, то выбирайте левого.
'''

class Heap:
    def __init__(self):
        self.heap = list()

    def add(self, elem: int):
        index = len(self.heap)
        self.heap.append(elem)
        self.sift_up(index)
        return 'ok'

    def sift_up(self, index):
        if index == 0:
            return
        prev = (index - 1) // 2
        if self.heap[prev] > self.heap[index]:
            self.heap[prev], self.heap[index] = self.heap[index], self.heap[prev]
            self.sift_up(prev)

    def get_min(self):
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def pop(self):
        min_val = self.get_min()
        self.heap[0] = self.heap[self.size() - 1]
        self.heap.pop()
        self.sift_down(0)
        return min_val

    def sift_down(self, index):
        if index * 2 + 1 >= self.size():
            return
        left, right = index * 2 + 1, index * 2 + 2
        min_child = left
        if right < self.size() and self.heap[right] < self.heap[left]:
            min_child = right
        if self.heap[min_child] >= self.heap[index]:
            return
        self.heap[index], self.heap[min_child] = self.heap[min_child], self.heap[index]
        self.sift_down(min_child)

    def structure(self):
        print('---STRUCTURE START---')
        line, max_amount, counter = [], 1, 1
        for elem in self.heap:
            line.append(elem)
            if len(line) >= max_amount:
                print(' '.join(str(el) for el in line))
                line, max_amount, counter = [], 2 ** counter, counter + 1
        if line:
            print(*line)
        print('---STRUCTURE END---')


heap = Heap()
in_put = ''
while in_put != 'exit':
    in_put = input()
    if 'add' in in_put:
        command, num = in_put.split()
        num = int(num)
        print(heap.add(num))
    elif in_put == 'min':
        print(heap.get_min())
    elif in_put == 'size':
        print(heap.size())
    elif in_put == 'pop':
        print(heap.pop())
    elif in_put == 'structure':
        heap.structure()
print('bye')
