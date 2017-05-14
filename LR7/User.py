from Checks import check_user_name


class User:
    def __init__(self):
        self.id = None
        self.second_name = None
        self.name = None
        self.city = None
        self.education = None
        self.job = None
        self.interests = []
        self.friends = []

    def input_info(self):
        print('Let\'s create new user! \nInput name')
        self.name = check_user_name(input())
        print('Input second name')
        self.second_name = check_user_name(input())
        print('Input city, if you don\'t want to do it, press Enter ')
        self.city = input()
        print('Input education, if you don\'t want to do it, press Enter ')
        self.education = input()
        print('Input job, if you don\'t want to do it, press Enter ')
        self.job = input()
        print('Input interests, if you don\'t want to do it, press Enter ')
        interests = input()
        self.interests = interests.split()

