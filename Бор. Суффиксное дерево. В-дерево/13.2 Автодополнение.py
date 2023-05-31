'''
13.2. Автодополнение

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Вам необходимо реализовать автодополнение при помощи бора.
В начале вам будут даны слова для начального заполнения бора.
Правила автодополнения слов: для строки s необходимо найти среди всех слов в боре, начинающихся на строку s такое, чтобы его количество повторений в боре было максимальным. Если таких слов несколько, необходимо вывести вывести слово наименьшей длины. 
Если и таких несколько, то необходимо вывести слово, идущее раньше всех в лексикографическом порядке. Если в боре слова, начинающегося со строки 
s, не существует, вывести "None".

Программа должна уметь отвечать на следующие команды:
+ s − добавить слово s в бор и вывести "ok".
? s − вывести лучшее автодополнение для строки s.
exit − программа должна вывести "bye" и завершить свою работу.

Описание входных данных
В первой строке на вход программы подаются слова для первоначального заполнения бора. Слова разделены пробелом.
В последующих строках находятся команды для обращения к бору, каждая команда в отдельной строке.
Все слова состоят из букв кириллицы, гарантируется, что в словах не содержится буквы "ё".

Описание выходных данных
Требуется вывести протокол работы с бором, по одному сообщению на строке.

Формат ввода
студент студенческий студсовет стул стоянка студсовет
? с
? сто
+ стул
+ стул
? с
? универ
exit

Формат вывода
студсовет
стоянка
ok
ok
стул
None
bye

https://albertauyeung.github.io/2020/06/15/python-trie.html/
'''

class Node:
    def __init__(self, char):
        # ключ - символ, значение - вершина(нод)
        self.char, self.is_end, self.children, self.counter = char, False, {}, 0


class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                new_node = Node(char)
                current_node.children[char] = new_node
                current_node = new_node
        current_node.is_end = True
        current_node.counter += 1
        return 'ok'

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def prefix_search(self, prefix):
        self.output = []
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 'None'
        self.dfs(current_node, prefix[:-1])
        if not self.output:
            return 'None'
        else:
            sorted_output = sorted(self.output, key=lambda x: x[1], reverse=True)
            max_counter = sorted_output[0][1]
            result = '�' * 999
            for output in sorted_output:
                if output[1] == max_counter and (len(output[0]) < len(result) or (len(output[0]) == len(result)
                                                                                  and output[0] < result)):
                    result = output[0]
            return result


trie = Trie()
words = input().split()
for word in words:
    trie.insert(word)
in_put = ''
while in_put != 'exit':
    in_put = input()
    if in_put[0] == '+':
        print(trie.insert(in_put[2:]))
    elif in_put[0] == '?':
        print(trie.prefix_search(in_put[2:]))
print('bye')
