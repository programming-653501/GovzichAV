import random


def check(ans):
    if ans == 'n':
        print('Bye!')
    elif ans != 'y':
        print('Incorrect input, try again')
        ans = check((input()))
    return ans


def HorizontalLine(n, m, f):
    k = 0
    j = n[0] - 1
    while j >= 0:
        if f[m[0]][j] == 2:
            print('Check by queen on position', 'x=', j, 'y=', m[0])
            k += 1
            break
        j -= 1
    j = n[0] + 1
    while j <= 7:
        if f[m[0]][j] == 2:
            print('Check by queen on position', 'x=', j, 'y=', m[0])
            k += 1
            break
        j += 1
    return k


def Diagonals(n, m, f):
    k = 0
    i = m[0] + 1
    j = n[0] + 1
    while i <= 7 and j <= 7:
        if f[i][j] == 2:
            print('Check by queen on position', 'x=', j, 'y=', i)
            k += 1
            break
        j += 1
        i += 1
    i = m[0] - 1
    j = n[0] - 1
    while i >= 0 and j >= 0:
        if f[i][j] == 2:
            print('Check by queen on position', 'x=', j, 'y=', i)
            k += 1
            break
        j -= 1
        i -= 1
    i = m[0] - 1
    j = n[0] + 1
    while i >= 0 and j <= 7:
        if f[i][j] == 2:
            print('Check by queen on position', 'x=', j, 'y=', i)
            k += 1
            break
        j += 1
        i -= 1
    i = m[0] + 1
    j = n[0] - 1
    while i <= 7 and j >= 0:
        if f[i][j] == 2:
            print('Check by queen on position', 'x=', j, 'y=', i)
            k += 1
            break
        j -= 1
        i += 1
    return k


def VerticalLine(n, m, f):
    k = 0
    i = m[0] - 1
    while i >= 0:
        if f[i][n[0]] == 2:
            print('Check by queen on position', 'x=', n[0], 'y=', i)
            k += 1
            break
        i -= 1
    i = m[0] + 1
    while i <= 7:
        if f[i][n[0]] == 2:
            print('Check by queen on position', 'x=', n[0], 'y=', i)
            k += 1
            break
        i += 1
    return k

a = 0
ans = 'y'
while ans == 'y':
    while True:
        try:
            a = int(input('How much queens on board?'))
            while a > 63:
                a = int(input('Incorrect input. Try again'))
        except ValueError:
            print('Incorrect input. Try again')
        else:
            break

    if a < 32:
        f = [[0] * 8]
        for i in range(8):
            f.append([0] * 8)

        i = 0
        while i < a:
            m = random.sample(range(0, 8), 1)
            n = random.sample(range(0, 8), 1)
            if f[m[0]][n[0]] == 0:
                f[m[0]][n[0]] = 2
                i += 1

        i = 0
        while i != 1:
            m = random.sample(range(0, 8), 1)
            n = random.sample(range(0, 8), 1)
            if f[m[0]][n[0]] == 0:
                f[m[0]][n[0]] = 1
                i += 1
    else:
        f = [[2] * 8]
        for i in range(8):
            f.append([2] * 8)

        i = 0
        while i < 64 - a:
            m = random.sample(range(0, 8), 1)
            n = random.sample(range(0, 8), 1)
            if f[m[0]][n[0]] == 2:
                f[m[0]][n[0]] = 0
                i += 1

        i = 0
        while i != 1:
            m = random.sample(range(0, 8), 1)
            n = random.sample(range(0, 8), 1)
            if f[m[0]][n[0]] == 0:
                f[m[0]][n[0]] = 1
                i += 1

    for i in range(8):
        print(f[i])

    c = VerticalLine(n, m, f) + HorizontalLine(n, m, f) + Diagonals(n, m, f)
    if c == 0:
        print('Safe position')

    print('Would you like to continue?(y/n)')
    ans = check(input())
