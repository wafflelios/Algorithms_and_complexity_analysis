'''
9.3. Цирк гимнастов

Ограничение времени: 0.7 секунд
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Владелец цирка гимнастов Сергей Павлович в целях привлечения большого количества публики собирается представить никому не виданный ранее трюк: 
построить из всех своих гимнастов максимально высокую башню! Башня строится таким образом: один гимнаст стоит на полу, ему на плечи взбирается второй гимнаст, 
второму гимнасту взбирается на плечи третий гимнаст и так далее.
Сергей Павлович знает каждого гимнаста: его имя, вес и какой вес он может удержать (некоторые гимнасты в его цирке пришли из цирка силачей). 
Ростом все гимнасты примерно одинаковые. Всего в труппе N артистов, Сергей Павлович хочет знать, из скольких из них получится сделать максимально высокую башню, 
ведь если хоть один из гимнастов не выдержит веса сверху, то вся башня рухнет!

Формат входных данных
В первой строке данных представлено целое число N (1 <= N <= 10 ** 4) - общее кол-во гимнастов.
В следующих N строках представлены следующие данные о гимнасте, разделенные точкой с запятой: имя; вес 1 <= m <= 10 ** 4, который гимнаст может удержать;
вес гимнаста 1 <= w <= 10 ** 4.

Формат выходных данных
В единственной строке выведите целое число M - максимальное количество гимнастов в башне.

Формат ввода
10
Mikhail Semyonovich;60;62
Sergei Pavlovich;170;60
Andrei Sergeevich;80;80
Mikhail Pavlovich;40;65
Nikolai Petrovich;55;50
Ivan Ivanovich;30;70
Alexandr Romanovich;45;62
Matvei Nikolaevich;60;40
Roman Danilovich;70;72
Kornei Sidorovich;92;80

Формат вывода
4

Примечания
В спорной ситуации (когда два гимнаста могут поднять один и тот же вес, например) Сергей Павлович предпочитает брать на выступление гимнаста, у которого вес меньше.
'''

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
