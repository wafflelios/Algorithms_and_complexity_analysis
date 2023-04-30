class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next, self.prev = None, None

    def __init__(self):
        self.start = self.end = self.center = self.Node(None)
        self.length = 0

    def check_if_empty(self, node):
        if self.start.value is None:
            self.start = self.end = self.center = node
            return True
        return False

    def add_to_start(self, value):
        self.length += 1
        new_node = self.Node(value)
        if self.check_if_empty(new_node):
            return
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node
        if self.length % 2 == 0:
            self.center = self.center.prev

    def insert(self, node, value):
        new_node = self.Node(value)
        next_node = node.next
        if next_node is None:
            new_node.next = None
            node.next = new_node
            new_node.prev = node
            self.end = new_node
            return
        next_node.prev = new_node
        new_node.next = next_node
        node.next = new_node
        new_node.prev = node
        self.length += 1
        if self.length % 2 == 1:
            self.center = self.center.next

    def add_to_the_end(self, value):
        self.length += 1
        new_node = self.Node(value)
        if self.check_if_empty(new_node):
            return
        self.insert(self.end, value)
        if self.length % 2 == 1:
            self.center = self.center.next

    def front_pop(self):
        result = self.start
        self.start = self.start.next
        return result.value


dragon_queue = DoubleLinkedList()
res = ''
for _ in range(int(input())):
    in_put = input()
    if '+' in in_put:
        dragon_queue.add_to_the_end(in_put.split()[1])
    elif '*' in in_put:
        dragon_queue.insert(dragon_queue.center, in_put.split()[1])
    elif '!' in in_put:
        dragon_queue.add_to_start(in_put.split()[1])
    else:
        res += str(dragon_queue.front_pop()) + '\n'
print(res)
