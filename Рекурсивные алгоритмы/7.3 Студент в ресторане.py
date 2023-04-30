'''
7.3. Студент в ресторане

Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб
Ввод стандартный ввод или input.txt
Вывод стандартный вывод или output.txt

Один голодный студент зашёл в один замечательный ресторан. Денег у студента - кот наплакал, а именно W денежных единиц. А кушать хочется. 
Официант предоставил студенту меню, в котором было n блюд. Под каждым i-ым блюдом красовалась цена p_i и калорийность c_i. 
Напишите программу, которая поможет студенту выбрать позиции из меню так, чтобы он получил максимально возможное число калорий за свой ограниченный бюджет.

Описание входных данных
В первой строке входных данных содержатся натурельные числа n (кол-во блюд)(1 <= n <= 20) и W (бюджет студента)(1 <= W <= 10 ** 9). Следующие n строк содержат описание
позиций в меню: цену p_i и калорийность c_i(1 <= p_i, c_i <= 10 ** 9)

Описание выходных данных
В первой строке выходных данных выпишите количество выбранных позиций меню и их суммарную калорийность. 
Во второй строке выведите через пробел номера выбранных позиций (в порядке возрастания). 
Учтите, что студент, хоть и беден, но одно и то же блюдо есть не будет(хочет разные). 
Если искомых наборов позиций несколько, ты выберите тот, в котором наибольшее число блюд. И даже если с таким условием ответов может быть несколько, 
то выберите тот набор позиций, в котором первое блюдо имеет наименьший возможный номер, второе блюдо имеет наименьший возможный номер, и так далее.

Формат ввода
5 100
100 500
50 250
50 250
50 250
50 250

Формат вывода
2 500
2 3
'''

def enumeration(res, len_menu, menu, money, dishes_num, calories, counter):
    if money == 0 or counter == len_menu:
        if res[1] < calories or res[1] == calories and len(dishes_num) > len(res[0]):
            res[0], res[1] = dishes_num, calories
        return
    if money - menu[counter][0] >= 0:
        enumeration(res, len_menu, menu, money - menu[counter][0], dishes_num + [counter + 1],
                    calories + menu[counter][1], counter + 1)
    enumeration(res, len_menu, menu, money, dishes_num, calories, counter + 1)


def main():
    dish_amount, budget = map(int, input().split())
    menu, res = [], [[], 0]

    for _ in range(dish_amount):
        price, calories = map(int, input().split())
        menu.append((price, calories))

    menu = tuple(menu)
    enumeration(res, dish_amount, menu, budget, [], 0, 0)
    print(f'{len(res[0])} {res[1]}\n{" ".join(str(dish) for dish in res[0])}')


main()
