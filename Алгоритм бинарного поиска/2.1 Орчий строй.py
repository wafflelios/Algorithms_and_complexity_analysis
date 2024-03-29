'''
2.1. Орчий строй

Ограничение времени: 0.5 секунд
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

В строю отважной армии Сарумана друг за другом стоят n орков, рост i-го из них равен a_i условных единиц. 
Новобранец-орк Гримморхус тоже собирается встать в этот строй,
причём Саруману хочется поставить Гримморхуса на такую позицию p, чтобы f(p) =
[количество орков левее Гримморхуса того же роста, что и Гримморхус]
умножить на
[количество орков правее Гримморхуса с ростом, не равным росту Гримморхуса]
было максимально.
Для этого Гримморхус может встать в начало строя, в её конец, или между любыми двумя соседними орками.
К сожалению ни Гримморхус, ни Саруман не могут точно вспомнить рост Гримморхуса, у них есть только m предположений о том, каким он может быть, 
и для каждого из них они хотели бы знать оптимальную позицию, на которую Гримморхусу стоило бы встать.

Описание входных данных
В первой строке даны n целых чисел a_i - рост орков, стоящих в строю (1 <= n, a_i <= 10 ** 5).
Во второй строке даны m целых чисел x_i - предпологаемый рост Гримморхуса (1 <= m, x_i <= 10 ** 5)

Описание выходных данных
В единственной строке выведите m целых чисел - значение f(p) в оптимальной для данного роста позиции.

Формат ввода
1 1 2 2 2 2 1 1 1
1 2 1

Формат вывода
8 12 8
'''

def main():
    orc_growth = input().split()
    supposed_growth = input().split()
    dictionary = {}
    for counter in range(0, len(orc_growth) - 1):
        if orc_growth[counter] != orc_growth[counter + 1]:
            counter_L = orc_growth[:counter + 1].count(orc_growth[counter])
            counter_R = len(orc_growth[counter:]) - orc_growth[counter:].count(orc_growth[counter])
            multy = counter_L * counter_R
            if (orc_growth[counter] not in dictionary.keys()) or (dictionary[orc_growth[counter]] < multy):
                dictionary[orc_growth[counter]] = multy
    for grow in supposed_growth:
        if grow not in dictionary.keys():
            print(0, end=' ')
        else:
            print(dictionary[grow], end=' ')


main()
