def safe_int(s):
    try:
        return int(s)
    except Exception:
       return None
    
safe_int("d")    

