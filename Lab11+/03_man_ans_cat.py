# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

class Cat:
    def __init__(self, name, fullness):
        self.fullness = fullness
        self.house = None
        self.name = name

    def __str__(self):
        return 'сытость кота {} - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.catfood >= 10:
            cprint('кот {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.catfood -= 10
        else:
            cprint('кошачьей еды нет', color='red')
            self.sleep()

    def sleep(self):
        cprint('кот {} спал весь день'.format(self.name), color='yellow')
        self.fullness -= 10

    def wallpaper(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('кот {} драл обои весь день'.format(self.name), color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 20 and self.house.catfood >= 10:
            self.eat()
        elif dice == 1:
            self.wallpaper()
        elif dice == 2:
            self.sleep()


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} учил Python целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='cyan')

    def buy_catfood(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.catfood += 50
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean(self):
        self.house.mud -= 100
        self.fullness -= 20
        cprint('{} прибрался в доме'.format(self.name), color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30 and self.house.food >= 10:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.catfood < 10:
            self.buy_catfood()
        elif self.house.mud >= 100:
            self.clean()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.buy_catfood()
        elif dice == 4:
            self.work()
        else:
            self.watch_MTV()

    def takecat(self, cat):
        cat.house = self.house


class House:
    def __init__(self):
        self.food = 50
        self.money = 0
        self.catfood = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды осталось {}, грязи {}'.format(
            self.food, self.money, self.catfood, self.mud)


citizens = [
    Man(name='Серафим'),
    Man(name='Виталий'),
    Man(name='Никита'),
    # Man(name='Иван')
]
cats = [
    Cat(name='Том', fullness=50),
    Cat(name='Мурзик', fullness=35),
    Cat(name='Мурка', fullness=40)
    # Cat(name='Компот', fullness=45)
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
    for cat in cats:
        citisen.takecat(cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)
    for cat in cats:
        print(cat)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
