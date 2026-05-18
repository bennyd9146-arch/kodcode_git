def unique_characters(value:str):
    return len(set(value)) == len(value)
 
        
print(unique_characters("hello"))