'''
4.3. Мудрый дедушка

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Маленький Миша изучил алфавит и пошёл похвастаться своему мудрому дедушке. Дедушка, конечно, обрадовался достижению своего внука и предложил ему потренироваться 
с буквами, дав такую задачу:
«Я дам тебе строку s и вес для каждой буквы нашего алфавита w_i. Тебе необходимо получить такую строку, у которой максимальный вес. Но есть ограничения. 
Получить это строку максимального веса ты должен путём многократного обмена двух любых букв строки s. Как же вычислить вес строки, ты хочешь меня спросить? 
Всё очень просто: для каждой буквы из алфавита посчитай максимальное расстояние между позициями в строке и умножь на её вес. 
Напиши на листочке строку максимально возможного веса, а я дам тебе конфетку!».
От такого сложного условия у Миши разболелась голова, он расплакался и убежал. Мудрый дедушка не знал, что Миша еще не знает умножения. 
Теперь эту задачку придётся решать вам!

Описание входных данных:
Дана строка, состоящая из строчных букв кириллицы (1 <= |s| <= 5 * 10 ** 5). Следующая строка ввода содержит 32 чисел - веса букв кириллицы от 'a' до 'я',
веса неотрицательные и не превосходят 2 ** 31 - 1

Описание выходных данных:
Выведите строку s, в которой переставлены буквы так, чтобы полученный вес был максимально возможным. Если искомых вариантов несколько, 
буквы в строке с одинаковым весом должны идти в алфавитном порядке. После строки через пробел выведите её вес.

Формат ввода
примерчик
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32

Формат вывода
риекмпчир 190

Примечания
Гарантируется, что буквы ё нет в тестах.
'''

alphabet = { 'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0,
             'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0,
             'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}

word = list(input())
weight = input().split()
res, final_weight, len_str = '', 0, len(word)

index = 0
for key in alphabet.keys():
    alphabet[key] = weight[index]
    index += 1

num_amount = {}
for symbol in word:
    if symbol in num_amount.keys():
        num_amount[symbol] += 1
    else:
        num_amount[symbol] = 1

counter = 0
sorted_by_weight = dict(sorted(alphabet.items(), key=lambda item: int(item[1]), reverse=True))
for key in sorted_by_weight.keys():
    if sorted_by_weight[key] != '0' and key in num_amount.keys() and num_amount[key] > 1:
        res += key
        word.remove(key)
        word.remove(key)
        final_weight += int(alphabet[key]) * (len_str - 1 - counter)
        counter += 2
print(f'{res}{"".join(sorted(word))}{res[::-1]} {final_weight}')
