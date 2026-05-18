def num_in_nums(nums : tuple ,n : int ):
    count = 0
    for num in nums:
        if n == num:
            count += 1
    return count

print(num_in_nums((1,2,3,2,5,4,2,3),2)) 