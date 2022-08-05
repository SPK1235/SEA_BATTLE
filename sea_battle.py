import pygame
import sys
import random
import numpy as np


def frame(screen):
    """функция тетрадный лист и основная надпись"""
    global flag_sound
    if flag_sound:
        pygame.Surface.fill(screen, (255, 250, 250), rect=(885, 90, 60, 60))
        smail_def = pygame.image.load('звук.png')
        screen.blit(smail_def, (890, 90))
    if not flag_sound:
        pygame.Surface.fill(screen, (255, 250, 250), rect=(885, 90, 60, 60))
        smail_def = pygame.image.load('звук.png')
        screen.blit(smail_def, (890, 90))
        pygame.draw.line(screen, (255, 0, 0), (890, 90), (940, 140), 5)
        pygame.draw.line(screen, (255, 0, 0), (940, 90), (890, 140), 5)
    for i in range(0, 1020, 30):
        pygame.draw.line(screen, (106, 90, 205), (i, 0), (i, 700), 1)
    for i in range(0, 700, 30):
        pygame.draw.line(screen, (106, 90, 205), (0, i), (1020, i), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (1020, 0), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 700), 5)
    pygame.draw.line(screen, (0, 0, 0), (1019, 0), (1019, 700), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 698), (1020, 698), 3)
    smail_def = pygame.image.load('осн.надпись.png')
    screen.blit(smail_def, (140, 20))
    smail_def = pygame.image.load('надпись.png')
    screen.blit(smail_def, (280, 655))
    smail_def = pygame.image.load('мой флот.png')
    screen.blit(smail_def, (180, 170))
    smail_def = pygame.image.load('количество ходов.png')
    screen.blit(smail_def, (90, 590))
    pygame.display.update((885, 90, 60, 60))


def text(screen, size, content, point, color_content):
    txt = pygame.font.SysFont('Arial Black', size)
    text_1 = txt.render(content, True, color_content)
    screen.blit(text_1, point)


def button(screen, x_start, y_start, content, x_a, y_a):
    pygame.Surface.fill(screen, (255, 255, 255), rect=(x_start, y_start, 140, 40))
    pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 140, 40))
    pygame.draw.rect(screen, (0, 0, 128), (x_start, y_start, 140, 40), 4)
    el = pygame.font.SysFont('serif', 25)
    text_1 = el.render(content, True, (0, 0, 0))
    screen.blit(text_1, (x_start + x_a, y_start + y_a))


def grid(screen, x_start, x_end, y_start, y_end):
    """функция игровое поле 10 х 10"""
    cnt = 0
    list_letter = ('а.png', 'б.png', 'в.png', 'г.png', 'д.png', 'е.png', 'ж.png', 'з.png', 'и.png', 'к.png')
    list_number = ('1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png')
    for i in range(x_start, x_end, 30):
        pygame.draw.line(screen, (72, 61, 139), (i, y_start), (i, y_end), 2)
        if cnt < 10:
            if cnt == 6:
                smail_def = pygame.image.load(list_letter[cnt])
                screen.blit(smail_def, (i, y_start - 45))
            else:
                smail_def = pygame.image.load(list_letter[cnt])
                screen.blit(smail_def, (i + 5, y_start - 45))
            cnt += 1
    cnt = 0
    for i in range(y_start, y_end, 30):
        pygame.draw.line(screen, (72, 61, 139), (x_start, i), (x_end, i), 2)
        if cnt < 10:
            if cnt == 9:
                smail_def = pygame.image.load(list_number[cnt])
                screen.blit(smail_def, (x_start - 42, i - 12))
            else:
                smail_def = pygame.image.load(list_number[cnt])
                screen.blit(smail_def, (x_start - 25, i - 12))
            cnt += 1


def placement_ships(screen):
    smail_def = pygame.image.load('линкор.png')
    screen.blit(smail_def, (450, 270))
    smail_def = pygame.image.load('н.линкор.png')
    screen.blit(smail_def, (580, 257))
    smail_def = pygame.image.load('крейсер.png')
    screen.blit(smail_def, (450, 330))
    smail_def = pygame.image.load('н.крейсер.png')
    screen.blit(smail_def, (550, 315))
    smail_def = pygame.image.load('крейсер.png')
    screen.blit(smail_def, (450, 390))
    smail_def = pygame.image.load('н.крейсер.png')
    screen.blit(smail_def, (550, 375))
    smail_def = pygame.image.load('эсминец.png')
    screen.blit(smail_def, (450, 450))
    smail_def = pygame.image.load('н.эсминец.png')
    screen.blit(smail_def, (545, 435))
    smail_def = pygame.image.load('эсминец.png')
    screen.blit(smail_def, (450, 510))
    smail_def = pygame.image.load('н.эсминец.png')
    screen.blit(smail_def, (545, 495))
    smail_def = pygame.image.load('эсминец.png')
    screen.blit(smail_def, (750, 270))
    smail_def = pygame.image.load('н.эсминец.png')
    screen.blit(smail_def, (820, 257))
    smail_def = pygame.image.load('катер.png')
    screen.blit(smail_def, (750, 330))
    smail_def = pygame.image.load('н.катер.png')
    screen.blit(smail_def, (835, 320))
    smail_def = pygame.image.load('катер.png')
    screen.blit(smail_def, (750, 390))
    smail_def = pygame.image.load('н.катер.png')
    screen.blit(smail_def, (835, 380))
    smail_def = pygame.image.load('катер.png')
    screen.blit(smail_def, (750, 450))
    smail_def = pygame.image.load('н.катер.png')
    screen.blit(smail_def, (835, 440))
    smail_def = pygame.image.load('катер.png')
    screen.blit(smail_def, (750, 510))
    smail_def = pygame.image.load('н.катер.png')
    screen.blit(smail_def, (835, 500))
    smail_def = pygame.image.load('выбери корабли.png')
    screen.blit(smail_def, (570, 170))


def grout(screen):
    """функция отрисовки кораблей для установки"""
    global list_chek
    pygame.Surface.fill(screen, (255, 250, 250), rect=(440, 175, 570, 395))
    frame(screen)
    placement_ships(screen)
    smail_def = pygame.image.load('chek.png')
    if len(list_chek) > 0:
        for i in list_chek:
            screen.blit(smail_def, (i[0], i[1]))
    pygame.display.update((440, 175, 570, 395))


def generator(cell_number, n):
    """функция возможные варианты расстановки корабля относительно выбранной клетки"""
    list_cell = [cell_number]
    for i in range(cell_number, cell_number + n):
        """список вправо"""
        if i in range(10, 101, 10):
            if i not in list_cell:
                list_cell.append(i)
            break
        elif i not in list_cell:
            if 0 < i < 101:
                list_cell.append(i)
    for i in range(cell_number, cell_number - n, -1):
        """список влево"""
        if i in range(1, 92, 10):
            if i not in list_cell:
                list_cell.append(i)
            break
        elif i not in list_cell:
            if 0 < i < 101:
                list_cell.append(i)
    for i in range(cell_number + 10, cell_number + n * 10, 10):
        """список вниз"""
        if 0 < i < 101:
            list_cell.append(i)
    for i in range(cell_number - 10, cell_number - n * 10, -10):
        """список вверх"""
        if 0 < i < 101:
            list_cell.append(i)
    list_cell = sorted(list_cell)  # общий список всех клеток
    return list_cell


def reduction(list_ship, list_probability_ship, n):
    """функция сокращает возможные варианты расстановки корабля относительно  выбранных клеток"""
    difference_horizon_temp = set()
    difference = abs(list_ship[0] - list_ship[1])
    if len(list_ship) == 2:
        if difference < n:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1), list_ship[0] + n))
                                       & set(range(list_ship[1] - (n - 1), list_ship[1] + n)))
        elif difference >= 10:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1) * 10, list_ship[0] + n * 10, 10))
                                       & set(range(list_ship[1] - (n - 1) * 10, list_ship[1] + n * 10, 10)))
    if len(list_ship) == 3:
        if difference < n:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1), list_ship[0] + n))
                                       & set(range(list_ship[1] - (n - 1), list_ship[1] + n))
                                       & set(range(list_ship[2] - (n - 1), list_ship[2] + n)))
        elif difference >= 10:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1) * 10, list_ship[0] + n * 10, 10))
                                       & set(range(list_ship[1] - (n - 1) * 10, list_ship[1] + n * 10, 10))
                                       & set(range(list_ship[2] - (n - 1) * 10, list_ship[2] + n * 10, 10)))
    difference_horizon = list(difference_horizon_temp & set(list_probability_ship))
    return sorted(difference_horizon)


def ban_cell(list_ship):
    """функция формирует список запрещенных клеток для установки корабля"""
    list_ban_cell = []
    temp = set()
    list_ship = sorted(list_ship)
    for i in list_ship:
        temp.add(i - 1)
        temp.add(i - 11)
        temp.add(i - 10)
        temp.add(i - 9)
        temp.add(i + 1)
        temp.add(i + 11)
        temp.add(i + 10)
        temp.add(i + 9)
    temp = sorted(list(temp))
    for i in temp:
        if i not in list_ship:
            if 0 < i < 101:
                if list_ship[0] in range(1, 92, 10):
                    if i in range(10, 101, 10):
                        continue
                    else:
                        list_ban_cell.append(i)
                elif list_ship[0] in range(10, 101, 10) or list_ship[-1] in range(10, 101, 10):
                    if i in range(1, 92, 10):
                        continue
                    else:
                        list_ban_cell.append(i)
                else:
                    list_ban_cell.append(i)
    list_ban_cell = sorted(list(list_ban_cell))
    return list_ban_cell


