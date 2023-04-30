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
