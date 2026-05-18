def remove_duplicates(nums : list):
    nums = set(nums)
    return list(nums)
print(remove_duplicates([1,2,2,3,5,6,4,4,5,5]))