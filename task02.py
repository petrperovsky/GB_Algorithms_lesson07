"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""

import random


# def merge_two_list(a, b):
#     '''Слияние двух сортированных списков'''
#
#     i = j = 0
#     c = []
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += a[i:]
#     while j < len(b):
#         c += b[j:]
#     return c


def merge_sort(a):
    '''Сортировка методом слияния'''

    if len(a) == 1:
        return a
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])

    i = j = 0
    c = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    if i < len(left):
        c += left[i:]
    if j < len(right):
        c += right[j:]
    return c

a = [random.randint(0, 49) for i in range(10)]
print(f'Исходный массив:\t\t{a}\nОтсортированный массив:\t{merge_sort(a)}')

# Исходный массив:		[40, 30, 23, 41, 7, 48, 25, 2, 44, 25]
# Отсортированный массив:	[2, 7, 23, 25, 25, 30, 40, 41, 44, 48]