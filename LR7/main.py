from LinkedList import LinkedList
from User import User
from Checks import check_menu
from MenuOptions import add_user, search_user, exit_network, start


user_list = start()


while True:
    print('Menu: ')
    print('1. Add new user')
    print('2. Search user')
    print('3. Exit')
    answer = check_menu(input())
    print()

    if answer == 1:
        add_user(user_list)
    elif answer == 2:
        search_user(user_list)
    elif answer == 3:
        exit_network(user_list)
        break
    else:
        print('Incorrect input! Try again')
        print()
