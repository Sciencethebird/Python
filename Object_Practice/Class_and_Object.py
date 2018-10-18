'''
 - class
 - function
'''

class crush:

    def __init__(self, new_name = 'Nobody', level = 0, state = False):
        self.name = new_name
        self.if_she_loves_you = state
        self.level_of_friendship = level

    def show_stats(self):
        print('Name:', self.name)
        print('Friendship Score:', self.level_of_friendship)
        print('Does she love you?', self.if_she_loves_you)

    def reply_your_message(self):
        self.level_of_friendship += 5

    def follow_you_on_instagram(self):
        self.level_of_friendship += 50

    def ignore_your_message(self):
        self.level_of_friendship = 0
        self.if_she_loves_you = False

'''''
people1 = crush('Yahan', 50, False)
people2 = crush()
crushes = {'yahan':people1,'quiet':people2} #dictionary

people1.ignore_your_message()
people1.if_she_loves_you = True

people2.reply_your_message()
people2.follow_you_on_instagram()

crushes['yahan'].show_stats()
people2.show_stats()
'''''
