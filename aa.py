import os
class User:
    def __init__(self, login, password, age, gender):
        self.login = login
        self.password = password
        self.age = age
        self.gender = gender
        self.tanla_values = ['0', '1', '2']

    def tanla(self):
        print('''
        [0] ---> Exit
        [1] ---> Register
        [2] ---> Log In
        ''')

    def tanla_option(self):
        self.tanla()
        inp_tanla = input('[1, 2, 3]: ')
        while inp_tanla not in self.tanla_values:
            self.clear()
            self.tanla()
            inp_tanla = input('[1, 2, 3]: ')
        if inp_tanla == self.tanla_values[0]:
            self.exit()
        if inp_tanla == self.tanla_values[1]:
            self.register()
        if inp_tanla == self.tanla_values[2]:
            self.log_in()

    def exit(self):
        print('Tugadi!!!')
        exit()

    def register(self):
        pass

    def log_in(self):
        pass

    @staticmethod
    def clear():
        os.system('clear')


man = User('qwe', 'qwe', 'qwe', 'qwe')
man.tanla_option()
