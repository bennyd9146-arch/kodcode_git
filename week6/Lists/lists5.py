nums = [1,5,3,4,5,1,3,9]
new_mums = []
for num in nums:
    if num not in new_mums:
        new_mums.append(num)
print(new_mums)