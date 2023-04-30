def bubble_sort():
    beads = list(map(int, input().split()))
    number = int(input())
    length = len(beads)
    for index in range(length - 1):
        if index == number:
            print(*beads)
        for sub_index in range(length - index - 1):
            if beads[sub_index] > beads[sub_index + 1]:
                beads[sub_index], beads[sub_index + 1] = beads[sub_index + 1], beads[sub_index]
    print(*beads)


bubble_sort()
