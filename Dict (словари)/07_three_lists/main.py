def interdif(array_1, array_2, array_3):
    interarray = (set(array_1) & set(array_2)) & set(array_3)
    diffarray = set(array_1) - (set(array_2) | set(array_3))

    inter_array = []
    for i in array_3:
        if i in array_2 and i in array_1 and i not in inter_array:
            inter_array.append(i)

    dif_array = []
    for i in array_1:
        if i not in array_3 and i not in array_2:
            dif_array.append(i)

    print('Задача 1 со множествами: ', *interarray)
    print('Задача 2 со множествами: ', *diffarray)
    print('Задача 1 без множеств: ', *inter_array)
    print('Задача 2 без множеств: ', *dif_array)

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

interdif(array_1, array_2, array_3)





