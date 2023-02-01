"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def sum(count):
    if count == 1:
        return 1
    return sum(count-1) + count


n = 5
s = ''

print(f'для n = {n}')
if sum(n) == n*(n+1)/2:
    for i in range(1, n+1):
        s += str(i)
        if i < n:
            s += '+'
    print(f'{s} = {n}({n}+1)/2')
