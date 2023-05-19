'''
12.1. Куча и базовые операции

Ограничение времени: 3 секунды
Ограничение памяти: 16.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt
Реализуйте структуру данных «куча». Напишите программу, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

1. add n Добавить в кучу число n (значение n задается после команды). Программа должна вывести «ok».
2. min Взять из кучи минимальный элемент. Программа должна вывести его значение.
3. size Программа должна вывести количество элементов в куче.
4. exit Программа должна вывести «bye» и завершить работу.

Гарантируется, что набор входных команд удовлетворяет следующим требованиям: максимальное количество элементов в куче в любой момент не превосходит 100 000, все команды «min» корректны, то есть при их исполнении в очереди содержится хотя бы один элемент.

Описание входных данных
Вводятся команды управления очередью, по одной на строке.

Описание выходных данных
Требуется вывести протокол работы с очередью, по одному сообщению на строке.

Формат ввода
add 1
add 23
add -3
min
add -100
min
exit

Формат вывода
ok
ok
ok
-3
ok
-100
bye
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


heap = Heap()
in_put = ''
while in_put != 'exit':
    in_put = input()
    if 'add' in in_put:
        command, num = in_put.split()
        num = int(num)
        print(heap.add(num))
    elif 'min' in in_put:
        print(heap.get_min())
    elif 'size' in in_put:
        print(heap.size())
print('bye')
