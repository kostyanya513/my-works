# TODO здесь писать код
def is_prime(variable, val):
    ratio = 0
    for i_index in range(2, (variable // 2) + 1):
        if variable % i_index == 0:
            ratio += 1
    if ratio == 0:
        return val

def crypto(string):
    return [values for index, values in enumerate(list(string)) if is_prime(index, values)]

print(crypto((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
