def sort_heights(arr, start, end):
    l_point, r_point, pivot = start, end - 1, end
    if len(arr) != 1:
        print(arr[pivot])
    while l_point <= r_point:
        while arr[l_point] < arr[pivot]:
            l_point += 1
        while r_point >= start and arr[r_point] >= arr[pivot]:
            r_point -= 1
        if l_point <= r_point:
            arr[l_point], arr[r_point] = arr[r_point], arr[l_point]
    arr[l_point], arr[pivot] = arr[pivot], arr[l_point]
    if start < l_point - 1:
        sort_heights(arr, start, l_point - 1)
    if l_point + 1 < end:
        sort_heights(arr, l_point + 1, end)


heights = list(map(int, input().split()))
sort_heights(heights, 0, len(heights) - 1)
print(*heights)
