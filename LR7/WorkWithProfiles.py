from Checks import check_search, check_menu


def search_by_interest(linked_list):
    print('What interest you search?')
    request = input().lower()
    count = 0
    users = []
    coincidence = 0
    current = linked_list.first
    while count < linked_list.length:
        for interest in current.data.interests:
            if interest == request:
                users.append(current.data.id)
                coincidence += 1
                break
        current = current.next
        count += 1
    if coincidence == 0:
        print('No users with such interest')
    else:
        print_users(users, linked_list)
    print('You can watch profiles. Input id of profile or press anything to Home page')
    answer = input()
    view_profile(answer, linked_list)


def search_by_city(linked_list):
    print('What city you search?')
    request = input()
    count = 0
    users = []
    coincidence = 0
    current = linked_list.first
    while count < linked_list.length:
        if current.data.city == request:
            users.append(current.data.id)
            coincidence += 1
        current = current.next
        count += 1
    if coincidence == 0:
        print('No user lives in this city')
    else:
        print_users(users, linked_list)
    print('You can watch profiles. Input id of profile or press anything to Home page')
    answer = input()
    view_profile(answer, linked_list)


def search_by_education(linked_list):
    print('What education you search?')
    request = input()
    count = 0
    users = []
    coincidence = 0
    current = linked_list.first
    while count < linked_list.length:
        if current.data.education == request:
            users.append(current.data.id)
            coincidence += 1
        current = current.next
        count += 1
    if coincidence == 0:
        print('No user has this background')
    else:
        print_users(users, linked_list)
    print('You can watch profiles. Input id of profile or press anything to Home page')
    answer = input()
    view_profile(answer, linked_list)


def search_by_job(linked_list):
    print('What job you search?')
    request = input().lower()
    count = 0
    users = []
    coincidence = 0
    current = linked_list.first
    while count < linked_list.length:
        if current.data.job == request:
            users.append(current.data.id)
            coincidence += 1
        current = current.next
        count += 1
    if coincidence == 0:
        print('No user has in this job')
    else:
        print_users(users, linked_list)
    print('You can watch profiles. Input id of profile or press anything to Home page')
    answer = input()
    view_profile(answer, linked_list)


def print_users(users, linked_list):
    for user in users:
        current = linked_list.first
        count = 0
        while count < linked_list.length:
            if current.data.id == user:
                print(current.data.id, current.data.name, current.data.second_name)
            count += 1
            current = current.next


def view_profile(user_id, linked_list):
    current = linked_list.first
    count = 0
    try:
        while count < linked_list.length:
            if current.data.id == int(user_id):
                print(current.data.name, current.data.second_name)
                print('City:', current.data.city)
                print('Education:', current.data.education)
                print('Job:', current.data.job)
                print(current.data.interests)
                print_friends(current, linked_list)
                menu_profile(current, linked_list)
                return
            count += 1
            current = current.next
    except ValueError:
        print('Return to main menu...\n')


def print_friends(user, linked_list):
    coincidence = 0
    print('Friends:')
    for friend in user.data.friends:
        count = 0
        current = linked_list.first
        while count < linked_list.length:
            if current.data.id == int(friend):
                coincidence += 1
                print(current.data.id, current.data.name, current.data.second_name)
                break
            count += 1
            current = current.next
    if coincidence == 0:
        print('User does not have friends')
    print()


def menu_profile(user, linked_list):
    print('Profile settings: ')
    print('1. Choose another user')
    print('2. Correct connections')
    print('3. To main menu')

    answer = check_menu(input())
    print()

    if answer == 1:
        view_profile(input('Input user id: '), linked_list)
    elif answer == 2:
        change_connections(user, linked_list)
    elif answer == 3:
        return
    else:
        print('Incorrect input! Try again')
        print()
        menu_profile(user, linked_list)


def change_connections(user, linked_list):
    print('You want:')
    print('1. Add connection')
    print('2. Delete connection')

    answer = check_menu(input())

    if answer == 1:
        add_connection(user, linked_list)
    elif answer == 2:
        delete_connection(user, linked_list)
    else:
        print('Incorrect input! Try again')
        print()
        change_connections(user, linked_list)


def add_connection(user, linked_list):
    print('print user id, which you want to add')
    id_add = int(check_menu(input()))
    if id_add > linked_list.length:
        print('No such user')
        view_profile(user.data.id, linked_list)
    else:
        for friend in user.data.friends:
            if id_add == int(friend):
                print('Connection already made')
                view_profile(user.data.id, linked_list)
                return
        user.data.friends.append(id_add)
        count = 0
        current = linked_list.first
        while count < linked_list.length:
            if current.data.id == id_add:
                current.data.friends.append(user.data.id)
                break
            count += 1
            current = current.next
        view_profile(user.data.id, linked_list)


def delete_connection(user, linked_list):
    print('print user id, which you want to delete')
    id_delete = int(input())
    if id_delete > linked_list.length:
        print('No such user')
        print()
        view_profile(user.data.id, linked_list)
    else:
        i = 0
        for friend in user.data.friends:
            if int(id_delete) == int(friend):
                i += 1
                break
        if i == 0:
            print('No user in friends to delete')
            print()
            view_profile(user.data.id, linked_list)
        user.data.friends.remove(int(id_delete))
        count = 0
        current = linked_list.first
        while count < linked_list.length:
            if int(current.data.id) == int(id_delete):
                current.data.friends.remove(int(user.data.id))
                view_profile(user.data.id, linked_list)
                break
            count += 1
            current = current.next
