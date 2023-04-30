'''
4.2. Обратная польская запись

Ограничение времени: 0.5 секунд
Ограничение памяти: 15.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

В обратной польской записи (или постфиксной записи) операция идёт после двух операндов. Например, сумма A + B в обратной польской записи записывается как
AB+, выражение (A - B) * C записывается как AB-C*, а A + (B + C) * D записывается как ABC+D*+ и т. д.
Вам необходимо реализовать программу, находящую значение выражения, записанного в обратной польской записи.

Описание входных данных
В единственной строке записано выражение в обратной польской записи со следующими операциями:
+ - операция сложения
- - операция вычитания
* - операция умножения
/ - операция целочисленного деления
% - операция остатка от деления
Обратите внимание, что выражение AB/ является операцией целочисленного деления A на B, т. е. эквивалентно следующему привычному нам A/B
Гарантируется, что все числа неотрицательные и не больше 10 ** 6
Гарантируется, что кол-во операций не больше 10 ** 5

Описание выходных данных
Необходимо вывести значение выражения.

Формат ввода
4 2 + 9 *

Формат вывода
54
'''

from collections import deque

fake_list = input().split()
stack = deque()
f_num, s_num = 0, 0
for counter in range(len(fake_list)):
    if fake_list[counter] not in '+-*/%':
        stack.append(fake_list[counter])
    else:
        if fake_list[counter] == '+':
            s_num, f_num = int(stack.pop()), int(stack.pop())
            stack.append(f_num + s_num)
        elif fake_list[counter] == '-':
            s_num, f_num = int(stack.pop()), int(stack.pop())
            stack.append(f_num - s_num)
        elif fake_list[counter] == '*':
            s_num, f_num = int(stack.pop()), int(stack.pop())
            stack.append(f_num * s_num)
        elif fake_list[counter] == '/':
            s_num, f_num = int(stack.pop()), int(stack.pop())
            stack.append(f_num // s_num)
        elif fake_list[counter] == '%':
            s_num, f_num = int(stack.pop()), int(stack.pop())
            stack.append(f_num % s_num)
print(*stack)
