from functools import reduce


def foldrArray(f):
    def ap_init(init):
        def ap_xs(xs):
            acc = init
            for each in reversed(xs):
                acc = f(each)(acc)
            return acc

        return ap_xs

    return ap_init


def foldlArray(f):
    def ap_init(init):
        def ap_xs(xs):
            acc = init
            for each in xs:
                acc = f(acc)(each)
            return acc

        return ap_xs

    return ap_init
