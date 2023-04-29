def main():
    legs_groups, arms_groups, amount = input().split()
    amount = int(amount)
    legs_arr, arms_arr, answer = [], [], []
    for __ in range(int(legs_groups)):
        legs_arr.append(list(map(int, input().split())))
    for __ in range(int(arms_groups)):
        arms_arr.append(list(map(int, input().split())))
    requests_amount = int(input())
    for __ in range(requests_amount):
        leg_index, arm_index = map(int, input().split())
        start, end, val_minim, middle = 0, amount - 1, 9999999, 0
        while end - start > 1:
            middle = (end - start) // 2 + start
            if legs_arr[leg_index][middle] <= arms_arr[arm_index][middle]:
                start = middle
            elif legs_arr[leg_index][middle] > arms_arr[arm_index][middle]:
                end = middle
            if val_minim >= max(legs_arr[leg_index][middle], arms_arr[arm_index][middle]):
                val_minim = max(legs_arr[leg_index][middle], arms_arr[arm_index][middle])
        if end - start == 1:
            if int(max(legs_arr[leg_index][end], arms_arr[arm_index][end])) <= \
                    int(max(legs_arr[leg_index][start], arms_arr[arm_index][start])):
                start = end
                for counter in range(end + 1, amount):
                    if legs_arr[leg_index][counter] == legs_arr[leg_index][end]:
                        start += 1
                    else:
                        break
            answer.append(start)
        elif int(max(legs_arr[leg_index][0], arms_arr[arm_index][0])) == \
                int(max(legs_arr[leg_index][amount - 1], arms_arr[arm_index][amount - 1])):
            answer.append(amount - 1)
    print(*answer, sep='\n')


main()
