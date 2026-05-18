def secound(nums:list):
    max_num = int()
    for num in nums:
        if max_num < num:
            max_num = num

    second_num = None
    for num in nums:
        if num < max_num:
            if second_num is None or num > second_num:
                second_num = num

    return second_num
            
          
            
print(secound([10,10,10]))        