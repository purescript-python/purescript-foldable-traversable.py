def mapWithIndexArray(f):
    # This is a trick for speed up.
    # CPython details:
    #   loading default argument is about 10% faster than freevars.
    return lambda xs, f=f: tuple(f(i)(x) for i, x in enumerate(xs))