def installation_options(screen, list_probability_ship):
    """Функция отображения на игровом поле вариантов установки корабля"""
    global cell
    surf = pygame.Surface((32, 32))
    surf.set_alpha(100)
    for i in list_probability_ship:
        x_start = cell[i][0]
        y_start = cell[i][2]
        pygame.Surface.fill(surf, (176, 224, 230))
        pygame.draw.rect(surf, (25, 25, 112), (0, 0, 32, 32), 4)
        screen.blit(surf, (x_start, y_start))
        pygame.display.update()


def number_shots_remaining(screen):
    """функция отображает количество оставшихся выстрелов"""
    global flag_my_shot, flag_enemy_shot
    global list_my_shot, list_injured_my_ships, list_killed_my_ships
    global list_enemy_shot, list_injured_enemy_ships, list_killed_enemy_ships
    pygame.Surface.fill(screen, (255, 250, 250), rect=(90, 590, 360, 60))
    pygame.Surface.fill(screen, (255, 250, 250), rect=(570, 590, 360, 60))
    frame(screen)
    if flag_my_shot:
        col = str(100 - len(list(set(list_my_shot) | set(list_injured_enemy_ships) | set(list_killed_enemy_ships))))
        text(screen, 30, col, (863, 595), (0, 128, 0))
        col = str(100 - len(list(set(list_enemy_shot) | set(list_injured_my_ships) | set(list_killed_my_ships))))
        text(screen, 30, col, (385, 595), (255, 0, 0))
    elif flag_enemy_shot:
        col = str(100 - len(list(set(list_my_shot) | set(list_injured_enemy_ships) | set(list_killed_enemy_ships))))
        text(screen, 30, col, (863, 595), (255, 0, 0))
        col = str(100 - len(list(set(list_enemy_shot) | set(list_injured_my_ships) | set(list_killed_my_ships))))
        text(screen, 30, col, (385, 595), (0, 128, 0))
    smail_def = pygame.image.load('количество ходов.png')
    screen.blit(smail_def, (570, 590))
    pygame.display.update()


def check_function(list_ship, n):
    list_1 = []
    list_10 = []
    for i in range(len(list_ship) - 1):
        for j in range(1, len(list_ship)):
            if abs(list_ship[i] - list_ship[j]) == 1:
                list_1.append(list_ship[i])
                list_1.append(list_ship[j])
            elif abs(list_ship[i] - list_ship[j]) == 10:
                list_10.append(list_ship[i])
                list_10.append(list_ship[j])
    list_1 = set(list_1)
    list_10 = set(list_10)
    if len(list_1) >= n and len(list_10) >= n:
        return list(set(list_1) | set(list_10))
    elif len(list_1) < n <= len(list_10):
        return list_10
    elif len(list_10) < n <= len(list_1):
        return list_1
    else:
        return []


def choice_battleship(screen, cell_number):
    """установка линкора 4 клетки"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship, list_my_battleship, list_chek
    global flag_battleship, flag_automatic
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][2]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        list_probability_ship = generator(cell_number, 4)
        list_probability_ship = list(set(list_probability_ship) - set(list_ban_cell) - set(list_my_ship))
        list_probability_ship = check_function(list_probability_ship, 4)
        if len(list_probability_ship) >= 4:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            list_battleship.append(cell_number)
            list_my_ship.append(cell_number)
            if not flag_automatic:
                installation_options(screen, list_probability_ship)
    elif (len(list_battleship) == 1 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][2]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            installation_options(screen, list(set(list_probability_ship) - set(list_ban_cell)))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
    elif (len(list_battleship) == 2 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][2]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            installation_options(screen, list(set(list_probability_ship) - set(list_ban_cell)))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
    elif (len(list_battleship) == 3 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][2]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        list_my_battleship = list_battleship.copy()
        list_battleship = []
        list_probability_ship = []
        flag_battleship = True
        smail_def = pygame.image.load('chek.png')
        screen.blit(smail_def, (690, 265))
        pygame.display.update((690, 265, 50, 50))
        list_chek.append((690, 265))


def choice_cruiser(screen, cell_number, flag):
    """установка крейсера 3 клетки"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship, list_chek, flag_automatic
    global flag_cruiser_1, flag_cruiser_2, list_my_cruiser_1, list_my_cruiser_2
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][2]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        list_probability_ship = generator(cell_number, 3)
        list_probability_ship = list(set(list_probability_ship) - set(list_ban_cell) - set(list_my_ship))
        list_probability_ship = check_function(list_probability_ship, 3)
        if len(list_probability_ship) >= 3:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            list_battleship.append(cell_number)
            list_my_ship.append(cell_number)
            if not flag_automatic:
                installation_options(screen, list_probability_ship)
    elif (len(list_battleship) == 1 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 3)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][2]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            installation_options(screen, list(set(list_probability_ship) - set(list_ban_cell)))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
    elif (len(list_battleship) == 2 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][2]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        if flag == 1:
            flag_cruiser_1 = True
            list_my_cruiser_1 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (690, 325))
            pygame.display.update((690, 325, 50, 50))
            list_chek.append((690, 325))
        elif flag == 2:
            flag_cruiser_2 = True
            list_my_cruiser_2 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (690, 385))
            pygame.display.update((690, 385, 50, 50))
            list_chek.append((690, 385))
        list_battleship = []
        list_probability_ship = []


def choice_destroyer(screen, cell_number, flag):
    """установка эсминца 2 клетки"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship, flag_automatic
    global flag_destroyer_1, flag_destroyer_2, flag_destroyer_3
    global list_my_destroyer_1, list_my_destroyer_2, list_my_destroyer_3
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][2]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        list_probability_ship = generator(cell_number, 2)
        list_probability_ship = list(set(list_probability_ship) - set(list_ban_cell) - set(list_my_ship))
        list_probability_ship = check_function(list_probability_ship, 2)
        if len(list_probability_ship) >= 2:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            list_battleship.append(cell_number)
            list_my_ship.append(cell_number)
            if not flag_automatic:
                installation_options(screen, list_probability_ship)
    elif (len(list_battleship) == 1 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][2]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        if flag == 1:
            flag_destroyer_1 = True
            list_my_destroyer_1 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (690, 445))
            pygame.display.update((690, 445, 50, 50))
            list_chek.append((690, 445))
        elif flag == 2:
            flag_destroyer_2 = True
            list_my_destroyer_2 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (690, 505))
            pygame.display.update((690, 505, 50, 50))
            list_chek.append((690, 505))
        elif flag == 3:
            flag_destroyer_3 = True
            list_my_destroyer_3 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (965, 265))
            pygame.display.update((965, 265, 50, 50))
            list_chek.append((965, 265))
        list_battleship = []
        list_probability_ship = []


def choice_boat(screen, cell_number, flag):
    """установка катера 1 клетка"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship
    global flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][2]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
        pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        if flag == 1:
            flag_boat_1 = True
            list_my_boat_1 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (965, 325))
            pygame.display.update((965, 325, 50, 50))
            list_chek.append((965, 325))
        elif flag == 2:
            flag_boat_2 = True
            list_my_boat_2 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (965, 385))
            pygame.display.update((965, 385, 50, 50))
            list_chek.append((965, 385))
        elif flag == 3:
            flag_boat_3 = True
            list_my_boat_3 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (965, 445))
            pygame.display.update((965, 445, 50, 50))
            list_chek.append((965, 445))
        elif flag == 4:
            flag_boat_4 = True
            list_my_boat_4 = list_battleship.copy()
            smail_def = pygame.image.load('chek.png')
            screen.blit(smail_def, (965, 505))
            pygame.display.update((965, 505, 50, 50))
            list_chek.append((965, 505))
        list_battleship = []
        list_probability_ship = []


def delete_ship(screen):
    pygame.Surface.fill(screen, (255, 250, 250))
    frame(screen)
    grid(screen, 120, 421, 270, 571)
    placement_ships(screen)
    button(screen, 450, 590, 'Сброс', 38, 5)
    button(screen, 635, 590, 'Расставить', 13, 5)
    button(screen, 820, 590, 'Дальше', 30, 5)
    pygame.display.update()


def delete_1(screen):
    pygame.Surface.fill(screen, (255, 250, 250), rect=(120, 270, 300, 300))
    frame(screen)
    grid(screen, 120, 421, 270, 571)
    pygame.display.update()


def automatic_placement_ships(screen):
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship
    global flag_battleship, flag_cruiser_1, flag_cruiser_2, flag_destroyer_1, flag_destroyer_2, flag_destroyer_3
    global flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1,\
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4
    if (not flag_battleship and not flag_cruiser_1 and not flag_cruiser_2 and not flag_destroyer_1
            and not flag_destroyer_2 and not flag_destroyer_3 and not flag_boat_1 and not flag_boat_2
            and not flag_boat_3 and not flag_boat_1):
        try:
            """Выбор случайного места установки линкора"""
            cell_number = random.randint(1, 100)
            choice_battleship(screen, cell_number)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
            choice_battleship(screen, cell_number)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
            choice_battleship(screen, cell_number)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
            choice_battleship(screen, cell_number)
            """Выбор случайного места установки крейсера_1 и крейсера_2"""
            for i in range(1, 3):
                cell_number = list(set(range(1, 101)) - set(list_my_ship) - set(list_ban_cell))
                cell_number = random.choice(cell_number)
                choice_cruiser(screen, cell_number, i)
                cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                                 - set(list_my_ship) - set(list_ban_cell)))
                choice_cruiser(screen, cell_number, i)
                cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                                 - set(list_my_ship) - set(list_ban_cell)))
                choice_cruiser(screen, cell_number, i)
            """Выбор случайного места установки эсминца_1, эсминца_2, эсминца_3"""
            for i in range(1, 4):
                cell_number = list(set(range(1, 101)) - set(list_my_ship) - set(list_ban_cell))
                cell_number = random.choice(cell_number)
                choice_destroyer(screen, cell_number, i)
                cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                                 - set(list_my_ship) - set(list_ban_cell)))
                choice_destroyer(screen, cell_number, i)
            """Выбор случайного места установки катера_1, катера_2, катера_3, катера_4"""
            for i in range(1, 5):
                cell_number = list(set(range(1, 101)) - set(list_my_ship) - set(list_ban_cell))
                cell_number = random.choice(cell_number)
                choice_boat(screen, cell_number, i)
        except IndexError:
            delete_ship(screen)
            list_my_ship = []  # список моих кораблей
            list_ban_cell = []  # список запрещенных клеток для установки корабля
            list_battleship = []  # список координат установки линкора
            list_probability_ship = []  # список вариатов установки корабля
            list_my_battleship = []  # координаты моего линкора
            list_my_cruiser_1 = []  # координаты моего крейсера_1
            list_my_cruiser_2 = []  # координаты моего крейсера_2
            list_my_destroyer_1 = []  # координаты моего эсминца_1
            list_my_destroyer_2 = []  # координаты моего эсминца_2
            list_my_destroyer_3 = []  # координаты моего эсминца_3
            list_my_boat_1 = []  # координаты моего катера_1
            list_my_boat_2 = []  # координаты моего катера_2
            list_my_boat_3 = []  # координаты моего катера_3
            list_my_boat_4 = []  # координаты моего катера_4
            flag_battleship = False  # установлен ли линкор : True - да , False - нет
            flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
            flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
            flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
            flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
            flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
            flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
            flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
            flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
            flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
            automatic_placement_ships(screen)


