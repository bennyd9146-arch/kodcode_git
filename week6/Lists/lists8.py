def rotate_list(nums, k):
    n = len(nums)
    k = k % n 
    
   
    return nums[-k:] + nums[:-k]


print(rotate_list([1,2,3,4,5],7))

