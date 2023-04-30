'''
5.2. Очередь с приоритетом

Ограничение времени: 2.5 секунды
Ограничение памяти: 6.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt
В некотором изолированном от остального мира обществе X есть много разных профессий. Причем каждая профессия характеризуется своим уникальным параметром 
"важности для общества". Каждый работающий человек этого общества имеет свой уникальный рабочий номер и может вставать в очередь в Общественный Фонд Поддержки (ОФП) 
для получения компенсации расходов. Однако ОФП работает на благо общества, поэтому обслуживает сначала людей, которые имеют профессию с бо́льшим параметром "важности".
Но вскоре среди людей с более низким параметром "важности" начались забастовки, и чтобы их успокоить, правительство этого общества решило в некоторые дни выдавать 
компенсации людям профессий конкретного параметра "важности".
Реализуйте структуру данных, которая поможет выдавать компенсации людям в очереди!
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести 
одну строчку. Возможные команды для программы:
1. push i k добавить в очередь человека с номером i, имеющего профессию с параметром "важности" k и вывести «ok».
2. pop top удалить из очереди первого человека с наибольшим параметром "важности" и вывести его номер, если очередь пуста, вывести "-1".
3. pop k удалить из очереди первого человека с параметром "важности" k и вывести его номер, если такого нет, вывести "-1".
4. size вывести размер очереди.
5. popall k удалить из очереди всех людей с параметром "важности" k и вывести все номера этих людей через пробел в том порядке, в котором они находились в очереди, 
если таких людей нет, вывести "-1".
6. clear очистить очередь и вывести «ok».
7. exit вывести «bye» и завершить работу.

Описание входных данных
В каждой строке вводятся команды управления очередью. Максимальное кол-во команд не превышает 10 ** 5.
Максимальный рабочий номер человека не превышает 10 ** 7 - 1.
Максимальное значение параметра "важности для общества" не превышает 10 ** 7 - 1.

Описание выходных данных
Для каждой команды к очереди необходимо вывести в новой строке ответное сообщение по правилам, описанным выше.

Формат ввода
push 1 4
push 2 3
push 3 1
push 4 2
pop top
pop top
pop top
pop top
push 1 1
push 2 1
push 3 1
popall 1
size
pop top
push 1 999
push 2 1
size
pop 1
exit

Формат вывода
ok
ok
ok
ok
1
2
4
3
ok
ok
ok
1 2 3
0
-1
ok
ok
2
2
bye
'''

class Queue:
    def __init__(self):
        self.queue = {}

    def push(self, number, importance):
        if importance not in self.queue.keys():
            self.queue[importance] = [number]
        else:
            self.queue[importance].append(number)
        return 'ok'

    def pop_top(self):
        if not self.queue:
            return '-1'
        else:
            self.queue = dict(sorted(self.queue.items(), reverse=True))
            result = self.queue[list(self.queue.keys())[0]].pop(0)
            if not self.queue[list(self.queue.keys())[0]]:
                del self.queue[list(self.queue.keys())[0]]
            return result

    def pop_k(self, importance):
        if importance not in self.queue.keys():
            return '-1'
        else:
            result = self.queue[importance].pop(0)
            if not self.queue[importance]:
                del self.queue[importance]
            return result

    def size(self):
        size = 0
        for key, value in self.queue.items():
            size += len(value)
        return str(size)

    def popall(self, importance):
        if importance not in self.queue.keys():
            return '-1'
        else:
            answer = ' '.join(self.queue[importance])
            del self.queue[importance]
            return answer

    def clear(self):
        self.queue.clear()
        return 'ok'

    def exit(self):
        return 'bye'


command, queue, res = '', Queue(), ''
while command != 'exit':
    command = input()
    if 'push' in command:
        res += queue.push(command.split()[1], int(command.split()[2])) + '\n'
    elif 'pop top' in command:
        res += queue.pop_top() + '\n'
    elif 'popall' in command:
        res += queue.popall(int(command.split()[1])) + '\n'
    elif 'pop' in command:
        res += queue.pop_k(int(command.split()[1])) + '\n'
    elif 'size' in command:
        res += queue.size() + '\n'
    elif 'clear' in command:
        res += queue.clear() + '\n'
res += queue.exit()
print(res)
