def make_counter():
    count = 0
    def print_counter():
        nonlocal count
        count += 1
        return count
    print_counter()
make_counter()