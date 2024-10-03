summ = 0
q = []
with open('numbers.txt', 'r', encoding='utf-8') as nums:
    for elem in nums:
        q.extend(elem.strip().split())
    for number in q:
        summ += int(number)
print(summ)

with open('answer.txt', 'w') as answer:
    writing_to_file = answer.write(str(summ))