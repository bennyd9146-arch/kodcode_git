def set_age(age):
    try:
        age > 0 or age < 150
        return age

    except ValueError:
        return ValueError
    
set_age(100)