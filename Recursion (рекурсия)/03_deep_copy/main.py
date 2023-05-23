import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
num = int(input('Количество сайтов: '))

def sitecopy(site, num):
    if num == 0:
        return
    site_copy = copy.deepcopy(site)
    product = input('Введите название продукта: ')
    site_copy['html']['head']['title'] = f'Куплю/продам {product} недорого'
    site_copy['html']['body']['h2'] = f'У нас самая низакая цена на {product}'
    print(site_copy)
    sitecopy(site, num - 1)

sitecopy(site, num)

#к сожалению не знаю, как вывести на экран весь словарь по блокам, как в примере







