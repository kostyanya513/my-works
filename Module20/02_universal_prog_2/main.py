# TODO здесь писать код
def is_prime(variable, val):
    k = 0
    for i_index in range(2, (variable // 2) + 1):
        if variable % i_index == 0:
            k += 1
    if k == 0:
        return val

def crypto(string):
    string = list(string)
    s = [values for index, values in enumerate(string) if is_prime(index, values)]
    return s

print(crypto((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
