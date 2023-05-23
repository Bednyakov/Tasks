
def nesum(obj, reslist=[]):
    for i in obj:
        if type(i) != int:
            nesum(i)
        else:
            reslist.append(i)
    sumnum = 0
    for i in reslist:
        sumnum += i
    return sumnum
