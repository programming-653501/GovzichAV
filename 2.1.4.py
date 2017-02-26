def check(a):
    while 1 > a or a > 7:
        a = int(input('Incorrect format. Input again '))
    return a


def checkcon(a):
    if a == 'n':
        print('Thank you for trying our product! Bye!')
    elif a != 'y':
        print('Incorrect input, try again')
        a = checkcon((input()))
    return a


def checkday(day, year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        while 1 > day or day > 31:
            day = int(input('Incorrect format. Input again '))
    elif month == 2 and (year % 4 == 0):
        while 1 > day or day > 29:
            day = int(input('Incorrect format. Input again '))
    elif month == 2 and (year % 4 != 0):
        while 1 > day or day > 28:
            day = int(input('Incorrect format. Input again '))
    else:
        while 1 > day or day > 30:
            day = int(input('Incorrect format. Input again '))
    return day


def checkmonth(month):
    while 1 > month or month > 12:
        month = int(input('Incorrect format. Input again '))
    return month


def option1():
    while True:
        try:
            year = int(input('Enter year: '))
        except ValueError:
            print('Incorrect value, try again!')
        else:
            break

    while True:
        try:
            month = checkmonth(int(input('Enter number of month: ')))
        except ValueError:
            print('Incorrect value, try again!')
        else:
            break

    while True:
        try:
            day = checkday(int(input('Enter day: ')), year, month)
        except ValueError:
            print('Incorrect value, try again!')
        else:
            break
    return year, month, day


def option2(day, month, year):
    mapm = {1: 'January', 2: 'February', 3: 'Mach', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    print(day, mapm[month], year)


def option3(day, month, year):
    month1 = '0' + str(month)
    day1 = '0' + str(day)
    if day < 10 and month < 10:
       print(day1, month1, year, sep='.')
    elif month < 10:
        print(day, month1, year, sep='.')
    elif day < 10:
        print(day1, month, year, sep='.')
    else:
        print(day, month, year, sep='.')


def option4(day, month, year):
    k = day
    for month in range(1, month):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            k += 31
        elif month == 2 and (year % 4 == 0):
            k += 29
        elif month == 2 and (year % 4 != 0):
            k += 28
        else:
            k += 30
    print('Day of year', k)
    arrw = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if month < 3:
        month +=12
        year -= 1
    h = (day + 13 * (month + 1) // 5 + year % 100 + (year % 100) // 4 + year // 100 // 4 + 2 * (year // 100)) % 7
    print('Day of week is', arrw[h])


def option5(day, month, year):
    k = 0
    for year in range(year):
        if year % 4 == 0:
            k += 366
        else:
            k += 365
    k += day
    for month in range(1, month):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            k += 31
        elif month == 2 and (year % 4 == 0):
            k += 29
        elif month == 2 and (year % 4 != 0):
            k += 28
        else:
            k += 30
    print('Number of days from AD started:', k)


y, m, d = 0, 0, 0
print('do you like to start? (Format of input y/n)')
key = checkcon(input())
while key == 'y':
    print('Choose option you want to use: ')
    print('1. Input of date')
    print('2. Output date in format 1 January 2010')
    print('3. Output date in format 01.01.10.')
    print('4. Day of year and day in week')
    print('5. Number of days from AD started:')
    print('6. Information about author and version of program')
    print('7. Exit')

    while True:
        try:
            ans = check(int(input('Enter number of option ')))
        except ValueError:
            print('Incorrect value, try again!')
        else:
            break

    if ans == 1:
        y, m, d = option1()
    elif ans == 2:
        if y == 0 and m == 0 and d == 0:
            print('You did not input date. Please do it: ')
            y, m, d = option1()
        option2(d, m, y)
    elif ans == 3:
        if y == 0 and m == 0 and d == 0:
            print('You did not input date. Please do it: ')
            y, m, d = option1()
        option3(d, m, y)
    elif ans == 4:
        if y == 0 and m == 0 and d == 0:
            print('You did not input date. Please do it: ')
            y, m, d = option1()
        option4(d, m, y)
    elif ans == 5:
        if y == 0 and m == 0 and d == 0:
            print('You did not input date. Please do it: ')
            y, m, d = option1()
        option5(d, m, y)
    elif ans == 6:
        print(' Author: Govzich Anastasia \n Version of program: 2.1.4')
    elif ans == 7:
        print('Bye!')
        break
    print('do you like to continue? (Format of input y/n)')
    key = checkcon(input())
