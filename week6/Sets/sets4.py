def element_one(nums1:list,nums2:list):
    nums1 = set(nums1)
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1.symmetric_difference(nums2))
print(element_one([1,2,3,4,],[3,4,5,6]))