def distinct_words(item:str):
    item = item.lower().split()
    item = set(item)
    
    return len(item)
print(distinct_words("The cat and the dog and the bird"))