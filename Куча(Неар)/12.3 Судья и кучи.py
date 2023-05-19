'''
12.3. Судья и кучи

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Помните нашего вора в кондитерской лавке? Дак вот, его поймали. И вас, как соучастника, поймали тоже. Будут судить. Но судья человек интересный, он увлекается кучами! И может вас помиловать, если вы докажете, что помогали вору с помощью куч.
Условия задачи всё те же. Решите задачу о воре в кондитерской лавке с применением кучи.

Описание входных данных
В первойстроке входных данных содержатся натуральные числа n (количество тортов) (1 <= n <= 10 ** 5) и W (вместимость пакета) (1 <= W <= 10 ** 9). Следующие n строк содержат информацию о тортах: цену p_i (0 <= p_i <= 10 ** 9) и объем s_i (1 <= s_i <= 10 ** 9).

Описание выходных данных
В единственной строке выходных данных выведите общую стоимость тортов, которые удалось засунуть в пакет. С точностью до двух знаков после запятой.

Формат ввода
5 1000
125 400
500 1500
25 100
400 1300
250 700

Формат вывода
350.00

Примечания
Использовать heapq нельзя. Судье не понравится, когда куча сделана кем-то ещё, а не вами.
'''

class Heap:
    def __init__(self):
        self.heap = list()

    def add(self, elem: list):
        index = len(self.heap)
        self.heap.append(elem)
        self.sift_up(index)

    def sift_up(self, index):
        if index == 0:
            return
        prev = (index - 1) // 2
        if self.heap[prev][0] / self.heap[prev][1] < self.heap[index][0] / self.heap[index][1]:
            self.heap[prev], self.heap[index] = self.heap[index], self.heap[prev]
            self.sift_up(prev)

    def get_max(self):
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def pop(self):
        max_val = self.get_max()
        self.heap[0] = self.heap[self.size() - 1]
        self.heap.pop()
        self.sift_down(0)
        return max_val

    def sift_down(self, index):
        if index * 2 + 1 >= self.size():
            return
        left, right = index * 2 + 1, index * 2 + 2
        max_child = left
        if right < self.size() and self.heap[right][0] / self.heap[right][1] > self.heap[left][0] / self.heap[left][1]:
            max_child = right
        if self.heap[max_child][0] / self.heap[max_child][1] <= self.heap[index][0] / self.heap[index][1]:
            return
        self.heap[index], self.heap[max_child] = self.heap[max_child], self.heap[index]
        self.sift_down(max_child)


amount, bag = map(int, input().split())
cakes = Heap()
for _ in range(amount):
    price, weight = map(int, input().split())
    cakes.add([price, weight])

final_price = 0
while bag != 0 and cakes.heap:
    price, weight = cakes.get_max()
    if bag - weight >= 0:
        bag -= weight
        final_price += price
    else:
        final_price += price * bag / weight
        bag = 0
    cakes.pop()
print('%.2f' % final_price)
