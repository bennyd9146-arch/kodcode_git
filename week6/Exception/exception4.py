def parse_ints(values):
    numbers = []
    for value in values:


        try:
            numbers.append(int(value))
        except (TypeError,ValueError):
            continue
    return numbers
print(parse_ints([1,2,3,"h","t",5]))