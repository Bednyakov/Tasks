zen_file = open('zen.txt', 'r')

for i in zen_file.read().split('\n')[::-1]:
    print(i)

zen_file.close()
