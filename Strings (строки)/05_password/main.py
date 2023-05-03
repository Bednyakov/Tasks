while True:
    password = input('Придумайте пароль: ')
    nums = []
    upletters = []

    if password.isalnum() == True:
        for i in password:
            if i.isdigit():
                nums.append(i)
            if i.isupper():
                upletters.append(i)
    if len(nums) >= 3 and len(upletters) >= 1 \
            and (len(nums) + len(upletters)) < len(password):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')