def automatic_placement_enemy_ships():
    global list_enemy_ships, list_ban_cell, list_battleship, list_probability_ship
    global list_enemy_battleship, list_enemy_cruiser_1, list_enemy_cruiser_2
    global list_enemy_destroyer_1, list_enemy_destroyer_2, list_enemy_destroyer_3
    global list_enemy_boat_1, list_enemy_boat_2, list_enemy_boat_3, list_enemy_boat_4
    list_ban_cell = []
    list_battleship = []
    list_probability_ship = []
    try:
        """Выбор случайного места установки линкора"""
        cell_number = random.randint(1, 100)
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = generator(cell_number, 4)
        cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_enemy_battleship = list_battleship.copy()
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        list_battleship = []
        list_probability_ship = []
        """Выбор случайного места установки крейсера_1 и крейсера_2"""
        for i in range(1, 3):
            cell_number = list(set(range(1, 101)) - set(list_enemy_ships) - set(list_ban_cell))
            cell_number = random.choice(cell_number)
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            list_probability_ship = generator(cell_number, 3)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                             - set(list_enemy_ships) - set(list_ban_cell)))
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            list_probability_ship = reduction(list_battleship, list_probability_ship, 3)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                             - set(list_enemy_ships) - set(list_ban_cell)))
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            if i == 1:
                list_enemy_cruiser_1 = list_battleship.copy()
            elif i == 2:
                list_enemy_cruiser_2 = list_battleship.copy()
            temp = ban_cell(list_battleship)
            for j in temp:
                list_ban_cell.append(j)
            list_ban_cell = list(set(list_ban_cell))
            list_battleship = []
            list_probability_ship = []
        """Выбор случайного места установки эсминца_1, эсминца_2, эсминца_3"""
        for i in range(1, 4):
            cell_number = list(set(range(1, 101)) - set(list_enemy_ships) - set(list_ban_cell))
            cell_number = random.choice(cell_number)
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            list_probability_ship = generator(cell_number, 2)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                             - set(list_enemy_ships) - set(list_ban_cell)))
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            if i == 1:
                list_enemy_destroyer_1 = list_battleship.copy()
            elif i == 2:
                list_enemy_destroyer_2 = list_battleship.copy()
            elif i == 3:
                list_enemy_destroyer_3 = list_battleship.copy()
            temp = ban_cell(list_battleship)
            for j in temp:
                list_ban_cell.append(j)
            list_ban_cell = list(set(list_ban_cell))
            list_battleship = []
            list_probability_ship = []
        """Выбор случайного места установки катера_1, катера_2, катера_3, катера_4"""
        for i in range(1, 5):
            cell_number = list(set(range(1, 101)) - set(list_enemy_ships) - set(list_ban_cell))
            cell_number = random.choice(cell_number)
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            if i == 1:
                list_enemy_boat_1 = list_battleship.copy()
            elif i == 2:
                list_enemy_boat_2 = list_battleship.copy()
            elif i == 3:
                list_enemy_boat_3 = list_battleship.copy()
            elif i == 4:
                list_enemy_boat_4 = list_battleship.copy()
            temp = ban_cell(list_battleship)
            for j in temp:
                list_ban_cell.append(j)
            list_ban_cell = list(set(list_ban_cell))
            list_battleship = []
            list_probability_ship = []
        k = random.randint(1, 11)
        n = 10 // k
        set_1 = {1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91}
        tmp = set(list_enemy_ships) & set_1
        if len(tmp) > n:
            list_enemy_ships = []
            list_ban_cell = []
            list_battleship = []
            list_probability_ship = []
            list_enemy_battleship = []
            list_enemy_cruiser_1 = []
            list_enemy_cruiser_2 = []
            list_enemy_destroyer_1 = []
            list_enemy_destroyer_2 = []
            list_enemy_destroyer_3 = []
            list_enemy_boat_1 = []
            list_enemy_boat_2 = []
            list_enemy_boat_3 = []
            list_enemy_boat_4 = []
            automatic_placement_enemy_ships()
    except IndexError:
        list_enemy_ships = []
        list_ban_cell = []
        list_battleship = []
        list_probability_ship = []
        list_enemy_battleship = []
        list_enemy_cruiser_1 = []
        list_enemy_cruiser_2 = []
        list_enemy_destroyer_1 = []
        list_enemy_destroyer_2 = []
        list_enemy_destroyer_3 = []
        list_enemy_boat_1 = []
        list_enemy_boat_2 = []
        list_enemy_boat_3 = []
        list_enemy_boat_4 = []
        automatic_placement_enemy_ships()
        k = random.randint(1, 11)
        n = 10 // k
        set_1 = {1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91}
        tmp = set(list_enemy_ships) & set_1
        if len(tmp) > n:
            list_enemy_ships = []
            list_ban_cell = []
            list_battleship = []
            list_probability_ship = []
            list_enemy_battleship = []
            list_enemy_cruiser_1 = []
            list_enemy_cruiser_2 = []
            list_enemy_destroyer_1 = []
            list_enemy_destroyer_2 = []
            list_enemy_destroyer_3 = []
            list_enemy_boat_1 = []
            list_enemy_boat_2 = []
            list_enemy_boat_3 = []
            list_enemy_boat_4 = []
            automatic_placement_enemy_ships()


def my_shot(screen, cell_number):
    global cell, cell_2, flag_sound, flag_game, flag_my_victory
    global flag_my_shot, flag_enemy_shot
    global list_enemy_ships, list_killed_enemy_ships, list_my_shot, list_injured_enemy_ships
    if cell_number not in list_my_shot and cell_number not in list_killed_enemy_ships \
            and cell_number not in list_injured_enemy_ships:
        if flag_sound:
            pygame.mixer.music.play()
        if flag_my_shot and not flag_enemy_shot:
            x_start = cell_2[cell_number][0]
            y_start = cell_2[cell_number][2]
        else:
            x_start = cell[cell_number][0]
            y_start = cell[cell_number][2]
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 20, 5)
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start - 15), (x_start + 16, y_start + 8), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start + 24), (x_start + 16, y_start + 47), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start - 15, y_start + 16), (x_start + 8, y_start + 16), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 24, y_start + 16), (x_start + 47, y_start + 16), 5)
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(800)
        smail = pygame.image.load('взрыв.png')
        screen.blit(smail, (x_start - 10, y_start - 5))
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(1000)
        pygame.Surface.fill(screen, (255, 250, 250), rect=(540, 210, 380, 380))
        frame(screen)
        grid(screen, 600, 901, 270, 571)
        if cell_number in list_enemy_ships:
            list_injured_enemy_ships.append(cell_number)
            if len(list(set(list_enemy_battleship) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_battleship:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_battleship)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_cruiser_1) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_cruiser_1:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_cruiser_1)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_cruiser_2) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_cruiser_2:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_cruiser_2)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_destroyer_1) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_destroyer_1:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_destroyer_1)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_destroyer_2) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_destroyer_2:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_destroyer_2)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_destroyer_3) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_destroyer_3:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_destroyer_3)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_1) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_1:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_1)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_2) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_2:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_2)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_3) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_3:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_3)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_4) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_4:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_4)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
        else:
            list_my_shot.append(cell_number)
            flag_my_shot = False
            flag_enemy_shot = True
        for i in list_injured_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][2]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        list_killed_enemy_ships = list(set(list_killed_enemy_ships))
        for i in list_killed_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][2]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_my_shot:
            x_start = cell_2[i][0]
            y_start = cell_2[i][2]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
    pygame.display.update((540, 210, 380, 380))
    if len(list_killed_enemy_ships) == 20:
        flag_game = False
        flag_my_victory = True
        pygame.time.wait(1500)


