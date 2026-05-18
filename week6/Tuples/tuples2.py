def max_nums(nums:tuple):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
print(max_nums((10,5,40,80,100,50)))