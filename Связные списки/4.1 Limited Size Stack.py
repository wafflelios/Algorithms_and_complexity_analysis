'''
4.1. Limited Size Stack

Ограничение времени: 1.5 секунд
Ограничение памяти: 64.0 Мб
Ввод input.txt
Вывод output.txt

В этой задаче вам нужно реализовать стек ограниченного размера. Этот стек работает как обычный стек, однако при превышении максимального размера 
удаляет самый глубокий элемент в стеке. Таким образом в стеке всегда будет ограниченное число элементов.
Операция Push должна иметь сложность O(1), то есть никак не зависеть от размера стека.

Описание входных данных
В первой строке подаётся целое число, ограничитель размера стека.
В следующих строках указаны команды для работы со стеком:
1. push n Добавить в очередь число n (значение n задается после команды). Программа должна вывести 'ok'.
2. pop Удалить из очереди первый элемент. Программа должны вывести его значение.
3. count Программа должна вывести кол-во элементов в очереди.
4. exit Программа должна вывести 'bye' и завершить работу.

Описание выходных данных
Требуется вывести протокол работы со стеком, по одному сообщению на строке.

Формат ввода
2
push 10
push 20
push 30
push 40
pop
pop
count
exit

Формат вывода
ok
ok
ok
ok
40
30
0
bye

Примечания
Обратите внимание, что в этой задачи ввод и вывод реализован только через файлы input.txt и output.txt
'''

from collections import deque

with open('input.txt') as in_file:
    with open('output.txt', 'w') as out_file:
        lines = in_file.readlines()
        size = lines[0][:-1]
        fake_list = deque()
        in_put = [0, 0]
        for line in lines[1:]:
            in_put = line.split()
            if in_put[0] == 'push':
                if len(fake_list) >= int(size):
                    fake_list.append(in_put[1])
                    fake_list.popleft()
                else:
                    fake_list.append(in_put[1])
                out_file.write('ok\n')
            if in_put[0] == 'pop':
                out_file.write(fake_list.pop() + '\n')
            if in_put[0] == 'count':
                out_file.write(str(len(fake_list)) + '\n')
            if in_put[0] == 'exit':
                out_file.write('bye\n')
