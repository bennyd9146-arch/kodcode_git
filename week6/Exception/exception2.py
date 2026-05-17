def safe_divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return "undefined"
    
safe_divide(5,0)
    