def strategy_3():
    global list_enemy_shot, list_killed_my_ships, list_injured_my_ships, flag_strategy_3, flag_strategy_4
    cnt = np.arange(1, 101).reshape((10, 10))
    my_list = []
    shot = list(set(list_enemy_shot) | set(list_killed_my_ships) | set(list_injured_my_ships))
    for i in shot:
        if 1 <= i <= 10:
            cnt[0, i - 1] = 0
        elif i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            i = str(i)
            row = int(i[0]) - 1
            column = 9
            cnt[row, column] = 0
        elif i == 100:
            row = 9
            column = 9
            cnt[row, column] = 0
        else:
            i = str(i)
            row = int(i[0])
            column = int(i[1]) - 1
            cnt[row, column] = 0
    for row in cnt:
        len_row = 0
        len_row_max = 0
        for i in row:
            if i == 0:
                if len_row > len_row_max:
                    len_row_max = len_row
                len_row = 0
            else:
                len_row += 1
        if len_row > len_row_max:
            my_list.append(len_row)
        else:
            my_list.append(len_row_max)
    my_list_max_horizont = max(my_list)
    index_my_list = my_list.index(my_list_max_horizont)
    list_shot_1 = cnt[index_my_list: index_my_list + 1]
    cnt_1 = cnt.transpose()
    my_list = []
    for row in cnt_1:
        len_row = 0
        len_row_max = 0
        for i in row:
            if i == 0:
                if len_row > len_row_max:
                    len_row_max = len_row
                len_row = 0
            else:
                len_row += 1
        if len_row > len_row_max:
            my_list.append(len_row)
        else:
            my_list.append(len_row_max)
    my_list_max_vertical = max(my_list)
    index_my_list = my_list.index(my_list_max_vertical)
    list_shot_2 = cnt_1[index_my_list: index_my_list + 1]
    if my_list_max_horizont > my_list_max_vertical:
        list_shot = list_shot_1
    else:
        list_shot = list_shot_2
    len_row = 0
    len_row_max = 0
    list_row = []
    list_row_1 = []
    for i in list_shot[0]:
        if i == 0:
            if len_row > len_row_max:
                len_row_max = len_row
                list_row_1 = list_row.copy()
            len_row = 0
            list_row = []
        else:
            len_row += 1
            list_row.append(i)
    if len_row > len_row_max:
        list_row_1 = list_row.copy()
    cell_number = list_row_1[len(list_row_1) // 2]
    if my_list_max_horizont == my_list_max_vertical == 1:
        flag_strategy_4 = True
        flag_strategy_3 = False
    return cell_number


def enemy_shot(screen):
    global cell, cell_2, flag_sound, flag_game, flag_enemy_victory, flag_my_shot_injured
    global flag_my_shot, flag_enemy_shot
    global list_my_ship, list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1,\
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4,\
        list_killed_my_ships, list_injured_my_ships, list_enemy_shot, list_killed_enemy_ships
    global flag_strategy_0, flag_strategy_1, flag_strategy_2, flag_strategy_3, flag_strategy_4
    one_list = []
    cell_number = 0
    if flag_enemy_shot:
        if not flag_my_shot_injured:
            if not flag_strategy_0 and not flag_strategy_1 and not flag_strategy_2 and not flag_strategy_3 \
                    and not flag_strategy_4:
                n = random.randint(0, 2)
                if n == 0:
                    flag_strategy_0 = True
                elif n == 1:
                    flag_strategy_1 = True
                elif n == 2:
                    flag_strategy_2 = True
            if flag_strategy_0:
                one_list = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]
            elif flag_strategy_1:
                one_list = [4, 8, 13, 17, 22, 26, 30, 31, 35, 39, 44, 48, 53, 57, 62, 66, 70,
                            71, 75, 79, 84, 88, 93, 97]
            elif flag_strategy_2:
                one_list = [4, 8, 13, 17, 21, 25, 29, 32, 36, 40, 44, 48, 53, 57, 61, 65, 69,
                            72, 76, 80, 84, 88, 93, 97]
            if len(list(set(one_list) - set(list_enemy_shot)
                        - set(list_killed_my_ships) - set(list_injured_my_ships))) > 0:
                cell_number = random.choice(list(set(one_list) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
            elif not flag_strategy_3 and len(list(set(one_list) - set(list_enemy_shot)
                                                  - set(list_killed_my_ships) - set(list_injured_my_ships))) == 0:
                flag_strategy_0 = False
                flag_strategy_1 = False
                flag_strategy_2 = False
                flag_strategy_3 = True
                cell_number = strategy_3()
            elif flag_strategy_3:
                cell_number = strategy_3()
            if flag_strategy_4:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
            x_start = cell[cell_number][0]
            y_start = cell[cell_number][2]
        else:
            if len(list_injured_my_ships) == 1:
                tmp = generator(list_injured_my_ships[0], 2)
                cell_number = random.choice(list(set(tmp) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][2]
            elif len(list_injured_my_ships) == 2:
                tmp = generator(list_injured_my_ships[0], 3)
                tmp_1 = reduction(list_injured_my_ships, tmp, 3)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][2]
            elif len(list_injured_my_ships) == 3:
                tmp = generator(list_injured_my_ships[0], 4)
                tmp_1 = reduction(list_injured_my_ships, tmp, 4)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][2]
            else:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][2]
        if flag_sound:
            pygame.mixer.music.play()
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 20, 5)
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start - 15), (x_start + 16, y_start + 8), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start + 24), (x_start + 16, y_start + 47), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start - 15, y_start + 16), (x_start + 8, y_start + 16), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 24, y_start + 16), (x_start + 47, y_start + 16), 5)
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(800)
        smail = pygame.image.load('взрыв.png')
        screen.blit(smail, (x_start - 10, y_start - 5))
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(1000)
        if cell_number in list_my_ship:
            flag_my_shot_injured = True
            list_injured_my_ships.append(cell_number)
            if len(list(set(list_my_battleship) - set(list_injured_my_ships))) == 0:
                for j in list_my_battleship:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_battleship)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_cruiser_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_cruiser_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_destroyer_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_destroyer_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_destroyer_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_boat_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_boat_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_boat_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
            if len(list(set(list_my_boat_4) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_4:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_4)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                list_injured_my_ships = []
        else:
            list_enemy_shot.append(cell_number)
            flag_my_shot = True
            flag_enemy_shot = False
        pygame.Surface.fill(screen, (255, 250, 250), rect=(90, 240, 350, 350))
        frame(screen)
        grid(screen, 120, 421, 270, 571)
        for i in list_my_ship:
            x_start = cell[i][0]
            y_start = cell[i][2]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        for i in list_injured_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][2]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        list_killed_my_ships = list(set(list_killed_my_ships))
        for i in list_killed_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][2]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_enemy_shot:
            x_start = cell[i][0]
            y_start = cell[i][2]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
    pygame.display.update((90, 240, 350, 350))
    if len(list_killed_my_ships) == 20:
        flag_enemy_victory = True
        flag_game = False
        list_victory_enemy = list(set(list_enemy_ships) - set(list_killed_enemy_ships) - set(list_injured_enemy_ships))
        for i in list_victory_enemy:
            x_start = cell_2[i][0]
            y_start = cell_2[i][2]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        pygame.display.update()
        pygame.time.wait(3000)


def victory(screen):
    global flag_my_victory, flag_enemy_victory
    pygame.Surface.fill(screen, (255, 250, 250))
    """функция победа, тетрадный лист и основная надпись"""
    global flag_sound
    if flag_sound:
        pygame.Surface.fill(screen, (255, 250, 250), rect=(885, 90, 60, 60))
        smail_def = pygame.image.load('звук.png')
        screen.blit(smail_def, (890, 90))
    if not flag_sound:
        pygame.Surface.fill(screen, (255, 250, 250), rect=(885, 90, 60, 60))
        smail_def = pygame.image.load('звук.png')
        screen.blit(smail_def, (890, 90))
        pygame.draw.line(screen, (255, 0, 0), (890, 90), (940, 140), 5)
        pygame.draw.line(screen, (255, 0, 0), (940, 90), (890, 140), 5)
    for i in range(0, 1020, 30):
        pygame.draw.line(screen, (106, 90, 205), (i, 0), (i, 700), 1)
    for i in range(0, 700, 30):
        pygame.draw.line(screen, (106, 90, 205), (0, i), (1020, i), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (1020, 0), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 700), 5)
    pygame.draw.line(screen, (0, 0, 0), (1019, 0), (1019, 700), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 698), (1020, 698), 3)
    smail_def = pygame.image.load('осн.надпись.png')
    screen.blit(smail_def, (140, 20))
    smail_def = pygame.image.load('надпись.png')
    screen.blit(smail_def, (280, 655))
    if flag_my_victory:
        smail = pygame.image.load('smail4.png')
        screen.blit(smail, (370, 200))
        text(screen, 60, 'ТЫ ВЫИГРАЛ !!!', (225, 430), (255, 0, 0))
    elif flag_enemy_victory:
        smail = pygame.image.load('smail3.png')
        screen.blit(smail, (380, 200))
        text(screen, 60, 'ТЫ ПРОИГРАЛ !!!', (220, 430), (255, 0, 0))
    button(screen, 250, 560, 'Новая игра', 10, 5)
    button(screen, 630, 560, 'Выход', 33, 5)
    smail = pygame.image.load('victory.png')
    screen.blit(smail, (700, 200))
    smail = pygame.image.load('взрыв_2.png').convert_alpha()
    smail = pygame.transform.scale(smail, (50, 50))
    screen.blit(smail, (120, 300))
    pygame.display.update()
    pygame.time.wait(150)
    smail = pygame.image.load('взрыв_2.png').convert_alpha()
    smail = pygame.transform.scale(smail, (100, 100))
    screen.blit(smail, (105, 285))
    pygame.display.update()
    pygame.time.wait(150)
    smail = pygame.image.load('взрыв_2.png').convert_alpha()
    smail = pygame.transform.scale(smail, (200, 200))
    screen.blit(smail, (60, 220))
    pygame.display.update()
    pygame.time.wait(200)
    smail = pygame.image.load('go.png')
    screen.blit(smail, (90, 260))
    pygame.display.update()
    pygame.time.wait(500)


