numfile = open('numbers.txt', 'r')
res = 0
for i in numfile.read().split():
    res += int(i)
numfile.close()

resfile = open('answer.txt', 'w')
resfile.write(str(res))
resfile.close()

