nums = open('numbers.txt', 'r', encoding='utf-8')
summ = 0
for elem in nums:
    if elem.join(elem.split()):
        summ += int(elem.join(elem.split()))
nums.close()

answer = open('answer.txt', 'w')
writing_to_file = answer.write(str(summ))
answer.close()
