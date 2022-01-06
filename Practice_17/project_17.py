# На вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# Далее программа работает по следующему алгоритму:
# 1. Преобразование введённой последовательности в список
# 2. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# 3. Устанавливается номер позиции элемента, который меньше введенного числа, а следующий больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска.

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element):
    if array[0] == element:
        return 'Элемента меньше введенного числа - нет, позиция элемента равного числу: 1'
    elif array[0] > element:
        return 'Элемента меньше введенного числа - нет, позиция элемента больше числа: 1'
    elif array[-1] < element:
        return f'Позиция элемента меньше введенного числа: {len(array)}, элемента большего или равного числу - нет'

    left = 0
    right = len(array)-1

    def search(array, element, left, right):
        middle = (right+left) // 2
        if array[middle] < element and array[middle+1] >= element:
            return f'Позиция элемента меньше введенного числа: {middle+1}, Позиция элемента больше или равного числу: {middle+2}'
        elif array[middle] == element:
            return f'Позиция элемента меньше введенного числа: {middle}, Позиция элемента больше или равного числу: {middle+1}'
        elif element < array[middle]:
            return search(array, element, left, middle -1)
        else:
            return search(array, element, middle+1, right)
    return search(array, element, left, right)


sequence = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

sequence_sort = merge_sort(sequence)
number = int(input('Введите любое число: '))

print(f'\nОтсортированная последовательность: {sequence_sort}')
print(binary_search(sequence_sort, number))
