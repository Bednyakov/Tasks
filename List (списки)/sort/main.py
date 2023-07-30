num_list = [1, 4, -3, 0, 10]
count = len(num_list)

for i in range(count):
    for j in range(count - 1, i - 1, -1):
        if num_list[j - 1] > num_list[j]:
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]

print(num_list)

