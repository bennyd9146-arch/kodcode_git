def sum_nums(nums : tuple):
    
    count = 0
    for num in nums:
        count += num
    return count

print(sum_nums((1,2,3,4,5)))