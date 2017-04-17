
a = 10

while a <= 99:
    numbers = [a // 10, a % 10]
    count = numbers[0] + numbers[1]
    new_numbers = [0, 0, 0]
    sums = [0, 0, 0, 0, 0, 0, 0, 0]

    multiplier = 2
    while multiplier < 10:
        new_numbers[2] = numbers[1] * multiplier
        new_numbers[1] = numbers[0] * multiplier
        if new_numbers[2] > 9:
            new_numbers[1] += new_numbers[2]//10
            new_numbers[2] %= 10
        if new_numbers[1] > 9:
            new_numbers[0] += new_numbers[1]//10
            new_numbers[1] %= 10
        sums[multiplier-2] = new_numbers[0] + new_numbers[1] + new_numbers[2]
        multiplier += 1

    multiplier = 2

    while multiplier < 10:
        if sums[multiplier-2] == count:
            print(a, 'multiply on', multiplier, 'sum is', count)
        multiplier += 1

    a += 1

input()

