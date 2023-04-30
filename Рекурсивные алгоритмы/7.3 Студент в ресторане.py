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