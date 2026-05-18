def difrents_digit(nums:list):
    tmp = []
    count = 0
    for num in nums:
        if num not in tmp:
           tmp.append(num)
           count += 1
    return count
print(difrents_digit([1,2,3,2,3,5,3,4,6,5,9,8,6]))