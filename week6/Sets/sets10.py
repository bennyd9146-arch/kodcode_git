def symmetric_difference(nums1:list,nums2:list):
    nums = nums1 + nums2
    nums = set(nums)
    return list(nums)
print(symmetric_difference([1,2,3,4,5],[3,4,5,6,7]))    