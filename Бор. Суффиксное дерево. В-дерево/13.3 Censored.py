'''
13.3. Censored

Ограничение времени: 2 секунды
Ограничение памяти: 64.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вы живёте в одном царстве-государстве. Вы работаете цензором в КПОХП (Комиссии по проверке и оценке художественных произведений для печати и издания) имени Волгина. Вы отвечаете за проверку художественных произведений на соответствие идеологии и политической линии правительства, а также на соответствие морально-этическим нормам и ценностям, утверждаемым государством. Вы должны оценить содержание произведения и определить, является ли оно политически корректным, соответствует ли оно "общественной пользе" и не содержит ли оно "антиобщественных" или "противозаконных" элементов. Каждый день вам сверху "падает" некий список слов и чисел, запрещенных в вашем царстве-государстве. И каждый день авторы со всего вашего царства-государства отправляют вам на проверку свои произведения. Определите, содержит ли их произведение запрещенные слова и числа. Если содержит, то укажите строку и позицию, с которого начинается первое попавшееся запрещенное слово или число (Это поможет сотрудникам ГКБ при составлении протокола). А если не содержит, то напишите: "Одобрено".

Описание входных данных
Первая строка содержит число n (1 <= n <= 50000) − количество запрещённых слов и чисел. Следующие n строк содержат запрещенные слова и числа. Длина каждого слова или числа не превышает 10000 символов. После запрещенных слов и чисел идет число m (1 <= m <= 10000) − количество строк в тексте. 
Длина строк не превышает 5 * 10 ** 5 символов.

Описание выходных данных
В единственной строке выходных данных выведите через пробел номер строки и номер позиции запрещенного слова или числа. Если такого слова нет, то выведите "Одобрено".

Формат ввода
2
Fork
Light
5
Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.
Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.

Формат вывода
3 37

Проходит все тесты яндекс контеста, но не проходит пользовательский:
2
aabc
abd
1
aabd

возможно стоит рассматривать "подстрочно", все сводится к алгоритму укконена, но пока не получилось реализовать нормальный алгоритм поиска слов с их начальной позицией.
'''
class Node:
    def __init__(self):
        self.children, self.is_end = {}, False


class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.insert(word)

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                new_node = Node()
                current_node.children[char] = new_node
                current_node = new_node
        current_node.is_end = True

    def find_word(self, words):
        word_position = 0
        for word in words:
            current_node = self.root
            char_counter = 0
            for char in word:
                if char in current_node.children.keys():
                    current_node = current_node.children[char]
                    char_counter += 1
                    if current_node.is_end:
                        return word_position + 1
                else:
                    current_node = self.root
                    word_position += char_counter + 1
                    char_counter = 0
            word_position += char_counter + 1
        return None

def main():
    words_amount = int(input())
    words = []
    for _ in range(words_amount):
        words.append(input().lower())
    trie = Trie(words)
    strings_amount = int(input())
    strings = []
    for _ in range(strings_amount):
        strings.append(input().lower())
    for index in range(strings_amount):
        position = trie.find_word(list(strings[index].split()))
        if position:
            print(index + 1, position)
            break
    else:
        print('Одобрено')


main()
