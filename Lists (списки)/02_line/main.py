members = list(range(160, 178, 2))
members2 = list(range(162, 182, 3))
members.extend(members2)

print(f'Отсортированный список: {sorted(members)}')


