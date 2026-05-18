def count_keys(values : tuple):
    count = {}
    for value in values:
        if value in count:
            count[value] + 1
        else:
            count[value] = 1

    return tuple(count.items())

print(count_keys(("a","d","e","t","t","d","b","b","a")))

