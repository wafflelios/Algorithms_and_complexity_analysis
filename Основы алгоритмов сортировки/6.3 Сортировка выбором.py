score = list(map(int, input().split()))

for counter in range(len(score) - 1):
    minimum = min(score[counter:])
    score[score.index(minimum, counter)], score[counter] = score[counter], score[score.index(minimum, counter)]
    if counter == len(score) // 2 - 1:
        print(*score)

print(*score)
