def tpl_sort(tpl):
    for i in tpl:
        if type(i) != int:
            return tpl
            break

    return tuple(sorted(tpl))




