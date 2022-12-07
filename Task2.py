# Задача 2
'''
    Создайте программу для игры в "Крестики-нолики".
'''

from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.title('Крестики-Нолики')
stop_game = False
game_map = []
countX = 0
winner = 'Nobody'

def NewGame():
    for i in range(3):
        for j in range(3):
            game_map[i][j]['text'] = ' '
            game_map[i][j]['background'] = '#BAE4EF'
    global stop_game
    stop_game = False
    global countX
    countX = 0
    global winner
    winner = 'Nobody'

def Click(x, y):
    if (not(stop_game)) and game_map[x][y]['text'] == ' ':
        game_map[x][y]['text'] = 'X'
        global countX
        countX += 1
        CheckWinner('X')
        if (not(stop_game)) and countX < 5:
            ComputerMotion()
            CheckWinner('O')
        elif countX == 5:
            messagebox.showinfo("Игра окончена", "Победила дружба")

def  CheckWinner(sign):
    for i in range(3):
        CheckLine(game_map[i][0], game_map[i][1], game_map[i][2], sign)
        CheckLine(game_map[0][i], game_map[1][i], game_map[2][i], sign)
    CheckLine(game_map[0][0], game_map[1][1], game_map[2][2], sign)
    CheckLine(game_map[2][0], game_map[1][1], game_map[0][2], sign)

def CheckLine(x1, x2, x3, sign):
    if x1['text'] == sign and x2['text'] == sign and x3['text'] == sign:
        x1['background'] = x2['background'] = x3['background'] = '#F7B3B9'
        global stop_game
        stop_game = True
        global winner
        if sign == 'O':
            messagebox.showinfo("Игра окончена", "Вы проиграли")
        elif sign == 'X':
            messagebox.showinfo("Игра окончена", "Вы выиграли")


def IsWinningMove(x1, x2, x3, sign):
    result = False
    if x1['text'] == ' ' and x2['text'] == sign and x3['text'] == sign:
        x1['text'] = 'O'
        result = True
    if x1['text'] == sign and x2['text'] == ' ' and x3['text'] == sign:
        x2['text'] = 'O'
        result = True
    if x1['text'] == sign and x2['text'] == sign and x3['text'] == ' ':
        x3['text'] = 'O'
        result = True
    return result

def ComputerMotion():
    for i in range(3):
        if IsWinningMove(game_map[i][0], game_map[i][1], game_map[i][2], 'O'):
            return
        if IsWinningMove(game_map[0][i], game_map[1][i], game_map[2][i], 'O'):
            return
    if IsWinningMove(game_map[0][0], game_map[1][1], game_map[2][2], 'O'):
        return
    if IsWinningMove(game_map[2][0], game_map[1][1], game_map[0][2], 'O'):
        return
    for i in range(3):
        if IsWinningMove(game_map[i][0], game_map[i][1], game_map[i][2], 'X'):
            return
        if IsWinningMove(game_map[0][i], game_map[1][i], game_map[2][i], 'X'):
            return
    if IsWinningMove(game_map[0][0], game_map[1][1], game_map[2][2], 'X'):
        return
    if IsWinningMove(game_map[2][0], game_map[1][1], game_map[0][2], 'X'):
        return
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if game_map[i][j]['text'] == ' ':
            game_map[i][j]['text'] = 'O'
            break

def About():
    text = " Игра в крестики-нолики с компьютером \n Ваш ход крестиком первый"
    messagebox.showinfo("О программе", text)

for i in range(3):
    line = []
    for j in range(3):
        button = Button(window, text=' ', width = 4, height = 2,
                        font = ('Verdana', 30, 'bold'),
                        background = '#BAE4EF',
                        command = lambda i = i, j = j: Click(i, j))
        button.grid(row = i, column = j, sticky='nsew')
        line.append(button)
    game_map.append(line)

main_menu = Menu()
main_menu.add_cascade(label = "Новая игра", command = NewGame)
main_menu.add_cascade(label = "Справка", command = About)
main_menu.add_cascade(label = "Выход", command = window.quit)
window.config(menu = main_menu)

window.attributes("-toolwindow", 1)
window.resizable(width = False, height  = False)
window.eval('tk::PlaceWindow . center')

window.mainloop()

