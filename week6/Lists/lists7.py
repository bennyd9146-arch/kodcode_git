def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    list1.sort()
    list2.sort()
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1


    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

print(merge_sorted_lists([1,3,5,7,9],[1,8,7]))