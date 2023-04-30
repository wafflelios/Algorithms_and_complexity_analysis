dictionary = {}
res = ''

lst_1 = list(input().split())
lst_2 = list(input().split())

for num in lst_2:
    dictionary.setdefault(num, 0)
    dictionary[num] += 1

for num in lst_1:
    dictionary.setdefault(num, 0)
    res += str(dictionary[num]) + ' '

print(res)
