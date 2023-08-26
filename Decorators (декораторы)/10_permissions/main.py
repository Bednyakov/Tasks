user_permissions = ['admin']

def check_permission(username: str):
    '''Функция для передачи аргумента декоратору'''
    def check_permission_decorator(function):
        '''Декоратор для проверки доступа к вызываемой функции'''
        def inner():
            try:
                if username not in user_permissions:
                    raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {function.__name__}')
                else:
                    result = function()
                    return result
            except PermissionError as exc:
                print(f'PermissionError: {exc}')
        return inner
    return check_permission_decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
