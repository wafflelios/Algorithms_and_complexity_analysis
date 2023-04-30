amount, bag = map(int, input().split())
cakes = []
temp_bag = bag
for _ in range(amount):
    price, weight = map(int, input().split())
    cakes.append([price, weight])

sorted_cakes = sorted(cakes, key=lambda x: x[0] / x[1], reverse=True)

final_price = 0
for price, weight in sorted_cakes:
    if bag == 0:
        break
    elif bag - weight >= 0:
        bag -= weight
        final_price += price
    else:
        final_price += price * bag / weight
        bag = 0

print('%.2f' % final_price)
