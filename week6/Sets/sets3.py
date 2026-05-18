def common_elements(nums1:list,nums2:list):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1.intersection(nums2))
print(common_elements([1,2,3,4,],[3,4,5,6]))