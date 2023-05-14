num_list = [i for i in range(10)]

new_list = [(num_list[i], num_list[i+1])
            for i in range(0, len(num_list), 2)
            if i != len(num_list)]

print(new_list)
