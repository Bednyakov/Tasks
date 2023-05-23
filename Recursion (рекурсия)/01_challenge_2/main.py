def recnum(num=int(input('Введите число: ')), start=1):
    print(start)
    if start == num:
        return num

    recnum(num, start + 1)

recnum()
