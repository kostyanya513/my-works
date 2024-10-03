count = 0
print('Изначальный список: ', end = '')
nums = [1, 15, -3, 0, 10]
print(nums)
for index in range(len(nums)):
    for comparison in range(index, len(nums)):
        if nums[comparison] < nums[index]:
            nums[comparison], nums[index] = nums[index], nums[comparison]

print('Отсортированный список:', nums)