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