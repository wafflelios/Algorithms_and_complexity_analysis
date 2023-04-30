class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)
        return 'ok'

    def pop(self):
        if not self.queue:
            return None
        else:
            return self.queue.pop(0)

    def front(self):
        if not self.queue:
            return None
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)

    def view(self):
        return ', '.join(self.queue)

    def clear(self):
        self.queue.clear()
        return 'ok'

    def exit(self):
        return 'bye'


command, queue, res = '', Queue(), ''
while command != 'exit':
    command = input()
    if 'push' in command:
        res += queue.push(command.split()[1]) + '\n'
    elif 'pop' in command:
        res += queue.pop() + '\n'
    elif 'front' in command:
        res += queue.front() + '\n'
    elif 'size' in command:
        res += str(queue.size()) + '\n'
    elif 'view' in command:
        res += queue.view() + '\n'
    elif 'clear' in command:
        res += queue.clear() + '\n'
res += queue.exit()
print(res)
