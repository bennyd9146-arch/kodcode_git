def count_errors(funcs):
    errors = 0
    for func in funcs:
        try:
            func()
        except Exception:
            errors += 1
    return errors

