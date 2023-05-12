def chained(functions):
    def func(arg):
        for f in functions:
            arg = f(arg)
    return func

