def is_subest(nums1:list,nums2:list):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return nums2.issubset(nums1)
    
print(is_subest([1,2,3,4,5],[1,2,3]))