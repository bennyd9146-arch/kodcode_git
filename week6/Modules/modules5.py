def add_item(item, bag=None):
    if bag == None:
        bag = []
    bag.append(item)
    return bag
print(add_item("abc"))
