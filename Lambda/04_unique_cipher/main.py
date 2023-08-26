from collections import Counter

def count_unique_characters(element: str) -> int:
    return sum(list(filter(lambda value: value == 1, Counter(element.lower()).values())))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)

if __name__ == '__main__':
    print("Количество уникальных символов в строке:", unique_count)
