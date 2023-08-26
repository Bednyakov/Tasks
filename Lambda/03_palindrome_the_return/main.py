from collections import Counter

def can_be_poly(word: str) -> bool:
    '''Функция сравнивает остаток от деления длины слова
    с суммой остатка от деления полученных счетчиков букв'''
    return len(word) % 2 == sum(value % 2 for value in Counter(word).values())


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))


