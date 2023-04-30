def main():
    amount = int(input())
    temp_diff = []
    for _ in range(amount):
        min_t, max_t = map(int, input().split())
        temp_diff.append([min_t, max_t])
    temp_diff = tuple(temp_diff)
    bacteria = tuple(map(int, input().split()))
    for bact in bacteria:
        counter = 0
        for min_t, max_t in temp_diff:
            if max_t >= bact >= min_t:
                counter += 1
        print(counter)


main()
