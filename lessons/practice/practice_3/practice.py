from random import randint
from termcolor import colored, cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return colored(f'Я - {self.name}, сытость {self.fullness}', color='yellow')

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='blue')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'У {self.name} нет еды', color='red')

    def work(self):
        cprint(f'{self.name} сходил на работу', color='cyan')
        self.house.money += 50
        self.fullness -= 10

    def watching_tv(self):
        cprint(f'{self.name} смотрел телевизор целый день', color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магазин', color='cyan')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('Деньги кончились', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watching_tv()

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print(f'{self.name} въехал в дом')


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return colored(f'В доме еды осталось {self.food}, денег {self.money}', color='yellow')


beavis = Man(name='Бивис')
butthead = Man(name='Батхед')
my_sweet_home = House()

beavis.go_into_the_house(house=my_sweet_home)
butthead.go_into_the_house(house=my_sweet_home)

for day in range(1, 366):
    print(f'=-=-=-=-=-=-=-=-=-= День {day} =-=-=-=-=-=-=-=-=-=')
    beavis.act()
    butthead.act()
    print('--------------------------------------------------')
    print(my_sweet_home)
    print(beavis)
    print(butthead)
