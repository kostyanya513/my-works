def sum(terms, summ=0):
    if isinstance(terms, (int, float)):
        summ += terms
    elif isinstance(terms, list):
        for next_term in terms:
            summ += sum(next_term)
        else:
            sum(next_term)

    return summ


list_terms = [1, 2, 3, 4, 5]
print(sum(list_terms))
