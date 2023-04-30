def main():
    string, flag = input(), True
    len_s, result = len(string), f'1 {string}'
    for len_part in range(2, len_s + 1):
        if len_s % len_part == 0:
            sub_s_len = len_s // len_part
            sub_s = [hash(string[start: start + sub_s_len]) for start in range(0, len_s, sub_s_len)]
            for index in range(1, len_part):
                if sub_s[index] != sub_s[0]:
                    flag = False
                    break
            if flag:
                result = f'{len_s // len(string[:sub_s_len])} {string[:sub_s_len]}'
    print(result)


main()
