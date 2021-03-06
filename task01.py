"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы."""

import random


def bubble_sort(array):
    '''Сортировка пузырьком'''

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

a = [random.randint(-100, 99) for i in range(10)]
print(f'Исходный массив:\t\t{a}\nОтсортированный массив:\t{bubble_sort(a)}')

# Исходный массив:		[-38, 80, -94, 47, 87, -42, 85, -99, -98, 26]
# Отсортированный массив:	[-99, -98, -94, -42, -38, 26, 47, 80, 85, 87]
