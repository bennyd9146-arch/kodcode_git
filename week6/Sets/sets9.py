def pair_sum_exists(nums:list,result:int):
    new = set()
    for num in nums:
        coplement = result - num
        if coplement in new:
            return True
        else:
            new.add(num)
    
    return False
print(pair_sum_exists([1,2,3,4,5,6],6))