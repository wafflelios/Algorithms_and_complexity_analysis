amount, colours = map(int, input().split())
tiles = list(input().split())
res = []

for index in range(amount // 2 + 1):
    diff, counter = False, 0
    for tile_1 in range(index, amount):
        tile_2 = index - counter - 1
        counter += 1
        if tile_2 < 0:
            break
        elif tiles[tile_1] != tiles[tile_2]:
            diff = True
            break
    if not diff:
        res.append(amount - index)
print(*res)