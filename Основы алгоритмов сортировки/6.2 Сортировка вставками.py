balls = list(map(int, input().split()))

for index in range(1, len(balls)):
    current = balls[index]
    sub_index = index - 1
    while sub_index >= 0 and balls[sub_index] > current:
        balls[sub_index + 1] = balls[sub_index]
        sub_index -= 1
    balls[sub_index + 1] = current
    if index == (len(balls) - 1) // 2:
        print(*balls)

print(*balls)
