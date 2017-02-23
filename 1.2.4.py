
a = 10

while a <= 99:
    c = [a // 10, a % 10]
    count = c[0] + c[1]
    d = [0, 0, 0]
    sums = [0, 0, 0, 0, 0, 0, 0, 0]

    i = 2

    while i < 10:
        d[2] = c[1] * i
        d[1] = c[0] * i
        if d[2] > 9:
            d[1] += d[2]//10
            d[2] %= 10
        if d[1] > 9:
            d[0] += d[1]//10
            d[1] %= 10
        sums[i-2] = d[0] + d[1] + d[2]
        i += 1

    i = 2

    while i < 10:
        if sums[i-2] == count:
            print(a, 'multiply on', i, 'sum is', count)
        i += 1

    a += 1

input ()

