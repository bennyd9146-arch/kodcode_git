def swap_pairs(nums:tuple):
    revers_even = []
   
    for num in range(0,len(nums),2):
   
        revers_even.append(nums[num + 1])
        revers_even.append(nums[num])
   
    return tuple(revers_even)

print(swap_pairs((1,2,3,4,5,8)))