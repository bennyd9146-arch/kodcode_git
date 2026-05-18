def merge_and_sort(nums1:tuple , nums2:tuple):
    tmp_merge = []
    merge = []

    for num in nums1:
        tmp_merge.append(num)
    for num in nums2:
        tmp_merge.append(num)
   
    for num1 in tmp_merge:
        for num2 in range(num1):
            if num1 > num2:
                merge.append(num2)
            else:
                merge.append(num1)

print(merge_and_sort((2,5,1,0),(8,6,9,7,10)))