
nice_list = [5, 8, 9, 4, 2, 9, 1, 8]

def nicefunc(obj):
    if len(obj) <= 1:
        return obj
    fst_list = []
    mid_list = []
    scnd_list = []
    for i in obj:
        if i < obj[-1]:
            fst_list.append(i)
        elif i > obj[-1]:
            scnd_list.append(i)
        else:
            mid_list.append(i)
    return nicefunc(fst_list) + mid_list + nicefunc(scnd_list)

print(nicefunc(nice_list))