def work():
    global list_my_ship, list_enemy_ships, list_ban_cell, list_probability_ship, list_battleship, list_chek
    global flag_battleship, flag_cruiser_1, flag_cruiser_2, flag_destroyer_1, flag_destroyer_2, flag_destroyer_3
    global flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global flag_my_shot, flag_enemy_shot, flag_sound, flag_game, flag_my_victory, flag_automatic
    global list_enemy_battleship, list_enemy_cruiser_1, list_enemy_cruiser_2, list_enemy_destroyer_1,\
        list_enemy_destroyer_2, list_enemy_destroyer_3, list_enemy_boat_1,\
        list_enemy_boat_2, list_enemy_boat_3, list_enemy_boat_4,\
        list_killed_enemy_ships, list_injured_enemy_ships, list_my_shot
    global list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1,\
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4,\
        list_killed_my_ships, list_injured_my_ships, list_enemy_shot, flag_strategy_0, flag_strategy_1, \
        flag_strategy_2, flag_strategy_3, flag_strategy_4
    pygame.init()
    pygame.display.set_caption(' МОРСКОЙ БОЙ ')
    screen = pygame.display.set_mode((1020, 700))
    pygame.display.set_icon(pygame.image.load('sea_battle.png'))
    pygame.Surface.fill(screen, (255, 250, 250))
    frame(screen)
    grid(screen, 120, 421, 270, 571)
    placement_ships(screen)
    button(screen, 450, 590, 'Сброс', 38, 5)
    button(screen, 635, 590, 'Расставить', 13, 5)
    button(screen, 820, 590, 'Дальше', 30, 5)
    pygame.display.update()
    pygame.mixer.music.load('click.mp3')
    flag_main_menu = True
    flag_choice_battleship = False
    flag_choice_cruiser_1 = False
    flag_choice_cruiser_2 = False
    flag_choice_destroyer_1 = False
    flag_choice_destroyer_2 = False
    flag_choice_destroyer_3 = False
    flag_choice_boat_1 = False
    flag_choice_boat_2 = False
    flag_choice_boat_3 = False
    flag_choice_boat_4 = False
    flag_quit = False
    cell_number = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos_mouse = event.pos
                    if 450 <= pos_mouse[0] <= 590 and 590 <= pos_mouse[1] <= 630 and flag_main_menu:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(450, 590, 140, 40))
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.display.update((450, 590, 140, 40))
                        pygame.time.wait(300)
                        button(screen, 450, 590, 'Сброс', 38, 5)
                        pygame.display.update((450, 590, 140, 40))
                        list_my_ship = []  # список моих кораблей
                        list_ban_cell = []  # список запрещенных клеток для установки корабля
                        list_battleship = []  # список координат установки линкора
                        list_probability_ship = []  # список вариатов установки корабля
                        list_my_battleship = []  # координаты моего линкора
                        list_my_cruiser_1 = []  # координаты моего крейсера_1
                        list_my_cruiser_2 = []  # координаты моего крейсера_2
                        list_my_destroyer_1 = []  # координаты моего эсминца_1
                        list_my_destroyer_2 = []  # координаты моего эсминца_2
                        list_my_destroyer_3 = []  # координаты моего эсминца_3
                        list_my_boat_1 = []  # координаты моего катера_1
                        list_my_boat_2 = []  # координаты моего катера_2
                        list_my_boat_3 = []  # координаты моего катера_3
                        list_my_boat_4 = []  # координаты моего катера_4
                        flag_battleship = False  # установлен ли линкор : True - да , False - нет
                        flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
                        flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
                        flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
                        flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
                        flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
                        flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
                        flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
                        flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
                        flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                        flag_quit = False
                        flag_automatic = False
                        list_chek = []
                        cell_number = 0
                        delete_ship(screen)
                    elif 635 <= pos_mouse[0] <= 775 and 590 <= pos_mouse[1] <= 630 and flag_main_menu:
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(635, 590, 140, 40))
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.display.update((635, 590, 140, 40))
                        pygame.time.wait(300)
                        button(screen, 635, 590, 'Расставить', 13, 5)
                        pygame.display.update((635, 590, 140, 40))
                        list_my_ship = []  # список моих кораблей
                        list_ban_cell = []  # список запрещенных клеток для установки корабля
                        list_battleship = []  # список координат установки линкора
                        list_probability_ship = []  # список вариатов установки корабля
                        list_my_battleship = []  # координаты моего линкора
                        list_my_cruiser_1 = []  # координаты моего крейсера_1
                        list_my_cruiser_2 = []  # координаты моего крейсера_2
                        list_my_destroyer_1 = []  # координаты моего эсминца_1
                        list_my_destroyer_2 = []  # координаты моего эсминца_2
                        list_my_destroyer_3 = []  # координаты моего эсминца_3
                        list_my_boat_1 = []  # координаты моего катера_1
                        list_my_boat_2 = []  # координаты моего катера_2
                        list_my_boat_3 = []  # координаты моего катера_3
                        list_my_boat_4 = []  # координаты моего катера_4
                        flag_battleship = False  # установлен ли линкор : True - да , False - нет
                        flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
                        flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
                        flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
                        flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
                        flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
                        flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
                        flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
                        flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
                        flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                        flag_quit = False
                        flag_automatic = True
                        cell_number = 0
                        list_chek = []
                        delete_ship(screen)
                        automatic_placement_ships(screen)
                    elif (820 <= pos_mouse[0] <= 960 and 590 <= pos_mouse[1] <= 630 and flag_main_menu
                          and len(list_my_ship) == 20 and flag_battleship and flag_cruiser_1 and flag_cruiser_2
                          and flag_destroyer_1 and flag_destroyer_2 and flag_destroyer_3
                          and flag_boat_1 and flag_boat_2 and flag_boat_3 and flag_boat_4):
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(820, 590, 140, 40))
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.display.update((820, 590, 140, 40))
                        pygame.time.wait(300)
                        button(screen, 820, 590, 'Дальше', 30, 5)
                        pygame.display.update((820, 590, 140, 40))
                        list_enemy_ships = []
                        list_ban_cell = []
                        list_battleship = []
                        list_probability_ship = []
                        automatic_placement_enemy_ships()
                        pygame.Surface.fill(screen, (255, 250, 250), rect=(440, 180, 560, 460))
                        frame(screen)
                        grid(screen, 600, 901, 270, 571)
                        smail_def = pygame.image.load('количество ходов.png')
                        screen.blit(smail_def, (570, 590))
                        smail_def = pygame.image.load('вражеский флот.png')
                        screen.blit(smail_def, (610, 170))
                        pygame.display.update((440, 180, 560, 460))
                        flag_main_menu = False
                        flag_game = True
                        flag_my_shot = True
                        flag_enemy_shot = False
                        flag_quit = False
                        cell_number = 0
                        pygame.mixer.music.load('shot.mp3')
                        number_shots_remaining(screen)
                    elif 440 <= pos_mouse[0] <= 700 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        """выбор установки линкора"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_battleship:
                            flag_choice_battleship = True
                        input_box = pygame.Rect(440, 260, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((440, 260, 290, 50))
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 440 <= pos_mouse[0] <= 700 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        """выбор установки крейсера 1"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_cruiser_1:
                            flag_choice_cruiser_1 = True
                        input_box = pygame.Rect(440, 320, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((440, 320, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 440 <= pos_mouse[0] <= 700 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        """выбор установки крейсера 2"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_cruiser_2:
                            flag_choice_cruiser_2 = True
                        input_box = pygame.Rect(440, 380, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((440, 380, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 440 <= pos_mouse[0] <= 700 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        """выбор установки эсминца 1"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_destroyer_1:
                            flag_choice_destroyer_1 = True
                        input_box = pygame.Rect(440, 440, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((440, 440, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 440 <= pos_mouse[0] <= 700 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        """выбор установки эсминца 2"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_destroyer_2:
                            flag_choice_destroyer_2 = True
                        input_box = pygame.Rect(440, 500, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((440, 500, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 740 <= pos_mouse[0] <= 970 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        """выбор установки эсминца 3"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_destroyer_3:
                            flag_choice_destroyer_3 = True
                        input_box = pygame.Rect(740, 260, 260, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((740, 260, 260, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 740 <= pos_mouse[0] <= 970 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        """выбор установки катера 1"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_boat_1:
                            flag_choice_boat_1 = True
                        input_box = pygame.Rect(740, 320, 260, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((740, 320, 260, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 740 <= pos_mouse[0] <= 970 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        """выбор установки катера 2"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_boat_2:
                            flag_choice_boat_2 = True
                        input_box = pygame.Rect(740, 380, 260, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((740, 380, 260, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 740 <= pos_mouse[0] <= 970 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        """выбор установки катера 3"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_boat_3:
                            flag_choice_boat_3 = True
                        input_box = pygame.Rect(740, 440, 260, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((740, 440, 260, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_4 = False
                    elif 740 <= pos_mouse[0] <= 970 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        """выбор установки катера 4"""
                        grout(screen)
                        cell_number = 0
                        if flag_sound:
                            pygame.mixer.music.play()
                        if len(list_battleship) == 0 and not flag_boat_4:
                            flag_choice_boat_4 = True
                        input_box = pygame.Rect(740, 500, 260, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((740, 500, 260, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                    elif 890 <= pos_mouse[0] <= 940 and 90 <= pos_mouse[1] <= 140:
                        if flag_sound:
                            flag_sound = False
                            frame(screen)
                        elif not flag_sound:
                            flag_sound = True
                            frame(screen)
                    elif 600 <= pos_mouse[0] <= 740 and 560 <= pos_mouse[1] <= 600 and flag_quit:
                        """Кнопка "Выход" """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(630, 560, 140, 40))
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.display.update((630, 560, 140, 40))
                        pygame.time.wait(300)
                        button(screen, 630, 560, 'Выход', 33, 5)
                        pygame.display.update((630, 560, 140, 40))
                        pygame.quit()
                        sys.exit()
                    elif 250 <= pos_mouse[0] <= 390 and 560 <= pos_mouse[1] <= 600 and flag_quit:
                        """Кнопка "Новая игра" """
                        pygame.Surface.fill(screen, (0, 0, 0), rect=(250, 560, 140, 40))
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.display.update((250, 560, 140, 40))
                        pygame.time.wait(300)
                        button(screen, 250, 560, 'Новая игра', 10, 5)
                        pygame.display.update((250, 560, 140, 40))
                        pygame.Surface.fill(screen, (255, 250, 250))
                        frame(screen)
                        grid(screen, 120, 421, 270, 571)
                        placement_ships(screen)
                        button(screen, 450, 590, 'Сброс', 38, 5)
                        button(screen, 635, 590, 'Расставить', 13, 5)
                        button(screen, 820, 590, 'Дальше', 30, 5)
                        pygame.display.update()
                        pygame.mixer.music.load('click.mp3')
                        flag_main_menu = True
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                        flag_quit = False
                        flag_strategy_0 = False  # стратегия стрельбы 0
                        flag_strategy_1 = False  # стратегия стрельбы 1
                        flag_strategy_2 = False  # стратегия стрельбы 2
                        flag_strategy_3 = False  # стратегия стрельбы 3
                        flag_strategy_4 = False  # стратегия стрельбы 4
                        cell_number = 0
                        list_my_ship = []  # список моих кораблей
                        list_ban_cell = []  # список запрещенных клеток для установки корабля
                        list_battleship = []  # список координат установки корабля
                        list_probability_ship = []  # список вариатов установки корабля
                        list_enemy_ships = []  # список вражеских кораблей
                        list_enemy_battleship = []  # координаты вражеского линкора
                        list_enemy_cruiser_1 = []  # координаты вражеского крейсера_1
                        list_enemy_cruiser_2 = []  # координаты вражеского крейсера_2
                        list_enemy_destroyer_1 = []  # координаты вражеского эсминца_1
                        list_enemy_destroyer_2 = []  # координаты вражеского эсминца_2
                        list_enemy_destroyer_3 = []  # координаты вражеского эсминца_3
                        list_enemy_boat_1 = []  # координаты вражеского катера_1
                        list_enemy_boat_2 = []  # координаты вражеского катера_2
                        list_enemy_boat_3 = []  # координаты вражеского катера_3
                        list_enemy_boat_4 = []  # координаты вражеского катера_4
                        list_killed_enemy_ships = []  # список вражеских убитых кораблей
                        list_injured_enemy_ships = []  # список раненых вражеских кораблей
                        list_my_shot = []  # список моих выстрелов
                        list_my_ship = []  # список моих кораблей
                        list_my_battleship = []  # координаты моего линкора
                        list_my_cruiser_1 = []  # координаты моего крейсера_1
                        list_my_cruiser_2 = []  # координаты моего крейсера_2
                        list_my_destroyer_1 = []  # координаты моего эсминца_1
                        list_my_destroyer_2 = []  # координаты моего эсминца_2
                        list_my_destroyer_3 = []  # координаты моего эсминца_3
                        list_my_boat_1 = []  # координаты моего катера_1
                        list_my_boat_2 = []  # координаты моего катера_2
                        list_my_boat_3 = []  # координаты моего катера_3
                        list_my_boat_4 = []  # координаты моего катера_4
                        list_killed_my_ships = []  # список моих убитых кораблей
                        list_injured_my_ships = []  # список моих раненых кораблей
                        list_enemy_shot = []
                        list_chek = []
                        flag_battleship = False  # установлен ли линкор : True - да , False - нет
                        flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
                        flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
                        flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
                        flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
                        flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
                        flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
                        flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
                        flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
                        flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
                        flag_my_shot = False  # мой выстрел
                        flag_enemy_shot = False  # вражеский выстрел
                        flag_game = False  # игра
                        flag_my_victory = False  # я победил
                    elif 120 <= pos_mouse[0] <= 150 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 1
                    elif 150 <= pos_mouse[0] <= 180 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 2
                    elif 180 <= pos_mouse[0] <= 210 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 3
                    elif 210 <= pos_mouse[0] <= 240 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 4
                    elif 240 <= pos_mouse[0] <= 270 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 5
                    elif 270 <= pos_mouse[0] <= 300 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 6
                    elif 300 <= pos_mouse[0] <= 330 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 7
                    elif 330 <= pos_mouse[0] <= 360 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 8
                    elif 360 <= pos_mouse[0] <= 390 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 9
                    elif 390 <= pos_mouse[0] <= 420 and 270 <= pos_mouse[1] <= 300 and flag_main_menu:
                        cell_number = 10
                    elif 120 <= pos_mouse[0] <= 150 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 11
                    elif 150 <= pos_mouse[0] <= 180 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 12
                    elif 180 <= pos_mouse[0] <= 210 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 13
                    elif 210 <= pos_mouse[0] <= 240 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 14
                    elif 240 <= pos_mouse[0] <= 270 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 15
                    elif 270 <= pos_mouse[0] <= 300 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 16
                    elif 300 <= pos_mouse[0] <= 330 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 17
                    elif 330 <= pos_mouse[0] <= 360 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 18
                    elif 360 <= pos_mouse[0] <= 390 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 19
                    elif 390 <= pos_mouse[0] <= 420 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 20
                    elif 120 <= pos_mouse[0] <= 150 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 21
                    elif 150 <= pos_mouse[0] <= 180 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 22
                    elif 180 <= pos_mouse[0] <= 210 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 23
                    elif 210 <= pos_mouse[0] <= 240 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 24
                    elif 240 <= pos_mouse[0] <= 270 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 25
                    elif 270 <= pos_mouse[0] <= 300 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 26
                    elif 300 <= pos_mouse[0] <= 330 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 27
                    elif 330 <= pos_mouse[0] <= 360 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 28
                    elif 360 <= pos_mouse[0] <= 390 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 29
                    elif 390 <= pos_mouse[0] <= 420 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 30
                    elif 120 <= pos_mouse[0] <= 150 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 31
                    elif 150 <= pos_mouse[0] <= 180 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 32
                    elif 180 <= pos_mouse[0] <= 210 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 33
                    elif 210 <= pos_mouse[0] <= 240 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 34
                    elif 240 <= pos_mouse[0] <= 270 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 35
                    elif 270 <= pos_mouse[0] <= 300 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 36
                    elif 300 <= pos_mouse[0] <= 330 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 37
                    elif 330 <= pos_mouse[0] <= 360 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 38
                    elif 360 <= pos_mouse[0] <= 390 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 39
                    elif 390 <= pos_mouse[0] <= 420 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 40
                    elif 120 <= pos_mouse[0] <= 150 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 41
                    elif 150 <= pos_mouse[0] <= 180 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 42
                    elif 180 <= pos_mouse[0] <= 210 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 43
                    elif 210 <= pos_mouse[0] <= 240 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 44
                    elif 240 <= pos_mouse[0] <= 270 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 45
                    elif 270 <= pos_mouse[0] <= 300 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 46
                    elif 300 <= pos_mouse[0] <= 330 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 47
                    elif 330 <= pos_mouse[0] <= 360 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 48
                    elif 360 <= pos_mouse[0] <= 390 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 49
                    elif 390 <= pos_mouse[0] <= 420 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 50
                    elif 120 <= pos_mouse[0] <= 150 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 51
                    elif 150 <= pos_mouse[0] <= 180 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 52
                    elif 180 <= pos_mouse[0] <= 210 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 53
                    elif 210 <= pos_mouse[0] <= 240 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 54
                    elif 240 <= pos_mouse[0] <= 270 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 55
                    elif 270 <= pos_mouse[0] <= 300 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 56
                    elif 300 <= pos_mouse[0] <= 330 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 57
                    elif 330 <= pos_mouse[0] <= 360 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 58
                    elif 360 <= pos_mouse[0] <= 390 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 59
                    elif 390 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 60
                    elif 120 <= pos_mouse[0] <= 150 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 61
                    elif 150 <= pos_mouse[0] <= 180 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 62
                    elif 180 <= pos_mouse[0] <= 210 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 63
                    elif 210 <= pos_mouse[0] <= 240 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 64
                    elif 240 <= pos_mouse[0] <= 270 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 65
                    elif 270 <= pos_mouse[0] <= 300 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 66
                    elif 300 <= pos_mouse[0] <= 330 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 67
                    elif 330 <= pos_mouse[0] <= 360 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 68
                    elif 360 <= pos_mouse[0] <= 390 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 69
                    elif 390 <= pos_mouse[0] <= 420 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 70
                    elif 120 <= pos_mouse[0] <= 150 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 71
                    elif 150 <= pos_mouse[0] <= 180 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 72
                    elif 180 <= pos_mouse[0] <= 210 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 73
                    elif 210 <= pos_mouse[0] <= 240 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 74
                    elif 240 <= pos_mouse[0] <= 270 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 75
                    elif 270 <= pos_mouse[0] <= 300 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 76
                    elif 300 <= pos_mouse[0] <= 330 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 77
                    elif 330 <= pos_mouse[0] <= 360 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 78
                    elif 360 <= pos_mouse[0] <= 390 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 79
                    elif 390 <= pos_mouse[0] <= 420 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 80
                    elif 120 <= pos_mouse[0] <= 150 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 81
                    elif 150 <= pos_mouse[0] <= 180 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 82
                    elif 180 <= pos_mouse[0] <= 210 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 83
                    elif 210 <= pos_mouse[0] <= 240 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 84
                    elif 240 <= pos_mouse[0] <= 270 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 85
                    elif 270 <= pos_mouse[0] <= 300 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 86
                    elif 300 <= pos_mouse[0] <= 330 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 87
                    elif 330 <= pos_mouse[0] <= 360 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 88
                    elif 360 <= pos_mouse[0] <= 390 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 89
                    elif 390 <= pos_mouse[0] <= 420 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 90
                    elif 120 <= pos_mouse[0] <= 150 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 91
                    elif 150 <= pos_mouse[0] <= 180 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 92
                    elif 180 <= pos_mouse[0] <= 210 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 93
                    elif 210 <= pos_mouse[0] <= 240 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 94
                    elif 240 <= pos_mouse[0] <= 270 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 95
                    elif 270 <= pos_mouse[0] <= 300 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 96
                    elif 300 <= pos_mouse[0] <= 330 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 97
                    elif 330 <= pos_mouse[0] <= 360 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 98
                    elif 360 <= pos_mouse[0] <= 390 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 99
                    elif 390 <= pos_mouse[0] <= 420 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 100
                    elif 600 <= pos_mouse[0] <= 630 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 1
                    elif 630 <= pos_mouse[0] <= 660 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 2
                    elif 660 <= pos_mouse[0] <= 690 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 3
                    elif 690 <= pos_mouse[0] <= 720 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 4
                    elif 720 <= pos_mouse[0] <= 750 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 5
                    elif 750 <= pos_mouse[0] <= 780 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 6
                    elif 780 <= pos_mouse[0] <= 810 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 7
                    elif 810 <= pos_mouse[0] <= 840 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 8
                    elif 840 <= pos_mouse[0] <= 870 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 9
                    elif 870 <= pos_mouse[0] <= 900 and 270 <= pos_mouse[1] <= 300 and flag_game and flag_my_shot:
                        cell_number = 10
                    elif 600 <= pos_mouse[0] <= 630 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 11
                    elif 630 <= pos_mouse[0] <= 660 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 12
                    elif 660 <= pos_mouse[0] <= 690 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 13
                    elif 690 <= pos_mouse[0] <= 720 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 14
                    elif 720 <= pos_mouse[0] <= 750 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 15
                    elif 750 <= pos_mouse[0] <= 780 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 16
                    elif 780 <= pos_mouse[0] <= 810 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 17
                    elif 810 <= pos_mouse[0] <= 840 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 18
                    elif 840 <= pos_mouse[0] <= 870 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 19
                    elif 870 <= pos_mouse[0] <= 900 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 20
                    elif 600 <= pos_mouse[0] <= 630 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 21
                    elif 630 <= pos_mouse[0] <= 660 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 22
                    elif 660 <= pos_mouse[0] <= 690 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 23
                    elif 690 <= pos_mouse[0] <= 720 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 24
                    elif 720 <= pos_mouse[0] <= 750 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 25
                    elif 750 <= pos_mouse[0] <= 780 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 26
                    elif 780 <= pos_mouse[0] <= 810 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 27
                    elif 810 <= pos_mouse[0] <= 840 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 28
                    elif 840 <= pos_mouse[0] <= 870 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 29
                    elif 870 <= pos_mouse[0] <= 900 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 30
                    elif 600 <= pos_mouse[0] <= 630 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 31
                    elif 630 <= pos_mouse[0] <= 660 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 32
                    elif 660 <= pos_mouse[0] <= 690 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 33
                    elif 690 <= pos_mouse[0] <= 720 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 34
                    elif 720 <= pos_mouse[0] <= 750 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 35
                    elif 750 <= pos_mouse[0] <= 780 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 36
                    elif 780 <= pos_mouse[0] <= 810 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 37
                    elif 810 <= pos_mouse[0] <= 840 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 38
                    elif 840 <= pos_mouse[0] <= 870 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 39
                    elif 870 <= pos_mouse[0] <= 900 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 40
                    elif 600 <= pos_mouse[0] <= 630 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 41
                    elif 630 <= pos_mouse[0] <= 660 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 42
                    elif 660 <= pos_mouse[0] <= 690 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 43
                    elif 690 <= pos_mouse[0] <= 720 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 44
                    elif 720 <= pos_mouse[0] <= 750 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 45
                    elif 750 <= pos_mouse[0] <= 780 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 46
                    elif 780 <= pos_mouse[0] <= 810 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 47
                    elif 810 <= pos_mouse[0] <= 840 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 48
                    elif 840 <= pos_mouse[0] <= 870 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 49
                    elif 870 <= pos_mouse[0] <= 900 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 50
                    elif 600 <= pos_mouse[0] <= 630 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 51
                    elif 630 <= pos_mouse[0] <= 660 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 52
                    elif 660 <= pos_mouse[0] <= 690 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 53
                    elif 690 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 54
                    elif 720 <= pos_mouse[0] <= 750 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 55
                    elif 750 <= pos_mouse[0] <= 780 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 56
                    elif 780 <= pos_mouse[0] <= 810 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 57
                    elif 810 <= pos_mouse[0] <= 840 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 58
                    elif 840 <= pos_mouse[0] <= 870 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 59
                    elif 870 <= pos_mouse[0] <= 900 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 60
                    elif 600 <= pos_mouse[0] <= 630 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 61
                    elif 630 <= pos_mouse[0] <= 660 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 62
                    elif 660 <= pos_mouse[0] <= 690 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 63
                    elif 690 <= pos_mouse[0] <= 720 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 64
                    elif 720 <= pos_mouse[0] <= 750 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 65
                    elif 750 <= pos_mouse[0] <= 780 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 66
                    elif 780 <= pos_mouse[0] <= 810 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 67
                    elif 810 <= pos_mouse[0] <= 840 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 68
                    elif 840 <= pos_mouse[0] <= 870 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 69
                    elif 870 <= pos_mouse[0] <= 900 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 70
                    elif 600 <= pos_mouse[0] <= 630 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 71
                    elif 630 <= pos_mouse[0] <= 660 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 72
                    elif 660 <= pos_mouse[0] <= 690 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 73
                    elif 690 <= pos_mouse[0] <= 720 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 74
                    elif 720 <= pos_mouse[0] <= 750 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 75
                    elif 750 <= pos_mouse[0] <= 780 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 76
                    elif 780 <= pos_mouse[0] <= 810 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 77
                    elif 810 <= pos_mouse[0] <= 840 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 78
                    elif 840 <= pos_mouse[0] <= 870 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 79
                    elif 870 <= pos_mouse[0] <= 900 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 80
                    elif 600 <= pos_mouse[0] <= 630 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 81
                    elif 630 <= pos_mouse[0] <= 660 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 82
                    elif 660 <= pos_mouse[0] <= 690 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 83
                    elif 690 <= pos_mouse[0] <= 720 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 84
                    elif 720 <= pos_mouse[0] <= 750 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 85
                    elif 750 <= pos_mouse[0] <= 780 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 86
                    elif 780 <= pos_mouse[0] <= 810 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 87
                    elif 810 <= pos_mouse[0] <= 840 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 88
                    elif 840 <= pos_mouse[0] <= 870 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 89
                    elif 870 <= pos_mouse[0] <= 900 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 90
                    elif 600 <= pos_mouse[0] <= 630 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 91
                    elif 630 <= pos_mouse[0] <= 660 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 92
                    elif 660 <= pos_mouse[0] <= 690 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 93
                    elif 690 <= pos_mouse[0] <= 720 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 94
                    elif 720 <= pos_mouse[0] <= 750 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 95
                    elif 750 <= pos_mouse[0] <= 780 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 96
                    elif 780 <= pos_mouse[0] <= 810 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 97
                    elif 810 <= pos_mouse[0] <= 840 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 98
                    elif 840 <= pos_mouse[0] <= 870 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 99
                    elif 870 <= pos_mouse[0] <= 900 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 100
                    if flag_main_menu and flag_choice_battleship and 0 < cell_number < 101 and not flag_battleship:
                        choice_battleship(screen, cell_number)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_cruiser_1 and 0 < cell_number < 101 and not flag_cruiser_1:
                        choice_cruiser(screen, cell_number, 1)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_cruiser_2 and 0 < cell_number < 101 and not flag_cruiser_2:
                        choice_cruiser(screen, cell_number, 2)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_destroyer_1 and 0 < cell_number < 101 and not flag_destroyer_1:
                        choice_destroyer(screen, cell_number, 1)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_destroyer_2 and 0 < cell_number < 101 and not flag_destroyer_2:
                        choice_destroyer(screen, cell_number, 2)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_destroyer_3 and 0 < cell_number < 101 and not flag_destroyer_3:
                        choice_destroyer(screen, cell_number, 3)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_boat_1 and 0 < cell_number < 101 and not flag_boat_1:
                        choice_boat(screen, cell_number, 1)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_boat_2 and 0 < cell_number < 101 and not flag_boat_2:
                        choice_boat(screen, cell_number, 2)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_boat_3 and 0 < cell_number < 101 and not flag_boat_3:
                        choice_boat(screen, cell_number, 3)
                        if flag_sound:
                            pygame.mixer.music.play()
                    elif flag_main_menu and flag_choice_boat_4 and 0 < cell_number < 101 and not flag_boat_4:
                        choice_boat(screen, cell_number, 4)
                        if flag_sound:
                            pygame.mixer.music.play()
                    if flag_game and flag_my_shot and cell_number != 0:
                        my_shot(screen, cell_number)
                        number_shots_remaining(screen)
                        cell_number = 0
        if flag_game and flag_enemy_shot:
            enemy_shot(screen)
            number_shots_remaining(screen)
            cell_number = 0
        if not flag_game and not flag_main_menu:
            victory(screen)
            flag_quit = True
            pygame.mixer.music.load('click.mp3')


if __name__ == '__main__':
    cell = {1: [120, 150, 270, 300], 2: [150, 180, 270, 300], 3: [180, 210, 270, 300], 4: [210, 240, 270, 300],
            5: [240, 270, 270, 300], 6: [270, 300, 270, 300], 7: [300, 330, 270, 300], 8: [330, 360, 270, 300],
            9: [360, 390, 270, 300], 10: [390, 420, 270, 300], 11: [120, 150, 300, 330], 12: [150, 180, 300, 330],
            13: [180, 210, 300, 330], 14: [210, 240, 300, 330], 15: [240, 270, 300, 330], 16: [270, 300, 300, 330],
            17: [300, 330, 300, 330], 18: [330, 360, 300, 330], 19: [360, 390, 300, 330], 20: [390, 420, 300, 330],
            21: [120, 150, 330, 360], 22: [150, 180, 330, 360], 23: [180, 210, 330, 360], 24: [210, 240, 330, 360],
            25: [240, 270, 330, 360], 26: [270, 300, 330, 360], 27: [300, 330, 330, 360], 28: [330, 360, 330, 360],
            29: [360, 390, 330, 360], 30: [390, 420, 330, 360], 31: [120, 150, 360, 390], 32: [150, 180, 360, 390],
            33: [180, 210, 360, 390], 34: [210, 240, 360, 390], 35: [240, 270, 360, 390], 36: [270, 300, 360, 390],
            37: [300, 330, 360, 390], 38: [330, 360, 360, 390], 39: [360, 390, 360, 390], 40: [390, 420, 360, 390],
            41: [120, 150, 390, 420], 42: [150, 180, 390, 420], 43: [180, 210, 390, 420], 44: [210, 240, 390, 420],
            45: [240, 270, 390, 420], 46: [270, 300, 390, 420], 47: [300, 330, 390, 420], 48: [330, 360, 390, 420],
            49: [360, 390, 390, 420], 50: [390, 420, 390, 420], 51: [120, 150, 420, 450], 52: [150, 180, 420, 450],
            53: [180, 210, 420, 450], 54: [210, 240, 420, 450], 55: [240, 270, 420, 450], 56: [270, 300, 420, 450],
            57: [300, 330, 420, 450], 58: [330, 360, 420, 450], 59: [360, 390, 420, 450], 60: [390, 420, 420, 450],
            61: [120, 150, 450, 480], 62: [150, 180, 450, 480], 63: [180, 210, 450, 480], 64: [210, 240, 450, 480],
            65: [240, 270, 450, 480], 66: [270, 300, 450, 480], 67: [300, 330, 450, 480], 68: [330, 360, 450, 480],
            69: [360, 390, 450, 480], 70: [390, 420, 450, 480], 71: [120, 150, 480, 510], 72: [150, 180, 480, 510],
            73: [180, 210, 480, 510], 74: [210, 240, 480, 510], 75: [240, 270, 480, 510], 76: [270, 300, 480, 510],
            77: [300, 330, 480, 510], 78: [330, 360, 480, 510], 79: [360, 390, 480, 510], 80: [390, 420, 480, 510],
            81: [120, 150, 510, 540], 82: [150, 180, 510, 540], 83: [180, 210, 510, 540], 84: [210, 240, 510, 540],
            85: [240, 270, 510, 540], 86: [270, 300, 510, 540], 87: [300, 330, 510, 540], 88: [330, 360, 510, 540],
            89: [360, 390, 510, 540], 90: [390, 420, 510, 540], 91: [120, 150, 540, 570], 92: [150, 180, 540, 570],
            93: [180, 210, 540, 570], 94: [210, 240, 540, 570], 95: [240, 270, 540, 570], 96: [270, 300, 540, 570],
            97: [300, 330, 540, 570], 98: [330, 360, 540, 570], 99: [360, 390, 540, 570], 100: [390, 420, 540, 570]}
    cell_2 = {1: [600, 630, 270, 300], 2: [630, 660, 270, 300], 3: [660, 690, 270, 300], 4: [690, 720, 270, 300],
              5: [720, 750, 270, 300], 6: [750, 780, 270, 300], 7: [780, 810, 270, 300], 8: [810, 840, 270, 300],
              9: [840, 870, 270, 300], 10: [870, 900, 270, 300], 11: [600, 630, 300, 330], 12: [630, 660, 300, 330],
              13: [660, 690, 300, 330], 14: [690, 720, 300, 330], 15: [720, 750, 300, 330], 16: [750, 780, 300, 330],
              17: [780, 810, 300, 330], 18: [810, 840, 300, 330], 19: [840, 870, 300, 330], 20: [870, 900, 300, 330],
              21: [600, 630, 330, 360], 22: [630, 660, 330, 360], 23: [660, 690, 330, 360], 24: [690, 720, 330, 360],
              25: [720, 750, 330, 360], 26: [750, 780, 330, 360], 27: [780, 810, 330, 360], 28: [810, 840, 330, 360],
              29: [840, 870, 330, 360], 30: [870, 900, 330, 360], 31: [600, 630, 360, 390], 32: [630, 660, 360, 390],
              33: [660, 690, 360, 390], 34: [690, 720, 360, 390], 35: [720, 750, 360, 390], 36: [750, 780, 360, 390],
              37: [780, 810, 360, 390], 38: [810, 840, 360, 390], 39: [840, 870, 360, 390], 40: [870, 900, 360, 390],
              41: [600, 630, 390, 420], 42: [630, 660, 390, 420], 43: [660, 690, 390, 420], 44: [690, 720, 390, 420],
              45: [720, 750, 390, 420], 46: [750, 780, 390, 420], 47: [780, 810, 390, 420], 48: [810, 840, 390, 420],
              49: [840, 870, 390, 420], 50: [870, 900, 390, 420], 51: [600, 630, 420, 450], 52: [630, 660, 420, 450],
              53: [660, 690, 420, 450], 54: [690, 720, 420, 450], 55: [720, 750, 420, 450], 56: [750, 780, 420, 450],
              57: [780, 810, 420, 450], 58: [810, 840, 420, 450], 59: [840, 870, 420, 450], 60: [870, 900, 420, 450],
              61: [600, 630, 450, 480], 62: [630, 660, 450, 480], 63: [660, 690, 450, 480], 64: [690, 720, 450, 480],
              65: [720, 750, 450, 480], 66: [750, 780, 450, 480], 67: [780, 810, 450, 480], 68: [810, 840, 450, 480],
              69: [840, 870, 450, 480], 70: [870, 900, 450, 480], 71: [600, 630, 480, 510], 72: [630, 660, 480, 510],
              73: [660, 690, 480, 510], 74: [690, 720, 480, 510], 75: [720, 750, 480, 510], 76: [750, 780, 480, 510],
              77: [780, 810, 480, 510], 78: [810, 840, 480, 510], 79: [840, 870, 480, 510], 80: [870, 900, 480, 510],
              81: [600, 630, 510, 540], 82: [630, 660, 510, 540], 83: [660, 690, 510, 540], 84: [690, 720, 510, 540],
              85: [720, 750, 510, 540], 86: [750, 780, 510, 540], 87: [780, 810, 510, 540], 88: [810, 840, 510, 540],
              89: [840, 870, 510, 540], 90: [870, 900, 510, 540], 91: [600, 630, 540, 570], 92: [630, 660, 540, 570],
              93: [660, 690, 540, 570], 94: [690, 720, 540, 570], 95: [720, 750, 540, 570], 96: [750, 780, 540, 570],
              97: [780, 810, 540, 570], 98: [810, 840, 540, 570], 99: [840, 870, 540, 570], 100: [870, 900, 540, 570]}
    list_ban_cell = []  # список запрещенных клеток для установки корабля
    list_battleship = []  # список координат установки корабля
    list_probability_ship = []  # список вариатов установки корабля
    list_enemy_ships = []  # список вражеских кораблей
    list_enemy_battleship = []  # координаты вражеского линкора
    list_enemy_cruiser_1 = []  # координаты вражеского крейсера_1
    list_enemy_cruiser_2 = []  # координаты вражеского крейсера_2
    list_enemy_destroyer_1 = []  # координаты вражеского эсминца_1
    list_enemy_destroyer_2 = []  # координаты вражеского эсминца_2
    list_enemy_destroyer_3 = []  # координаты вражеского эсминца_3
    list_enemy_boat_1 = []  # координаты вражеского катера_1
    list_enemy_boat_2 = []  # координаты вражеского катера_2
    list_enemy_boat_3 = []  # координаты вражеского катера_3
    list_enemy_boat_4 = []  # координаты вражеского катера_4
    list_killed_enemy_ships = []  # список вражеских убитых кораблей
    list_injured_enemy_ships = []  # список раненых вражеских кораблей
    list_my_shot = []  # список моих выстрелов
    list_my_ship = []  # список моих кораблей
    list_my_battleship = []  # координаты моего линкора
    list_my_cruiser_1 = []  # координаты моего крейсера_1
    list_my_cruiser_2 = []  # координаты моего крейсера_2
    list_my_destroyer_1 = []  # координаты моего эсминца_1
    list_my_destroyer_2 = []  # координаты моего эсминца_2
    list_my_destroyer_3 = []  # координаты моего эсминца_3
    list_my_boat_1 = []  # координаты моего катера_1
    list_my_boat_2 = []  # координаты моего катера_2
    list_my_boat_3 = []  # координаты моего катера_3
    list_my_boat_4 = []  # координаты моего катера_4
    list_killed_my_ships = []  # список моих убитых кораблей
    list_injured_my_ships = []  # список моих раненых кораблей
    list_enemy_shot = []  # список вражеских выстрелов
    flag_battleship = False  # установлен ли линкор : True - да , False - нет
    flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
    flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
    flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
    flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
    flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
    flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
    flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
    flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
    flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
    flag_my_shot = False  # мой выстрел
    flag_enemy_shot = False  # вражеский выстрел
    flag_my_shot_injured = False  # мой корабль ранен
    flag_sound = True  # звук включен/выключен
    flag_game = False  # игра
    flag_my_victory = False  # я победил
    flag_enemy_victory = False  # победил противник
    flag_automatic = False  # автоматическая расстановка кораблей
    list_chek = []  # список галочек установленных кораблей
    flag_strategy_0 = False  # стратегия стрельбы 0
    flag_strategy_1 = False  # стратегия стрельбы 1
    flag_strategy_2 = False  # стратегия стрельбы 2
    flag_strategy_3 = False  # стратегия стрельбы 3
    flag_strategy_4 = False  # стратегия стрельбы 4
    work()
