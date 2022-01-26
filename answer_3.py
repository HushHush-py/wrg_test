#На языке Python или С/С++, написать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
#Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным)

from random import randint
from time import perf_counter

a = [randint(-10**3, 10**3) for _ in range(2*10**3+1)]

def answer_sort(numbers: list):
    n = len(numbers)
    for i in range(1, n):
        elem = numbers[i]           # первый элемент из неотсортированной части списка
        if elem < numbers[0]:       # если он меньше первого элемента в отсортированной части
            del numbers[i]          #   то удаляем из неотсортированной части
            numbers.insert(elem, 0) #   и добавляем в начало отсортированной части
        elif elem > numbers[i - 1]: # если больше последнего элемента в отсортированной части
            continue                #   то не делаем ничего, он уже на своём месте
        else:                       # и только в этом случае начинаем перебирать отсортированную часть
            j = i
            while j >= 1 and numbers[j - 1] > elem:
                numbers[j] = numbers[j - 1]
                j -= 1
            numbers[j] = elem


t_start = perf_counter()
answer_sort(a)
t_stop = perf_counter()
print(f"Время выполнения answer_sort(): {t_stop-t_start:.4f} cек")
