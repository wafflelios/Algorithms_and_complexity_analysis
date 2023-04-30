class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        return self.queue.pop(0)

    def sort(self):
        self.queue = sorted(self.queue, key=lambda x: x.weight)

    def size(self):
        return len(self.queue)


class Node:
    def __init__(self, char, weight, one, zero):
        self.char, self.weight, self.one, self.zero = char, weight, one, zero


def post_order(node, length):
    global RES
    if node.zero is None and node.one is None:
        RES += length * freq[node.char]
        return
    if node:
        length += 1
        post_order(node.zero, length)
        post_order(node.one, length)


string = input()
freq = {}
for letter in string:
    if letter not in freq.keys():
        freq[letter] = string.count(letter)
if len(freq) == 1:
    print(1)
else:
    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1]))

    queue = Queue()
    for letter, frequency in sorted_freq.items():
        queue.push(Node(letter, frequency, None, None))

    while queue.size() > 1:
        node_1 = queue.pop()
        node_0 = queue.pop()
        new_node = Node(node_1.char + node_0.char, node_1.weight + node_0.weight, node_1, node_0)
        queue.push(new_node)
        queue.sort()

    counter = 0
    RES = 0
    post_order(queue.pop(), counter)
    print(RES)