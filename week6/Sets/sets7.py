def first_repeated_element(nums:list):
    new = set()
    for item in nums:
        if item in new:
            return item
        new.add(item)
    return None
print(first_repeated_element([1,2,3,4,5]))