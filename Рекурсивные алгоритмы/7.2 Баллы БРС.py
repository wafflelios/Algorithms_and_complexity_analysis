students, minimum, maximum = map(int, input().split())
counter, current, res = 1, [], 0

def create_seq(amount, min_v, max_v):
    global current, counter, res
    if counter == 1:
        max_v += 1
    if counter == amount:
        for base in range(min_v + amount - counter, max_v):
            res += 1
            current.append(base)
            print(' '.join(str(current[val]) for val in range(amount)))
            current.pop(-1)
        counter -= 1
        return
    for base in range(min_v + amount - counter, max_v):
        current.append(base)
        counter += 1
        create_seq(amount, min_v, base)
        current.pop(-1)
    counter -= 1
    return


create_seq(students, minimum, maximum)
print(res)
