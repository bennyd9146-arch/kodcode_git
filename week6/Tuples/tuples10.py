def rotate_tuple(nums : tuple, k : int):
    n = len(nums)
    k = k % n 
    
   
    return nums[-k:] + nums[:-k]


print(rotate_tuple((1,2,3,4,5),7))
