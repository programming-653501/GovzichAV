import random


def parse_int(string):
    while 1:
        try:
            string = int(string)
            while not string:
                print('Value should not be 0! Try again:')
                string = int(input())
        except ValueError:
            print('Value should be integer! Try again:')
            string = input()
        else:
            return string


def generate_queue(number):
    a = []
    queue = []
    correlation = []
    for i in range(number):
        print('Input time in service', i + 1)
        for_check = parse_int(input())
        a.append(for_check)
        row = [1] * int(random.random() * 10)
        queue.append(row)
        correlation.append(i)
    return a, queue, correlation


def search_min_queue(queue, remaining_numbers):
    min_queue = (len(queue[0]) + 1) * a[0] + residue[0]
    index_min = 0
    for i in range(remaining_numbers):
        if (len(queue[i]) + 1) * a[i] + residue[i] < min_queue:
            min_queue = (len(queue[i]) + 1)*a[i] + residue[i]
            index_min = i
    return min_queue, index_min


def changes_in_queue(queue, remaining_numbers, a, residue, min_queue):
    for i in range(remaining_numbers):
        fixed_autos = min_queue // a[i]
        if min_queue % a[i]:
            residue[i] += min_queue % a[i]
            if residue[i] > a[i]:
                fixed_autos += residue[i] // a[i]
                residue[i] -= (residue[i] // a[i]) * a[i]
        for j in range(fixed_autos):
            if queue[i] and queue[i][0] != -1:
                queue[i].remove(1)
        for j in range(int(random.random()*10)):
            queue[i].append(1)
        return queue


quantity = 0
way = []

print('Quantify of services: ')
number = parse_int(input())
residue = [0] * number
remaining_numbers = number
a, queue, correlation = generate_queue(number)
print('Input time you have')
time = parse_int(input())

print(queue)
while time > 0 and quantity < number:
    min_queue, index_min = search_min_queue(queue, remaining_numbers)
    if time - min_queue > 0:
        time -= min_queue
        quantity += 1
        way.append(correlation[index_min]+1)
        a.remove(a[index_min])
        queue.remove(queue[index_min])
        correlation.remove(correlation[index_min])
        remaining_numbers -= 1
        if quantity == number:
            print('You go throw', quantity, 'services')
            print('Shortest way was:', way)
            break
    elif time - min_queue == 0:
        quantity += 1
        way.append(correlation[index_min]+1)
        a.remove(a[index_min])
        queue.remove(queue[index_min])
        correlation.remove(correlation[index_min])
        remaining_numbers -= 1
        print('You go throw', quantity, 'services')
        print('Shortest way was:', way)
        break
    else:
        print('You go throw', quantity, 'services')
        print('Shortest way was:', way)
        break
    queue = changes_in_queue(queue, remaining_numbers, a, residue, min_queue)
    print(queue)
