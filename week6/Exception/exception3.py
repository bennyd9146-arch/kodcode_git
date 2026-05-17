def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"
    
print(get_value({"a":1},"b"))