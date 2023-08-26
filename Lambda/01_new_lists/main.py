from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

#good_floats: List[float] = [round((number ** 3), 3) for number in floats]
lambda_floats: List[float] = list(map(lambda number: round(number ** 3, 3), floats))

#good_names: List[str] = [name for name in names if len(name) >= 5]
lambda_names: List[str] = list(filter(lambda name: len(name) >= 5, names))

lambda_numbers: int = reduce(lambda number1, number2: number1 * number2, numbers)

if __name__ == '__main__':
    print(f'''
    {lambda_floats}
    {lambda_names}
    {lambda_numbers}
    ''')



