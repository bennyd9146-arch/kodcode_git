def min_and_max_num(nums : tuple):
    min_num =  nums[0]
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
        
        elif  num < min_num:
            min_num = num

    return (min_num , max_num)
print(min_and_max_num((1,2,3,5,9,6,5,100,80,30)))