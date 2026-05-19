import math
def public_names(m):
    new_m = []
    for i in dir(m):
        if not i.startswith("_"):
            new_m.append(i)
    return new_m
m = math
print(public_names(m))