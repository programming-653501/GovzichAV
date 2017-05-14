from LinkedList import LinkedList
from User import User
from WorkWithProfiles import search_by_city, search_by_education, search_by_interest, search_by_job, check_search


def add_user(linked_list):
    user = User()
    user.id = linked_list.last.data.id + 1
    user.input_info()
    linked_list.add(user)
    print('User was successfully added! \n')


def exit_network(linked_list):
    file = open('users.txt', 'w')
    count = 0
    current = linked_list.first
    while count < linked_list.length:
        str_interests = ''
        str_friends = ''
        for interest in current.data.interests:
            str_interests += interest + ' '
        for friend in current.data.friends:
            str_friends += str(friend) + ' '
        file.write(str(current.data.id)+' '+current.data.second_name+' '+current.data.name+' '+current.data.city +
                   ' '+current.data.education+' '+current.data.job + ' ' +
                   '['+str_interests.rstrip()+']'+' '+'['+str_friends.rstrip()+']'+'\n')
        current = current.next
        count += 1
    file.close()


def search_user(linked_list):
    print('Search by:')
    print('1. Interest')
    print('2. City')
    print('3. Education')
    print('4. Job')
    answer = check_search(input())
    print()
    if answer == 1:
        search_by_interest(linked_list)
    elif answer == 2:
        search_by_city(linked_list)
    elif answer == 3:
        search_by_education(linked_list)
    elif answer == 4:
        search_by_job(linked_list)
    else:
        print('Incorrect input!')
        print()
        search_user(linked_list)


def start():
    file = open('users.txt', 'r')
    user_list = LinkedList()

    for line in file:

        user = User()
        user_data = line.split()
        user.id = int(user_data[0])
        user.second_name = user_data[1]
        user.name = user_data[2]
        user.city = user_data[3]
        user.education = user_data[4]
        user.job = user_data[5]
        i = 7
        if user_data[6] != '[]':
            if user_data[6][len(user_data[6])-1] == ']':
                user.interests.append(user_data[6][1:len(user_data[6]) - 1])
            else:
                user.interests.append(user_data[6][1:len(user_data[6])])
                while user_data[i][len(user_data[i])-1] != ']':
                    user.interests.append(user_data[i])
                    i += 1
                user.interests.append(user_data[i][0:len(user_data[i])-1])
                i += 1
        else:
            i += 1
        if user_data[i] != '[]':
            if user_data[i][len(user_data[i]) - 1] == ']':
                user.friends.append(user_data[i][1:len(user_data[i]) - 1])
            else:
                user.friends.append(user_data[i][1:len(user_data[i])])
                if len(user_data) > i:
                    i += 1
                while user_data[i][len(user_data[i])-1] != ']':
                    user.friends.append(user_data[i])
                    i += 1
                user.friends.append(user_data[i][0:len(user_data[i])-1])
        user_list.add(user)
    file.close()
    return user_list
