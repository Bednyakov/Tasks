
a = 'abcd'
b = (10, 20, 30, 40)
notzip = ((a[i], b[i]) for i in range((len(a) + len(b)) // 2))


print(notzip)
for i in notzip:
    print(i)



