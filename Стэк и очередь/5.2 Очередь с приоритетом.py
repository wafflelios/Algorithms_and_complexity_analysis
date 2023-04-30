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