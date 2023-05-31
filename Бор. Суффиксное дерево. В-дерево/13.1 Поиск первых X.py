'''
13.1. Поиск первых X

Ограничение времени: 6 секунд
Ограничение памяти: 512.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Реализуйте структуру данных Бор (Trie). Напишите программу, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:
add s Добавить строку в структуру s (значение s задается после команды). Программа должна вывести «ok».
get s x Программа должна вывести первые x по алфавиту строки добавленные в структуру. Они должны начитнаться на s и быть длинне чем s (Например 'abcde' начинается на 'abcd' и длинее, слодовательно для поиска по 'abcd', следует в том числе выдовать результат 'abcde', при соблюдении остальных условий)
exit Программа должна вывести «bye» и завершить работу.

Описание входных данных
Вводятся команды управления структурой, по одной на строке.

Описание выходных данных
Требуется вывести протокол работы со структурой, по одному сообщению на строке.

Формат ввода
add abcde
add abrtyur
add abc
get ab 2
exit

Формат вывода
ok
ok
ok
abc abcde
bye

Примечания
Если при ответе на get запрос поиск не даёт ни одного результата, то выводите 'empty'.
Если при ответе на get запрос поиск возвращает несколько результатов, и, в алфавитном порядке, одно слово является началом другого, то первым выводить более короткое. (Например "abc", "abcd" выводятся в таком порядке)

https://albertauyeung.github.io/2020/06/15/python-trie.html/
'''

class Node:
    def __init__(self, char):
        # ключ - символ, значение - вершина(нод)
        self.char, self.is_end, self.children = char, False, {}

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
        return 'ok'

    def dfs(self, node, prefix, length):
        if node.is_end and len(prefix + node.char) > length:
            self.output.append(prefix + node.char)

        for child in node.children.values():
            self.dfs(child, prefix + node.char, length)

    def prefix_search(self, prefix, amount):
        self.output, or_len = [], len(prefix)
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 'empty'
        self.dfs(current_node, prefix[:-1], or_len)
        if not self.output:
            return 'empty'
        elif len(self.output) < amount:
            return ' '.join(sorted(self.output))
        else:
            return ' '.join(sorted(self.output)[:amount])


trie = Trie()
in_put = ''
while in_put != 'exit':
    in_put = input()
    if in_put[:3] == 'add':
        word = in_put[4:]
        print(trie.insert(word))
    elif in_put[:3] == 'get':
        command, prefix, amount = in_put.split()
        result = trie.prefix_search(prefix, int(amount))
        print(trie.prefix_search(prefix, int(amount)))
print('bye')
