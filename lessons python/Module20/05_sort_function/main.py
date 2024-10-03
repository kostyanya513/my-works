def tpl_sort(string):
    for index in string:
        if not isinstance(index, int):
            return string
    return tuple(sorted(string))

tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))