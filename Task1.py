# Задача 1
"""
    Создайте программу для игры с конфетами человек против компьютера.
    Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
                    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
                    Все конфеты оппонента достаются сделавшему последний ход.
    Подумайте как наделить бота "интеллектом"
"""

import random
from random import randint, choice

messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']

total = 150
max_to_take = 28

# player = 1 - Human
# player = 0 - Artificial Intelligence

def InitGame():
    first = randint(0, 1)
    if first == 1:
        print("Первый ход ваш. Поехали!")
    else:
        print("Первый ход искусственного интеллекта игры. Поехали!")
    return first

def Game(player):
    global total
    while total > max_to_take:
        if player == 0:
            if total - max_to_take == 29:
                motion = total - max_to_take
            else:
                motion = random.randint(1, min(max_to_take, total))
                while total - motion <= max_to_take:
                    motion = random.randint(1, min(max_to_take, total))
            print("ИИ забирает", motion)
        else:
            motion = int(input("Укажите кол-во конфет, которые вы забираете " ))
            while (not(1 <= motion <= min(max_to_take, total))):
                print(f'Можно забирать не более {max_to_take} конфет. На столе всего {total} конфет')
                motion = int(input())
        total = total - motion
        if total > max_to_take:
            print(f'На столе осталось {total} конфет')
        else:
            print('Игра окончена')
        if player == 1:
            return 0
        else:
            return 1

player = InitGame()
while total > max_to_take:
    player = Game(player)
if player == 1:
    print('Вы  победили! Все конфеты ваши! Надеюсь, поделитесь, а то слипнется :)')
else:
    print('Вы проиграли искусственному интеллекту :( Ему достаются все конфеты!')