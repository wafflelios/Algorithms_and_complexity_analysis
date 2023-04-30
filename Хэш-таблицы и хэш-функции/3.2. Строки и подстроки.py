'''
3.2. Строки и подстроки

Ограничение времени: 1.5 секунд
Ограничение памяти: 256.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Дана непустая строка s. Нужно найти такое наибольшее число k и строку t, что s совпадает со строкой t, выписанной k раз подряд.

Описание входных данных
Одна строка длины N, (1 <= N <= 6 * 10 ** 5), состоящая только из маленьких латинских букв.

Описание выходных данных
Вывести k и строку t.

Формат ввода
abcabcabc

Формат вывода
3 abc
'''

'''
РЕШЕНИЕ С ИСПОЛЬЗОВАНИЕМ ХЭШЕЙ
'''
def main():
    string, flag = input(), True
    len_s, result = len(string), f'1 {string}'
    for len_part in range(2, len_s + 1):
        if len_s % len_part == 0:
            sub_s_len = len_s // len_part
            sub_s = [hash(string[start: start + sub_s_len]) for start in range(0, len_s, sub_s_len)]
            if all(sub_s[index] == sub_s[0] for index in range(1, len_part)):
                result = f'{len_s // len(string[:sub_s_len])} {string[:sub_s_len]}'
    print(result)


main()

'''
РЕШЕНИЕ БЕЗ ИСПОЛЬЗОВАНИЯ ХЭШЕЙ
'''
string, sub_str = input(), ''
for symbol in string:
    sub_str += symbol
    if len(string) % len(sub_str) == 0 and sub_str * (len(string) // len(sub_str)) == string:
        print(f'{len(string) // len(sub_str)} {sub_str}')
        break
