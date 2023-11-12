"""Модуль для генерации числа"""
from random import randint

"""Названия"""
identificators = {
    1: 'Камень',
    2: 'Ножницы',
    3: 'Бумага'
}

"""Комбинации побед"""
combinations = {
    1: 2,
    2: 3,
    3: 1
}

pc_variant = randint(1, 3)
client_variant = int(input('Камень - 1, ножницы - 2, бумага - 3: '))

if pc_variant == client_variant:
    print('Ничья')
elif combinations[client_variant] == pc_variant:
    print(f'Вы выиграли. Компьютер - {identificators[pc_variant]}; Вы - {identificators[client_variant]}')
else:
    print(f'Вы проиграли. Компьютер - {identificators[pc_variant]}; Вы - {identificators[client_variant]}')
