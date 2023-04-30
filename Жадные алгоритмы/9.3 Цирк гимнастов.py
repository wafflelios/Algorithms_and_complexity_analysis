class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self, num=0):
        return self.queue.pop(num)

    def sort(self):
        self.queue = sorted(self.queue, key=lambda x: x[1], reverse=True)

    def get_person_with_most_body_w(self):
        res_person, res_index = [0, 0], 0
        for num in range(len(self.queue)):
            if self.queue[num][1] > res_person[1]:
                res_person = self.queue[num]
                res_index = num
        return res_person, res_index


amount = int(input())
people = []
for _ in range(amount):
    person = input().split(';')
    hold_w, body_w = int(person[1]), int(person[2])
    people.append([hold_w, body_w])

sorted_people = sorted(people, key=lambda x: x[0] + x[1])
sum_w, counter = 0, 0
queue = Queue()
for hold_w, body_w in sorted_people:
    if hold_w >= sum_w:
        counter += 1
        sum_w += body_w
        queue.push([hold_w, body_w])
    else:
        person, index = queue.get_person_with_most_body_w()
        if person[1] > body_w:
            sum_w -= person[1]
            queue.pop(index)
            queue.push([hold_w, body_w])
            sum_w += body_w
    queue.sort()

print(counter)
