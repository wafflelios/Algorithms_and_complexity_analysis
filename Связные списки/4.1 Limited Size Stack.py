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
