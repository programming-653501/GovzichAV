def check_user_name(u_name):
    while u_name is None:
        print('This is required field! Please input it again:')
        u_name = input()
    return u_name


def check_menu(answer):
    while True:
        try:
            answer = int(answer)
        except ValueError:
            print('Incorrect input! Try again:')
            answer = input()
        else:
            break
    return answer


def check_search(answer):
    while True:
        try:
            answer = int(answer)
        except ValueError:
            print('Incorrect input! Try again:')
            answer = input()
        else:
            break
    return answer
