def revers(nums : tuple):
    revers_nums = []
    nums = list(nums)
    for num in nums:
        revers_nums = [num] + revers_nums

    return tuple(revers_nums)

print(revers((1,2,3,4,5)))